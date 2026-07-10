#!/bin/bash
# rename_to_3digits.sh
#
# Renames all files in the current directory from "NN_..." or "N_..." format
# to zero-padded 3-digit "0NN_..." format, using `git mv` to preserve history.
#
# Usage:
#   1. cd into the folder (e.g., 05_essential_8) inside your local git repo clone
#   2. bash rename_to_3digits.sh
#   3. Review the changes with `git status`
#   4. git commit -m "Rename files to 3-digit numbering for correct sort order"
#   5. git push

set -e

echo "Scanning current directory: $(pwd)"
echo "----------------------------------------"

for f in *; do
  # Skip if not a regular file
  [ -f "$f" ] || continue

  # Match a leading number (1-3 digits) followed by an underscore
  if [[ "$f" =~ ^([0-9]{1,3})_(.*)$ ]]; then
    num="${BASH_REMATCH[1]}"
    rest="${BASH_REMATCH[2]}"

    # Zero-pad to 3 digits
    padded=$(printf "%03d" "$((10#$num))")

    newname="${padded}_${rest}"

    if [ "$f" != "$newname" ]; then
      echo "Renaming: $f  ->  $newname"
      git mv "$f" "$newname"
    else
      echo "Already correct: $f"
    fi
  else
    echo "Skipping (no leading number pattern): $f"
  fi
done

echo "----------------------------------------"
echo "Done. Review with 'git status', then commit and push."