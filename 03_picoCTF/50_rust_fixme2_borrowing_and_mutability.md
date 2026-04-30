# 50. Rust Fixme 2 — Borrowing & Mutability in Rust

**Category:** General Skills | **Difficulty:** Easy | **Platform:** picoCTF 2025  
**Flag:** `picoCTF{4r3_y0u_h4v1n5_fun_y31?}`

---

## What This Challenge Is About

This challenge teaches one of Rust's most important concepts: **ownership, borrowing, and mutability**.

Unlike Python or Java, Rust has **no garbage collector (GC)**. Instead, the compiler enforces strict rules about who owns memory and who can modify it. This means bugs that would only crash your program at runtime in other languages are caught **before the program even runs** in Rust.

---

## Key Concepts Learned

### 1. Variables are Immutable by Default

In Rust, every variable is **read-only by default**. If you want to modify a variable, you must explicitly mark it with `mut`.

```rust
// ❌ Error: cannot mutate an immutable variable
let name = String::from("hello");
name.push_str(" world");

// ✅ Works: mut allows modification
let mut name = String::from("hello");
name.push_str(" world");
```

### 2. References: `&` vs `&mut`

When you pass a variable to a function, you can either:
- **Move** it (the original owner loses access), or
- **Borrow** it with a reference (`&`)

A regular reference (`&`) is **read-only**. If you want the function to be able to **modify** the value, you need a **mutable reference** (`&mut`).

| Syntax | Meaning |
|--------|---------|
| `&x` | Immutable reference — read only |
| `&mut x` | Mutable reference — read and write |

```rust
fn add_text(s: &String) {
    s.push_str("!"); // ❌ Error: s is read-only
}

fn add_text(s: &mut String) {
    s.push_str("!"); // ✅ Works: s is mutable
}
```

### 3. Matching `mut` Consistently

When you pass a `&mut` reference to a function, **three things** must all say `mut`:

1. The variable itself must be declared with `let mut`
2. The function parameter must accept `&mut Type`
3. The call site must pass `&mut variable`

If any one of these is missing, Rust will refuse to compile.

---

## The Bug: What Was Wrong

The downloaded file had 3 places where `mut` was missing:

### Bug 1 — Function signature missing `mut`

```rust
// ❌ Before
fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &String) {

// ✅ After
fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
```

Inside `decrypt()`, the code calls `borrowed_string.push_str(...)` — which **modifies** the string. But the parameter said `&String` (read-only), so Rust blocked it.

### Bug 2 — Variable not declared as mutable

```rust
// ❌ Before
let party_foul = String::from("Using memory unsafe languages is a: ");

// ✅ After
let mut party_foul = String::from("Using memory unsafe languages is a: ");
```

To pass a `&mut` reference, the original variable must itself be declared `mut`.

### Bug 3 — Wrong reference type at call site

```rust
// ❌ Before
decrypt(encrypted_buffer, &party_foul);

// ✅ After
decrypt(encrypted_buffer, &mut party_foul);
```

Even if the function expects `&mut`, you must explicitly pass `&mut` — Rust won't do it automatically.

---

## Fixed Code

```rust
use xor_cryptor::XORCryptor;

fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
    let key = String::from("CSUCKS");

    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");

    let res = XORCryptor::new(&key);
    if res.is_err() {
        return;
    }
    let xrc = res.unwrap();

    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    borrowed_string.push_str(&String::from_utf8_lossy(&decrypted_buffer));
    println!("{}", borrowed_string);
}

fn main() {
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76",
                      "01", "1c", "7e", "59", "63", "e1", "61", "25",
                      "0d", "c4", "60", "f2", "12", "a0", "18", "03",
                      "51", "03", "36", "05", "0e", "f9", "42", "5b"];

    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    let mut party_foul = String::from("Using memory unsafe languages is a: ");
    decrypt(encrypted_buffer, &mut party_foul);
}
```

---

## How to Run

Make sure `Cargo.toml` includes the dependency:

```toml
[dependencies]
xor_cryptor = "1.0.0"
```

Then run from the project root (not `src/`):

```bash
cd fixme2
cargo run
```

Output:
```
Using memory unsafe languages is a: PARTY FOUL! Here is your flag: picoCTF{4r3_y0u_h4v1n5_fun_y31?}
```

---

## Why Rust Does This

| Language | Memory Safety | How |
|----------|--------------|-----|
| C / C++ | ❌ Manual | You manage memory; mistakes cause crashes |
| Java / Python | ✅ GC | Garbage collector cleans up automatically (slower) |
| Rust | ✅ No GC | Compiler enforces rules at compile time (fast & safe) |

Rust's `mut` system forces you to be **explicit** about what can change and what can't. It's annoying at first, but it eliminates entire categories of bugs — like accidentally modifying data you weren't supposed to touch.

---

## Summary

| Concept | Rule |
|---------|------|
| `let x` | Immutable — cannot be changed |
| `let mut x` | Mutable — can be changed |
| `&x` | Borrow read-only |
| `&mut x` | Borrow with write permission |
| All three must match | `let mut` + `&mut Type` + `&mut var` |
