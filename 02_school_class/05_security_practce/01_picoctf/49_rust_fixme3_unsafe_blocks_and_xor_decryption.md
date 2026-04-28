# 49. Rust fixme3 — Unsafe Blocks and XOR Decryption (picoCTF 2025)

## Challenge Overview

- **Platform:** picoCTF 2025
- **Category:** General Skills
- **Difficulty:** Easy
- **Title:** Rust fixme 3
- **Hint:** "Read the comments...darn it!"

### Description

> Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!

---

## What I Learned

### 1. What is Rust?

Rust is a systems programming language focused on **memory safety** and **performance**. Unlike Python (an interpreted language), Rust is a **compiled language** — meaning the source code must be translated into machine code before it can be executed.

| Feature | Python | Rust |
|---|---|---|
| Execution | Interpreted (line-by-line) | Compiled (translated all at once) |
| Memory management | Automatic (garbage collector) | Manual but safe (ownership system) |
| Package manager | pip | cargo |
| Run command | `python main.py` | `cargo run` |

The name "Rust" comes from rust fungi — symbolically, it represents fixing the "rusty" memory issues found in older languages like C and C++.

---

### 2. What is `cargo run`?

`cargo` is Rust's **build tool and package manager**, similar to `pip` in Python.

- `cargo run` = compile the project + run the resulting binary
- `cargo build` = compile only, without running
- Dependencies are declared in `Cargo.toml` and downloaded automatically on first run

---

### 3. What is `unsafe` in Rust?

Rust's core promise is **memory safety** — it prevents bugs like null pointer dereferences, buffer overflows, and use-after-free errors at compile time.

However, some low-level operations **require direct memory access**, which Rust cannot verify as safe. For these cases, Rust provides the `unsafe { }` block, which tells the compiler:

> "I know this is dangerous. I'm taking responsibility."

**Key rule:** Any call to an unsafe function **must** be wrapped inside an `unsafe { }` block. If it isn't, the compiler will refuse to compile the code.

---

## The Bug

The downloaded file `main.rs` contained the following code — with the `unsafe { }` block **commented out**:

```rust
// unsafe {
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    let decrypted_ptr = decrypted_buffer.as_ptr();
    let decrypted_len = decrypted_buffer.len();
    let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);  // unsafe function!
    borrowed_string.push_str(&String::from_utf8_lossy(decrypted_slice));
// }
```

`std::slice::from_raw_parts()` is an **unsafe function** because it directly reads from a raw memory pointer — a potentially dangerous operation. Calling it outside an `unsafe { }` block causes a compile error.

The **hint** in the comments was explicit:
```
// Did you know you have to do "unsafe operations" in Rust?
// This is where unsafe rust comes in...
```

---

## The Fix

Remove the `//` comment markers from the `unsafe { }` block:

```rust
unsafe {
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    let decrypted_ptr = decrypted_buffer.as_ptr();
    let decrypted_len = decrypted_buffer.len();
    let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);
    borrowed_string.push_str(&String::from_utf8_lossy(decrypted_slice));
}
```

---

## How to Find Bugs in Rust

Even without knowing Rust, the compiler gives highly descriptive error messages:

```
error[E0133]: call to unsafe function is unsafe and requires unsafe function or block
  --> src/main.rs:26:28
   |
26 |         let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);
   |                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |                               unsafe function call must be in unsafe block
```

- The `^^^^^` arrows point directly to the problematic line
- The error message explains **exactly what is wrong** and what is required
- For a fixme-style CTF challenge, simply running `cargo run` and reading the errors is often enough to solve it

---

## Code Walkthrough

```rust
use xor_cryptor::XORCryptor;
```
Import an external library — equivalent to Python's `import`.

```rust
fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
```
Define a function called `decrypt`. It takes:
- `Vec<u8>` — a list of bytes (the encrypted flag data)
- `&mut String` — a mutable reference to a String (can be modified inside the function)

```rust
let key = String::from("CSUCKS");
```
The XOR decryption key hardcoded in the file.

```rust
let res = XORCryptor::new(&key);
if res.is_err() { return; }
let xrc = res.unwrap();
```
Create the decryption object. If it fails, exit early. Otherwise, unwrap and use it.

```rust
unsafe {
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
```
Decrypt the encrypted byte array using XOR.

```rust
    let decrypted_ptr = decrypted_buffer.as_ptr();
    let decrypted_len = decrypted_buffer.len();
```
Get the raw memory address (pointer) and length of the decrypted data — low-level memory access.

```rust
    let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);
```
Reconstruct a readable slice of data from the raw pointer. This is the **unsafe operation** — it bypasses Rust's normal safety checks.

```rust
    borrowed_string.push_str(&String::from_utf8_lossy(decrypted_slice));
}
println!("{}", borrowed_string);
```
Convert the decrypted bytes to a UTF-8 string and append it to the output. Then print the full message including the flag.

```rust
let hex_values = ["41", "30", "20", ...];
let encrypted_buffer: Vec<u8> = hex_values.iter()
    .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
    .collect();
```
Convert hex strings like `"41"` to actual byte values like `65`. Equivalent to Python:
```python
encrypted_buffer = [int(h, 16) for h in hex_values]
```

---

## Steps to Solve

1. Download and extract `fixme3.tar.gz`
2. Install Rust from https://rustup.rs
3. Open the project folder in VS Code
4. Edit `src/main.rs` — remove `//` from the `unsafe {` and `}` lines
5. Open terminal and navigate to the project folder:
   ```powershell
   cd C:\Users\<username>\Downloads\fixme3\fixme3
   cargo run
   ```
6. Read the flag from the terminal output

> **Note:** After installing Rust, restart VS Code so the terminal recognizes the `cargo` command.

---

## Flag

```
picoCTF{n0w_y0uv3_f1x3d_1h3m_411}
```

---

## Key Takeaways

- Rust separates **safe** and **unsafe** code explicitly — unsafe operations must be declared
- `cargo` handles compilation, dependency management, and execution in one tool
- Rust's compiler error messages are detailed and tell you exactly where and why code fails
- For fixme CTF challenges, reading **both the comments and the compiler errors** is the primary strategy
- XOR encryption is a simple symmetric cipher — the same key used to encrypt is used to decrypt
