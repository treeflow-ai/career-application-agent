#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

ALLOWED_STATUSES={'VERIFIED','USER_CONFIRMED'}
REF_RE=re.compile(r'\[([A-Za-z0-9_:-]+)\](?!\()')

def load_evidence(path):
    data=yaml.safe_load(Path(path).read_text(encoding='utf-8'))
    return {e['id']:e for e in data.get('evidence',[])}

def validate_text(text, evidence):
    errs=[]
    for ref in REF_RE.findall(text):
        if ref not in evidence: errs.append(f'unknown evidence id: {ref}')
        elif evidence[ref].get('status') not in ALLOWED_STATUSES: errs.append(f'evidence not claimable: {ref}')
    if 'candidate@example.com' in text and 'mailto:candidate@example.com' not in text and 'Email' in text:
        errs.append('email appears without explicit mailto hyperlink')
    for bad in ['TODO_PRIVATE','REAL_NAME_HERE','PRIVATE_DATA_HERE']:
        if bad in text: errs.append(f'placeholder/private marker present: {bad}')
    return errs

if __name__=='__main__':
    if len(sys.argv)<3: raise SystemExit('usage: validate_application.py EVIDENCE_YAML FILE...')
    ev=load_evidence(sys.argv[1]); errs=[]
    for f in sys.argv[2:]:
        errs += [f'{f}: {e}' for e in validate_text(Path(f).read_text(encoding='utf-8'),ev)]
    if errs:
        print('\n'.join(errs)); raise SystemExit(1)
    print('application validation passed')
