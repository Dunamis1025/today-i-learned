# Today I Learned — Holmesglen CTF Aug 2026

**Event:** Holmesglen CTF Aug 2026 (Security Impossible, "Operation Nightjar")
**Date:** 2026-08-15 (10:00 AM – 4:00 PM)
**Team:** Parma Packets (mostly solo — teammate unresponsive)
**Result:** 12 / 49 flags captured, 1300 points
**Categories cleared:** Digital Forensics (650/650), Steganography (650/850)

This was my second CTF ever (first as part of a team). I'm ~1.5 years into
self-teaching cybersecurity, so the goal today was less about the
leaderboard and more about understanding *why* each command works, not
just copy-pasting it.

---

## 1. Digital Forensics

### 01_GhostFile — File carving from unallocated space
A USB `dd` disk image contained a deleted JPEG. Deleted files aren't
immediately erased — their bytes stay in unallocated disk space until
overwritten.

- Used `foremost` (signature-based carving) to recover the deleted photo
  from the raw image by scanning for JPEG file signatures rather than
  relying on the filesystem's file table.
- The recovered photo's **EXIF metadata** (`Comment` field, via `exiftool`)
  contained the flag.

**Key concept:** file carving = recovering files by recognizing their
binary signatures directly in raw disk bytes, ignoring the (broken)
filesystem index.

### 02_ChatWreck — SQLite deleted row recovery
A SQLite database was missing row `id=5` (deleted via `DELETE`, not
dropped/vacuumed).

- SQLite doesn't immediately erase deleted row data — it stays in the
  database's internal **freelist/freeblock** space until the page is
  reused.
- `strings` over the raw `.db` file surfaced the original row text still
  sitting in that freed space, containing the flag.

**Key concept:** "deleted" in most databases/filesystems means
"unlinked", not "wiped" — the bytes persist until something else
overwrites them.

### 03_RanFirst — Reconstructing an intrusion from `.bash_history` + `auth.log`
A full disk image was loop-mounted and inspected.

- `.bash_history` showed the attacker's exact command sequence after a
  successful brute-force login (via `auth.log`).
- The attacker downloaded and ran a malicious script, which dropped a
  hidden C2 (command-and-control) config at `/opt/.cache/.beacon.conf`.
- That file was **Base64-encoded**; decoding it revealed the flag.

**Key concept:** attacker post-exploitation activity is often
reconstructable purely from shell history + auth logs, even without a
live memory capture.

### 05_DeadDrop — Extracting a Base64 MIME attachment from an email
An `.eml` file's message body was a red herring — the actual payload was
a Base64-encoded ZIP file attached to the email.

- `grep -E` was used to isolate only the Base64-looking lines from the
  raw email text (filtering out headers/boundaries).
- Decoded and `unzip`'d the result; `ops_manifest.txt` inside contained
  the flag.

**Key concept:** raw `.eml` files are plain text with MIME
encoding — attachments are just Base64 blobs between boundary markers.

### 06_TimeLine — Correlating `auth.log` and `access.log` to reconstruct an intrusion timeline
Two log files, one attacker IP, three stages of the attack.

**Step 1 — find the brute-forcing IP:**
```bash
grep "Failed password" auth.log | grep -oP 'from \K[\d.]+' | sort | uniq -c | sort -rn
```
`grep -oP 'from \K[\d.]+'` uses a **lookbehind** (`\K` discards everything
matched before it from the output) so only the IP address after the
literal word `from` is captured — this is more robust than counting
fields with `awk '{print $NF}'`, since log lines can have a variable
number of fields (e.g. "invalid user" adds an extra word).

**Step 2 — confirm the successful login:**
```bash
grep "185.243.115.7" auth.log | grep "Accepted"
```

**Step 3 — pivot to the web log with the same IP:**
```
GET /admin              → recon
POST /admin/login       → likely compromised admin creds too
POST /admin/upload      → webshell dropped
GET /uploads/.sess.php?cmd=id            → webshell test
GET /uploads/.sess.php?x=<base64>        → data exfiltration
```

**Step 4 — extract & decode the exfil payload directly from the log,
rather than copy-pasting a long string by hand (which is error-prone):**
```bash
grep -oP '(?<=\.sess\.php\?x=)[^ ]+' access.log | base64 -d
```
(First attempt hand-copying the Base64 string from a wrapped terminal
line produced garbage output — a good reminder that long values should
always be extracted programmatically, not read off the screen.)

**Key concept:** intrusion timeline reconstruction = pick one anchor
(attacker IP) and pivot across every log source that shares it, in
chronological order.

### 04_LiveMemory — Recovering a session token from a RAM dump with `strings`
A ~4 MB `ram_capture.dmp` file (raw memory snapshot, no file signature —
`file` just reports `data`).

```bash
strings ram_capture.dmp | grep "SESSION_TOKEN"
```
- `strings` extracts human-readable text fragments from an otherwise
  unstructured binary blob (a live process's memory holds secrets in
  plaintext while running).
