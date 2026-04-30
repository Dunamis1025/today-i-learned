# Git Workflow & PowerShell Commands – Today I Learned

## Overview
For the first time, I restructured my GitHub repository directly through the terminal (Windows PowerShell in VSCode) instead of using the GitHub website or GUI. This document covers the core Git commands I used and key lessons learned, including mistakes and how I recovered from them.

---

## Core Git Commands

### 1. Sync Local with GitHub (Download)
```bash
git pull
```
- Downloads the latest changes from GitHub to your local machine
- **Always run this before starting any work** — if your local is outdated and you push, you may overwrite the latest content

### 2. Force Local to Match GitHub (Hard Reset)
```bash
git fetch origin
git reset --hard origin/main
```
- Used when `git pull` fails due to conflicts between local and remote files
- `git fetch origin` — downloads the latest info from GitHub without applying it yet
- `git reset --hard origin/main` — forcefully overwrites local files to match GitHub exactly
- **Warning:** All local changes will be permanently lost. Only use this when you're sure local files are not needed.

### 3. Move or Rename Files/Folders (Preserving History)
```bash
git mv original/path new/path
```
- Moves or renames files/folders while keeping commit history intact
- If you move files using File Explorer instead, Git treats it as "deleted + new file", which breaks the commit history
- Always use `git mv` for moving files within a Git repository

### 4. Stage All Changes
```bash
git add -A
```
- Stages all changes (new files, modifications, deletions) and prepares them for commit
- `-A` stands for "All"
- Think of it as: packing items into a box before sealing it

### 5. Commit (Save a Snapshot)
```bash
git commit -m "your commit message here"
```
- Saves a snapshot of your staged changes to local Git history
- `-m` flag lets you write the commit message inline
- Common message prefixes used by convention:
  - `feat:` — adding new content or feature
  - `refactor:` — restructuring without changing content
  - `fix:` — fixing an error
  - `add:` — adding new files

### 6. Push to GitHub (Upload)
```bash
git push
```
- Uploads your local commits to GitHub
- This is one-directional: Local → GitHub
- The opposite direction (GitHub → Local) is `git pull`

### 7. Undo the Last Commit (Revert)
```bash
git revert HEAD
git push
```
- Creates a new commit that undoes the last commit — does NOT delete history
- Safe way to recover from mistakes on a shared or public repository
- When Vim editor opens after `git revert HEAD`:
  - Type `:wq` and press Enter to save and exit

---

## Git Flow: The 3-Stage Model
Working Directory → Staging Area → Local Repository → GitHub
(edit files)     (git add -A)    (git commit)      (git push)

Analogy:
- `git add -A` = Pack items into a box
- `git commit -m` = Seal the box and write the label
- `git push` = Ship the package

---

## PowerShell vs Bash — Key Differences

Git commands themselves are the same across all platforms, but general terminal commands differ between Windows PowerShell and Linux/Mac Bash.

### Finding a Folder
```bash
# Linux / Mac (Bash)
find ~ -name "today-i-learned" -type d 2>/dev/null

# Windows (PowerShell)
Get-ChildItem -Path C:\Users\username -Recurse -Directory -Filter "today-i-learned"
```

### Creating Nested Folders
```bash
# Linux / Mac (Bash)
mkdir -p folder/subfolder

# Windows (PowerShell)
New-Item -ItemType Directory -Path "folder/subfolder"
```

### Moving Multiple Files with Wildcard
```bash
# Linux / Mac (Bash) — works fine
git mv folder/*.md destination/

# Windows (PowerShell) — wildcard (*) does NOT work with git mv
# Use this instead:
Get-ChildItem folder -Filter "*.md" | ForEach-Object { git mv "folder/$($_.Name)" "destination/" }
```

---

## Lessons Learned

### Always `git pull` Before Working
If your local clone is outdated and you push changes, you risk overwriting the latest commits on GitHub. Always sync first.

### Enter Commands One Line at a Time
Pasting multiple lines at once in PowerShell can cause them to execute all at once in unexpected ways. Enter each command individually and confirm the result before moving on.

### `git revert` is Not Scary
Git keeps full history — mistakes are recoverable. `git revert HEAD` safely undoes the last commit by creating a new "undo commit" rather than deleting anything.

### Terminal Environments Have Different Syntax
Windows PowerShell, Linux Bash, and Mac Zsh are different environments. The same task may require different commands. Always check which environment you're in before running commands.

### `git mv` vs Moving Files Manually
Moving files through File Explorer or drag-and-drop breaks Git history because Git sees it as delete + new file. Always use `git mv` to preserve the full commit history.

---

## Quick Reference

| Task | Command |
|------|---------|
| Download latest from GitHub | `git pull` |
| Force reset local to GitHub | `git fetch origin` + `git reset --hard origin/main` |
| Move/rename file or folder | `git mv old/path new/path` |
| Stage all changes | `git add -A` |
| Commit with message | `git commit -m "message"` |
| Upload to GitHub | `git push` |
| Undo last commit safely | `git revert HEAD` + `git push` |
| Exit Vim editor | `:wq` + Enter |
