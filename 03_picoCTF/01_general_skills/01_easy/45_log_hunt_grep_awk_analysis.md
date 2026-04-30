# 45. Log Hunt — grep, awk, and Log Analysis (picoCTF)

## Challenge Overview

- **Platform**: picoCTF (picoGym)
- **Category**: General Skills
- **Difficulty**: Easy
- **Challenge Name**: Log Hunt
- **Solves**: ~40,928
- **Approval Rate**: 94%

### Description

> Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag? Download the logs and figure out the full flag from the fragments.

### Hints

1. You can use `grep` to filter only matching lines from the log.
2. Some lines are duplicates; ignore extra occurrences.

---

## Solution Walkthrough

### Step 1 — Download the log file

```bash
wget <challenge-log-url>/server.log
```

### Step 2 — First attempt: grep for "picoCTF"

```bash
grep "picoCTF" server.log
```

**Result:** Only one repeated fragment appeared — `picoCTF{us3_`

**Why?** The other flag fragments (`sk1lls_`, `y0urlinux_`, `cedfa5fb}`) do **not** contain the string `"picoCTF"`, so they were invisible to this filter.

### Step 3 — Better approach: grep for "flag" (case-insensitive)

```bash
grep -i "flag" server.log | awk '{print $NF}' | sort -u
```

**Result:**

```
cedfa5fb}
picoCTF{us3_
sk1lls_
y0urlinux_
```

### Step 4 — Reconstruct the flag

Reading the fragments semantically:

```
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
```

> "use your linux skills" — the flag meaning guides the correct order.

---

## Command Breakdown

### `grep -i "flag"`

| Part | Meaning |
|------|---------|
| `grep` | Search for lines matching a pattern |
| `-i` | **i**gnore case — matches `FLAG`, `Flag`, `flag`, etc. |
| `"flag"` | The search pattern — matches `FLAGPART` because it contains `flag` |

**Why `-i` mattered here:**  
The log entries used `FLAGPART` (uppercase). Without `-i`, a search for `"flag"` would miss them. With `-i`, all case variants are caught.

---

### `awk '{print $NF}'`

`awk` is a text processing language named after its three creators: **A**ho, **W**einberger, and **K**ernighan.

It automatically splits each line into fields by whitespace and assigns them numbered variables:

```
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
      $1         $2    $3    $4          $5
```

| Symbol | Meaning |
|--------|---------|
| `$1`, `$2`... | Individual fields (columns) by whitespace |
| `NF` | **N**umber of **F**ields — total field count of the current line |
| `$NF` | The **last field** — `$` accesses a field by number, `NF` is always the last index |
| `{ }` | Curly braces wrap the **action block** — what awk does for every matching line |
| `print` | Outputs the value to stdout |

**Why `$NF` instead of `$5`?**  
Different log lines may have different numbers of columns. `$NF` always grabs the last word regardless of line length — making it robust.

---

### `sort -u`

| Part | Meaning |
|------|---------|
| `sort` | Sort lines alphabetically |
| `-u` | **u**nique — remove duplicate lines (short for `--unique`) |

**Why it was needed:**  
Each flag fragment appeared hundreds of times across the log (with different timestamps). `sort -u` collapsed all duplicates into one unique occurrence per fragment.

---

## Why the First Approach Failed

```bash
grep "picoCTF" server.log | sort -u | uniq
```

- `grep "picoCTF"` only matched lines **containing the literal string `picoCTF`**
- The fragments `sk1lls_`, `y0urlinux_`, and `cedfa5fb}` were stored on **separate lines** without `picoCTF` in them
- Those lines were completely invisible to the filter
- `sort -u` and `uniq` only deduplicate — they can't find what `grep` already missed

---

## Key Concepts Learned

| Concept | Summary |
|---------|---------|
| `grep -i` | Case-insensitive search — essential when log formats use uppercase keywords |
| `awk '{print $NF}'` | Extract the last field from each line regardless of column count |
| `$NF` in awk | `NF` = number of fields; `$NF` = value of the last field |
| `{ }` in awk | Action block — commands inside run for every processed line |
| `sort -u` | Sort and deduplicate simultaneously |
| Flag reconstruction | CTF flags split across log lines must be reassembled semantically |
| Random hash suffix | e.g. `cedfa5fb` — appended to flag for uniqueness, has no semantic meaning |

---

## Flag

```
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
```