- Several near-miss lines matched (`SESSION_TOKEN=` with no value —
  decoy/noise from unrelated code in memory); the real one had the flag
  as the token value.

**Key concept:** you don't always need a heavyweight tool like Volatility
for memory forensics — sometimes a plaintext secret is sitting in the
dump waiting to be `grep`'d.

---

## 2. Steganography

### 01_ChannelSurf — `zsteg` across all channel/bit-order combinations
```bash
zsteg -a image.png
```
`zsteg -a` brute-forces LSB extraction across every combination of
bit-plane, color channel, and byte order. Found reversed text in one
specific combination; `rev` un-reversed it to reveal the flag.

### 02_WhiteNoise — SNOW steganography (trailing whitespace)
A Python script (`deploy_helper.py`) had trailing whitespace after each
line — spaces and tabs encode binary (space=0, tab=1). Wrote a small
script to extract the trailing whitespace per line and decode it as
bits → the flag.

### 03_TwoFaced — PDF/ZIP polyglot file
A "PDF" was actually a **polyglot**: a valid PDF with a ZIP archive
concatenated directly after the `%%EOF` marker.

```bash
xxd file.pdf | grep -n "PK"        # confirm ZIP magic bytes are present
unzip file.pdf -d extracted/       # unzip ignores the leading PDF bytes
                                    # and finds the ZIP structure at the end
```
`unzip` warned `"extra bytes at beginning or within zipfile"` but still
successfully extracted `flag.txt` — PDF readers parse from the start of
the file, ZIP readers parse from the *end* (looking for the End of
Central Directory record), so the same file is valid as both formats
depending on which reader opens it.

**Key concept:** polyglot files exploit the fact that different file
formats define "start" and "end" differently, letting one blob of bytes
be simultaneously valid as two (or more) formats.

### 04_GridLock — QR code hidden in the Blue channel's LSB plane
A noisy PNG (`static_capture.png`) had a QR code hidden not in the
combined pixel data, but specifically in the **least significant bit of
the Blue channel** of every pixel.

```python
from PIL import Image
img = Image.open('static_capture.png').convert('RGB')
w, h = img.size
out = Image.new('1', (w, h))
px = img.load(); opx = out.load()
for y in range(h):
    for x in range(w):
        r, g, b = px[x, y]
        opx[x, y] = 255 if (b & 1) else 0
out.save('blue_lsb.png')
```
`b & 1` (bitwise AND with 1) isolates the least significant bit of the
blue value: odd → 1 (white), even → 0 (black). Rendering that bit per
pixel reconstructed a scannable QR code. `zsteg -a`'s generic text-mode
scan is useless here since the hidden payload is an *image*, not text —
this required a targeted, hint-driven extraction instead of a brute
force scan.

Read with a phone camera (faster than installing `zbarimg`, which
wasn't pre-installed).

### 05_FlipBook — One flag character per GIF frame
A GIF is really just a sequence of still frames.

```bash
convert surveillance_reel.gif frame_%02d.png   # ImageMagick: split into 40 frames
```
Each frame contained a single tiny character. Two failed approaches
before landing on a working one:
1. `tesseract` OCR — installed successfully via `sudo apt install
   tesseract-ocr`, but the images were too small/low-res for reliable
   single-character recognition (`--psm 10` mode).
2. `montage` with default smoothing filter — blurred pixel-art glyphs
   into unreadable mush.
3. **Fix:** Python + PIL with `Image.NEAREST` resampling (no
   interpolation, just nearest-pixel copy) to enlarge each frame
   crisply, arranged into a labeled grid image for manual reading.

Manually read all 40 characters in order; one character was misread
initially (extra `l`) and had to be corrected after the first flag
submission failed — a reminder that OCR/manual reading of noisy pixel
data benefits from a "submit, verify, retry" loop rather than assuming
100% accuracy up front.

### 07_Palette — Data hidden in a BMP color palette's LSBs (not the pixels)
`file mosaic.bmp` → `PC bitmap ... 96x96x8 ... 256 important colors,
bits_offset 1078`. An 8-bit BMP doesn't store per-pixel color — it
stores a **palette** (color lookup table) of 256 colors, and each pixel
is just an index into that table.

```python
with open('mosaic.bmp', 'rb') as f:
    data = f.read()
palette = data[54:1078]   # header ends at 54, pixel data starts at 1078
                           # → palette occupies exactly that gap
                           # (256 colors x 4 bytes: B, G, R, reserved)

bits = []
for i in range(0, len(palette), 4):
    b, g, r, _ = palette[i:i+4]     # BMP stores colors as B,G,R (reversed!)
    for val in (r, g, b):
        bits.append(val & 1)        # LSB of each channel value

chars = []
for i in range(0, len(bits) - 7, 8):
    byte = 0
    for bit in bits[i:i+8]:
        byte = (byte << 1) | bit
    if byte == 0:                   # null-terminated string, per the hint
        break
    chars.append(chr(byte))
print(''.join(chars))
```
Data was hidden in the LSB of each palette entry's R/G/B bytes (not the
pixel data at all), and the message was **null-terminated** like a C
string, so decoding stopped at the first `0x00` byte.

