# 36_rust_fixme1_ctf_writeup.md

## Challenge: Rust Fixme 1
- **Platform:** picoCTF 2025
- **Category:** General Skills
- **Difficulty:** Easy
- **Points:** 100

---

## Summary

Fixed three syntax errors in a Rust source file to decrypt and print the flag. The challenge required setting up a local Rust environment because the picoCTF webshell could not compile the project due to resource limitations.

---

## What Happened First (and Why It Failed)

I initially tried to solve this in the picoCTF webshell. The file downloaded and extracted fine, but `cargo run` failed with:

```
error: could not compile `rayon` (lib)
signal: 9, SIGKILL: kill
```

The webshell environment has strict memory and resource limits. Rust compiles heavyweight dependency crates like `rayon` locally, and the webshell killed the process before it could finish. The challenge page even warned: **"This problem is not solvable with the webshell."**

---

## Environment Setup (WSL + Ubuntu)

Since the webshell failed, I needed a local Linux environment. On Windows, that means WSL (Windows Subsystem for Linux) — a feature that runs a Linux environment inside Windows.

Steps taken:

1. Checked WSL status in PowerShell:
```powershell
wsl --list --verbose
# Result: no installed distributions
```

2. Installed Ubuntu from the Microsoft Store

3. Launched Ubuntu, created a UNIX username and password

4. Inside Ubuntu, installed Rust:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

5. Installed build-essential (C compiler required by Rust's build system):
```bash
sudo apt-get update --fix-missing
sudo apt install build-essential -y
```

> **Why build-essential?** Rust's compiler internally uses a C linker (`cc`) to produce the final binary. Without it, the build fails with `error: linker 'cc' not found`.

---

## Downloading and Extracting the Challenge

```bash
cd ~
wget https://challenge-files.picoctf.net/c_verbal_sleep/3f0e13f541928f420d9c8c96b06d4dbf7b2fa18b15adbd457108e8c80a1f5883/fixme1.tar.gz
tar -xvf fixme1.tar.gz
cd fixme1
```

---

## The Three Bugs

Opened the source file with nano (a terminal text editor):
```bash
nano src/main.rs
```

### Bug 1 — Missing semicolon (Line 5)
```rust
// Before
let key = String::from("CSUCKS")

// After
let key = String::from("CSUCKS");
```
In Rust, every statement must end with a semicolon. Python doesn't require this, but Rust does — omitting it is a syntax error.

### Bug 2 — Invalid return keyword (Line 18)
```rust
// Before
ret;

// After
return;
```
Rust does not have a `ret` shorthand. The compiler treated it as an undefined variable name and threw `error[E0425]: cannot find value 'ret' in this scope`.

### Bug 3 — Wrong format specifier in println! (Line 25)
```rust
// Before
println!(":?", String::from_utf8_lossy(&decrypted_buffer));

// After
println!("{}", String::from_utf8_lossy(&decrypted_buffer));
```
In Rust's `println!` macro, `{}` is the standard display formatter. `:?` is a debug formatter and must also be wrapped in braces as `{:?}`. Using `:?` alone caused `error: argument never used`.

---

## Running the Fixed Code

```bash
cargo run
```

Output:
```
picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}
```

---

## Key Concepts Learned

| Term | What it is |
|------|-----------|
| WSL | Windows feature that runs Linux inside Windows |
| Ubuntu | A Linux-based operating system (distro) |
| Terminal | Text-based command interface — like MS-DOS |
| Rust | A compiled programming language (like C, unlike Python) |
| Cargo | Rust's package manager and build tool |
| `cargo run` | Compiles and runs a Rust project |
| nano | Terminal text editor |
| build-essential | Linux package containing the C compiler toolchain |
| Compiled language | Code must be translated to machine code before running (vs Python which runs line by line) |

---

## Reflection

The actual code fix was straightforward — three small changes. The real challenge today was **environment setup**: understanding why the webshell failed, installing WSL, configuring Ubuntu from scratch, and resolving the missing C linker error. This mirrors real-world IT work where getting the environment right is often harder than the task itself.

---

## Flag
```
picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}
```
