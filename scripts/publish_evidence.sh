#!/usr/bin/env bash
# Re-sync the public MTG evidence package (Firstep214/mtg-commander-division). No bulk data, binaries or secrets.
set -euo pipefail
S=/workspace/mtg; R=$S/evidence_repo
[ -d "$R/.git" ] || gh repo clone Firstep214/mtg-commander-division "$R" -- -q
cd "$R"; git pull -q --rebase origin main 2>/dev/null || true
mkdir -p prompts/backup_2026-10-14 prompts/v2.3_installed decks forge scripts
# backups: keep only id/name/description
python3 - "$S" "$R" <<'PY'
import json,glob,os,sys,re
S,R=sys.argv[1:]
for f in glob.glob(f'{S}/prompts/backup_2026-10-14/*_profile.json'):
    n,i=re.match(r'(\d\d)_(.+)_profile\.json',os.path.basename(f)).groups(); d=json.load(open(f))
    json.dump({'id':i,'name':d.get('name'),'description':d.get('description')},open(f'{R}/prompts/backup_2026-10-14/{n}_{i}.json','w'),indent=1,ensure_ascii=False)
PY
cp $S/prompts/v2.3_installed/*.md prompts/v2.3_installed/
for f in READBACK.md INSTALL_RECEIPT.md; do [ -f $S/prompts/$f ] && cp $S/prompts/$f prompts/; done
cp $S/prompts/MTG-*.md prompts/ 2>/dev/null || true
cp $S/EVIDENCE_README.md README.md; cp $S/STATUS_CH001.md $S/AUDIT.md $S/CURRICULUM.md .
cp $S/decks/*.md $S/decks/*.txt decks/
cp $S/forge/sim_test.log $S/forge/sim_v1_final.log forge/
cp $S/check.py $S/audit_fresh.py $S/build_db.py scripts/; cp $S/publish_evidence.sh scripts/
for d in sources ledgers audits learning; do [ -d $S/$d ] && { mkdir -p $d; rsync -a --delete --exclude='*.jsonl*' --exclude='*.gz' --exclude='*.jar' --exclude='*.bz2' --exclude='oracle*.json' --exclude='default*.json' $S/$d/ $d/; }; done
# scrub: local box paths -> repo-relative note is fine; block secrets
if grep -rIEn '(gh[pousr]_[A-Za-z0-9]{20,}|github_pat_|xox[abpr]-|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|BEGIN [A-Z ]*PRIVATE KEY|"serverId"|"harness")' --exclude-dir=.git --exclude=publish_evidence.sh . ; then echo "SECRET/SENSITIVE PATTERN FOUND - aborting"; exit 1; fi
find . -type f -size +20M -not -path './.git/*' | grep . && { echo "large file - aborting"; exit 1; } || true
find . -type f -not -path './.git/*' -not -name SHA256SUMS.txt | sort | xargs sha256sum > SHA256SUMS.txt
git add -A; git diff --cached --quiet && { echo "no changes"; exit 0; }
git commit -qm "evidence sync $(date -Iseconds)"; git push -q -u origin HEAD
