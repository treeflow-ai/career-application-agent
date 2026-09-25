#!/usr/bin/env python3
"""Offline heuristic for saved public posting HTML.
Not a replacement for live official-source verification; useful for fixtures/CI."""
from pathlib import Path
import re, sys, json
CLOSED=[r'no longer accepting', r'job (?:is )?closed', r'position (?:has been )?filled', r'job not found', r'no longer available']
OPEN=[r'apply now', r'apply for this job', r'submit application', r'apply here']

def classify(text):
    s=re.sub(r'\s+',' ',text.lower())
    if any(re.search(p,s) for p in CLOSED): return 'CLOSED'
    if any(re.search(p,s) for p in OPEN): return 'OPEN_SIGNAL'
    return 'UNKNOWN'

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('usage: verify_posting_snapshot.py FILE')
    p=Path(sys.argv[1]); print(json.dumps({'file':str(p),'snapshot_signal':classify(p.read_text(encoding='utf-8', errors='ignore'))}))
