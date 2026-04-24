# 47. picoCTF - Collaborative Development Write-up

## Challenge Info

| Field      | Detail                  |
|------------|-------------------------|
| Name       | Collaborative Development |
| Category   | General Skills          |
| Difficulty | Easy                    |
| Year       | picoCTF 2024            |
| Tags       | git, browser_webshell_solvable |

## Problem Description

> My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?

A `challenge.zip` file is provided. The goal is to merge multiple Git branches to reconstruct a complete flag-printing Python script.

## Concepts Learned

- **Git branching**: Multiple team members working on separate branches simultaneously
- **Git merging**: Combining branch changes into `main` using `git merge`
- **Merge conflicts**: When two branches modify the same file, Git cannot auto-merge and requires manual resolution
- **Conflict markers**: Git marks conflicts in files using `<<<<<<<`, `=======`, `>>>>>>>` syntax
- **Git config**: Must set `user.name` and `user.email` before committing

## Solution Steps

### Step 1: Download and Extract

```bash
wget <challenge_zip_url>
unzip challenge.zip
cd drop-in   # Note: extracts to 'drop-in', not 'challenge'
```

### Step 2: Check Available Branches

```bash
git branch -a
```

Output:
```
  feature/part-1
  feature/part-2
  feature/part-3
* main
  master
```

### Step 3: Configure Git Identity

```bash
git config user.email "a@a.com"
git config user.name "a"
```

Required before committing. Git needs to know who is making the commit.

### Step 4: Merge Each Branch

```bash
git merge feature/part-1   # Success (Fast-forward)
git merge feature/part-2   # CONFLICT in flag.py
```

### Step 5: Resolve Merge Conflict

Open the conflicted file:
```bash
nano flag.py
```

The file will contain conflict markers like:
```
<<<<<<< HEAD
print("picoCTF{t3@mw0rk_", end="")
=======
print("m@k3s_th3_dr3@m_", end="")
>>>>>>> feature/part-2
```

**Resolution:** Keep both `print` statements and delete all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

Save and exit nano: `Ctrl+O` → Enter → `Ctrl+X`

### Step 6: Commit the Fix and Continue Merging

```bash
git add flag.py
git commit -m "fix conflict"
git merge feature/part-3   # CONFLICT again
```

Repeat Step 5 for the second conflict (part-3 adds the final segment of the flag).

```bash
git add flag.py
git commit -m "fix conflict2"
```

### Step 7: Run the Script

```bash
python3 flag.py
```

Output:
```
Printing the flag...
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_4c24302f}
```

## Flag

```
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_4c24302f}
```

## Key Takeaways

- Always `cd` into the correct extracted folder — zip files don't always extract to an expected directory name
- `git branch -a` lists all branches including remote-tracking ones
- Merge conflicts must be resolved manually by editing the file and removing conflict markers
- After resolving a conflict, always `git add <file>` and `git commit` before attempting the next merge
- The nano editor name comes from the SI prefix system: nano < pico, as it was built as a smaller alternative to the `pico` editor