**Key concept:** applied the same "steal the least significant bit"
idea from earlier challenges, but to a completely different location in
the file format — proof that LSB steganography is a general technique,
not just a pixel-specific trick.

---

## 3. Cryptography (attempted, not solved — out of time)

### 03_TinyKey — RSA with a deliberately small private exponent `d`
```python
d = getPrime(200)          # 200-bit private exponent (way too small)
e = inverse(d, phi)        # public exponent ends up huge as a side effect
```
This is the setup for **Wiener's Attack**: if `d` is small relative to
`n`, the fraction `e/n` has a continued-fraction convergent that reveals
`d` directly.

- Installed the `owiener` Python package (`pip install owiener` — note:
  `--break-system-packages` flag wasn't supported by this pip version;
  plain `pip install <pkg>` worked instead, defaulting to a user
  install).
- `owiener.attack(e, n)` returned `None` — attack failed.
- Reimplemented the underlying continued-fraction/convergents algorithm
  by hand to double check; also found no valid `d`.

**Takeaway (unresolved):** either `d` was just outside Wiener's
theoretical bound (`d < n^0.25 / 3`), or the setup needed a stronger
variant like **Boneh–Durfee** (works for a wider range of small `d` using
lattice reduction), which was too complex to implement in the time
remaining. Good reminder that "small private exponent" doesn't always
mean "Wiener's Attack will definitely work" — the exact bound matters.

### 01_CubeRoot — RSA with `e = 3` and no padding
```python
e = 3
c = pow(m, e, n)    # textbook RSA, no padding
```
Classic **Cube Root Attack**: if the plaintext `m` is small enough that
`m^3 < n`, then `c = m^3` outright (the mod never actually reduces
anything), so `m = cube_root(c)` recovers the plaintext directly with no
key needed at all.

```python
def icbrt(n):
    # integer cube root via binary search — avoids float overflow
    lo, hi = 0, 1
    while hi**3 < n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if mid**3 < n:
            lo = mid + 1
        else:
            hi = mid
    return lo
```
- First attempt used `n ** (1/3)` (floating-point exponentiation) —
  this silently overflows/hangs for ~900-digit integers because Python
  floats can't represent numbers that large. **Lesson: never use `**
  (1/3)` on arbitrarily large integers — always use an integer-only
  method (binary search, Newton's method, or `sympy.integer_nthroot`).**
- Rewrote as an integer-only binary search — ran cleanly, but returned
  `m**3 == c → False`.
- Conclusion: `m^3` was in fact `>= n` here, so the naive cube-root
  attack doesn't apply as-is; would need a more general technique
  (e.g. Coppersmith's method for small roots, or checking `m^3 - k*n`
  for small `k`) — also out of scope for the remaining time.

**Overall crypto takeaway:** even "textbook" RSA attacks have precise
mathematical preconditions, and it's worth verifying those
preconditions (e.g. checking `d`'s bound, or whether `m^3` genuinely
stays under `n`) before assuming a well-known attack will just work.

---

## General tooling notes from today

- `xxd file | grep -n "PK"` — quick way to check for an embedded ZIP
  signature inside another file.
- `file <filename>` — always the first move on an unknown file; tells
  you the *real* format regardless of extension.
- `grep -oP 'pattern\K...'` — the `\K` lookbehind trick is much safer
  than `awk '{print $N}'` for extracting a value from log lines with
  inconsistent field counts.
- Long values (Base64 blobs, huge integers) should be **extracted
  programmatically** (`grep -oP`, or split across variables in a script)
  rather than hand-copied from a terminal that's wrapped the text —
  hand-copying wrapped text is a reliable way to introduce silent
  corruption.
- `Image.NEAREST` vs default resampling filters matters a lot when
  enlarging small pixel-art-style images for manual inspection —
  default filters (bilinear/smoothing) destroy exactly the sharp edges
  you need to read.
- Python's `**` operator with a fractional exponent (`x ** (1/3)`)
  silently breaks down for very large integers (float overflow) — use
  integer-only algorithms (binary search / Newton's method) for
  cryptographic-sized numbers.

---

## Next time / follow-ups
- [ ] Come back to `03_TinyKey` with a Boneh–Durfee implementation
      (e.g. via `sympy` + a lattice/LLL library) if time allows.
- [ ] Come back to `01_CubeRoot` — try `m^3 - k*n` for small `k`, or
      look into Coppersmith's small-roots method.
- [ ] Try `06_PingStorm` (ICMP payload steganography) and unattempted
      categories: Web Exploitation, OSINT, Binary Exploitation (PWN),
      Reverse Engineering, Mobile.
