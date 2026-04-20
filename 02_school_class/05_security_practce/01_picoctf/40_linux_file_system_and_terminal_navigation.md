# [picoCTF] Magikarp Ground Mission - Writeup

## 1. Challenge Overview
- **Category**: General Skills
- **Points**: 30
- **Concepts**: SSH (Secure Shell), Linux File System Hierarchy, Terminal Navigation

## 2. Problem Description
The challenge requires navigating through a remote Linux server via SSH to locate three separate pieces of a flag hidden in different directories. This exercise tests the ability to move between directories and read file contents using the command line.

## 3. Technical Procedure

### Phase 1: Establishing Connection
Connected to the remote challenge instance using the Secure Shell (SSH) protocol on a non-standard port.
```bash
# Syntax: ssh [user]@[host] -p [port]
ssh ctf-player@wily-courier.picoctf.net -p 65325
```
*Input the provided password `8c606eb1` when prompted.*

### Phase 2: Locating the First Fragment
Upon login, the terminal defaults to the user's Home Directory.
```bash
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt

ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_
```
* **Result**: Found the first part of the flag and instructions to proceed to the Root directory.

### Phase 3: Navigating to the Root Directory
Moved to the absolute top of the file system hierarchy (Root) to find the second fragment.
```bash
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls
2of3.flag.txt  bin  boot  dev  etc  home  instructions-to-3of3.txt ...

ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_of_//4t3r_
```
* **Result**: Successfully retrieved the middle portion of the flag.

### Phase 4: Returning to the Home Directory
Followed the instructions to return to the user's personal directory space.
```bash
ctf-player@pico-chall$ cd ~
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in

ctf-player@pico-chall$ cat 3of3.flag.txt
0b24fc4f}
```
* **Result**: Obtained the final fragment.

## 4. Key Takeaways
### Linux Directory Concepts
- **Root Directory (`/`)**: The top-level directory of the entire file system. It contains all other directories and files, similar to `C:\` in Windows but more centralized.
- **Home Directory (`~`)**: The personal workspace for the current user (e.g., `/home/ctf-player`). Users typically have full permissions here but restricted permissions in the Root directory.


### Essential Commands Used
| Command | Purpose |
| :--- | :--- |
| `ls` | List directory contents |
| `cd /` | Change directory to Root |
| `cd ~` | Change directory to Home |
| `cat` | Concatenate and display file content |

## 5. Final Flag
**Flag**: `picoCTF{xxsh_0ut_of_//4t3r_0b24fc4f}`
