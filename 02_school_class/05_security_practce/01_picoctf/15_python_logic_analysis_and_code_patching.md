# PicoCTF: Serpentine - Technical Analysis & Code Patching

## 1. Challenge Overview
The **Serpentine** challenge focuses on basic Python logic, flow control, and understanding how functions are called within a script. The goal is to retrieve a hidden flag by analyzing and modifying the provided Python source code.

## 2. Technical Concepts
### ASCII Art and Multi-line Strings
The script uses triple quotes (`'''`) to display a large snake figure using ASCII art. This is a common way in Python to handle pre-formatted, multi-line string data.

### XOR Decryption Logic
The core cryptographic element is the `str_xor` function. It takes an encrypted string and a key, then performs a bitwise XOR operation.
- **Key Repeating:** If the key is shorter than the secret, the script repeats the key until the lengths match.
- **Reversibility:** XOR is symmetric; applying the same key to the ciphertext reveals the original plaintext.

## 3. Vulnerability & Solution
### The "Broken" Flow
In the original `main()` function, the menu option `b` (intended to print the flag) was programmed to only print a reminder message instead of executing the decryption function:
```python
elif choice == 'b':
    print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
```
The Patch
To solve this, the source code must be "patched" to call the print_flag() function when the user selects option b.

## 4. Source Code (Complete Script)

```python
import random
import sys

def str_xor(secret, key):
    # extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5c) + chr(0x01) + chr(0x57) + chr(0x2a) + chr(0x17) + chr(0x5e) + chr(0x5f) + chr(0x0d) + chr(0x3b) + chr(0x19) + chr(0x56) + chr(0x5b) + chr(0x5e) + chr(0x36) + chr(0x53) + chr(0x07) + chr(0x51) + chr(0x18) + chr(0x58) + chr(0x05) + chr(0x57) + chr(0x11) + chr(0x3a) + chr(0x0f) + chr(0x0e) + chr(0x59) + chr(0x06) + chr(0x4d) + chr(0x55) + chr(0x0c) + chr(0x0f) + chr(0x14)

def print_flag():
    # 'enkidu' is the key used for XOR decryption
    flag = str_xor(flag_enc, 'enkidu')
    print(flag)

def print_encouragement():
    encouragements = ['You can do it!', 'Keep it up!', 'Look how far you\'ve come!']
    choice = random.choice(range(0, len(encouragements)))
    print('\n' + '-'*53)
    print(encouragements[choice])
    print('-'*52 + '\n\n')

def main():
    print('''
    Y
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
    | |     /  /       \   \             .' .~       ~-. `.
    | |    /  /         )   )           /  /             `.`.
    \ \_ _/  /         /   /           /  /                `'
     \_ _ _.'         /   /           (  (
                     /   /             \  \\
                    /   /               \  \\
                   /   /                 )  )
                  (   (                 /  /
                   `.  `.             .'  /
                     `.  ~ - - - - ~  .'
                       ~ . _ _ _ _ . ~
    ''')
    print('Welcome to the serpentine encourager!\n\n')
    
    while True:
        print('a) Print encouragement')
        print('b) Print flag')
        print('c) Quit\n')
        choice = input('What would you like to do? (a/b/c) ')
        
        if choice == 'a':
            print_encouragement()
        elif choice == 'b':
            # FIX: Call the actual function instead of a print statement
            print_flag()
        elif choice == 'c':
            sys.exit(0)
        else:
            print('\nI did not understand "' + choice + '", input only "a", "b" or "c"\n\n')

if __name__ == "__main__":
    main()

```
## 5. Conclusion
By modifying the program's execution flow using a text editor (like nano), we bypass the intended restriction and force the program to reveal the decrypted flag using the existing print_flag and str_xor functions.
