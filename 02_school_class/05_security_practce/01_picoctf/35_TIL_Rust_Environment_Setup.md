import os

# Define the content for the TIL markdown file
til_content = """# Today I Learned: 2026-04-17

## Topic: Troubleshooting Rust Development Environment on Windows

Today, I attempted to solve the **picoCTF "Rust fixme 1"** challenge. Although I faced significant environment configuration issues, I gained practical experience in setting up a systems-level development environment.

### 1. Understanding Rust Project Structure
- Learned that a Rust project is managed by **Cargo**, which uses `Cargo.toml` for dependency management and `src/main.rs` for the source code.
- Identified that external crates (libraries) like `xor_cryptor` cannot be executed in standard online playgrounds without explicit dependency definitions.

### 2. Windows Environment Variable (PATH) Challenges
- Experienced the importance of the **System PATH**. Even after installing Rust via `rustup`, the terminal may not recognize the `cargo` command if the `~/.cargo/bin` directory is not correctly indexed.
- Practiced manual environment variable configuration using the `setx` command and the Windows System Properties GUI.

### 3. Visual Studio Build Tools Requirement
- Realized that Rust on Windows requires the **C++ Build Tools** and Windows SDK. I successfully installed over 5GB of necessary dependencies, including the MSVC compiler.

### 4. Language Logic Translation (Rust to Python)
- Attempted to bypass environment issues by translating Rust logic into Python. 
- Learned about **XOR cipher** mechanics and how character encoding (UTF-8 vs. ASCII) and terminal rendering can cause "mojibake" (garbled text) when outputting decrypted bytes.

### 5. Debugging & Persistence
- Practiced reading complex compiler error messages from the Rust compiler, which provides specific hints like `help: format specifiers use curly braces`.
- Maintained persistence through multiple reboots and manual configuration attempts, a crucial trait for a cybersecurity professional.

---
**Summary:** While the "flag" was not captured today due to persistent local environment conflicts, the deep dive into system paths, build engines, and cross-language logic was a highly valuable engineering exercise.
"""

# Save as a markdown file
file_path = "35_TIL_Rust_Environment_Setup.md"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(til_content)

print(f"File saved to {file_path}")
