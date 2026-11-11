#!/bin/bash
# Full live review of every published product listed in scripts/registry.json.
# Run from the norix-handover-v2 folder:  bash scripts/check_all.sh
python3 -I - <<'P'
import json,subprocess
for r in json.load(open('scripts/registry.json')):
    out=subprocess.run(['python3','-I','scripts/review.py',r['handle'],r['html'],r['subtitle'],r['seo_title'],r['seo_desc'],r['baseline']],capture_output=True,text=True).stdout
    print(out.strip().splitlines()[0]); print('\n'.join(l for l in out.splitlines() if l.startswith(('ISSUES','  -'))))
P
python3 -I scripts/sweep.py $(python3 -I -c "import json;print(' '.join(r['handle'] for r in json.load(open('scripts/registry.json'))))")
