#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
'README.md','SKILL.md','AGENT-ARCHITECTURE.md','docs/architecture.svg','docs/ENHANCED-RESUME-SKILL.md',
'skills/job-discovery.md','skills/job-verification.md','skills/job-evaluator.md','skills/evidence-mapper.md','skills/resume-tailor.md',
'profile/candidate.example.yaml','profile/evidence.example.yaml','profile/preferences.example.yaml','state/history.example.csv',
'scripts/verify_posting_snapshot.py','scripts/validate_application.py','tests/test_workflow.py'
]
PRIVATE={'profile/candidate.yaml','profile/preferences.yaml','profile/evidence-bank.yaml','profile/master-resume.md','profile/linkedin-profile.md','state/history.csv','state/current-run.yaml'}
EMAIL=re.compile(r'\b[A-Z0-9._%+-]+@([A-Z0-9.-]+\.[A-Z]{2,})\b',re.I)
PHONE=re.compile(r'(?<!\d)(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}(?!\d)')
ALLOWED_EMAIL_DOMAINS={'example.com','example.org','example.net'}
ALLOWED_SAMPLE_PHONE={'+1-555-010-2000'}

def main():
    errs=[]
    for r in REQUIRED:
        if not (ROOT/r).exists(): errs.append('missing required file: '+r)
    for r in PRIVATE:
        if (ROOT/r).exists(): errs.append('local personal-data file should not be committed: '+r)
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.git' in p.parts or p.suffix.lower() in {'.png','.jpg','.jpeg','.zip','.pyc'}: continue
        try: text=p.read_text(encoding='utf-8')
        except UnicodeDecodeError: continue
        for email in EMAIL.findall(text):
            if email.lower() not in ALLOWED_EMAIL_DOMAINS: errs.append(f'non-example email domain in {p.relative_to(ROOT)}: {email}')
        for phone in PHONE.findall(text):
            if phone not in ALLOWED_SAMPLE_PHONE: errs.append(f'phone-like PII in {p.relative_to(ROOT)}: {phone}')
    for y in ROOT.rglob('*.yaml'):
        try: yaml.safe_load(y.read_text(encoding='utf-8'))
        except Exception as e: errs.append(f'invalid YAML {y.relative_to(ROOT)}: {e}')
    if errs:
        print('\n'.join(errs)); return 1
    print('repo validation passed'); return 0
if __name__=='__main__': raise SystemExit(main())
