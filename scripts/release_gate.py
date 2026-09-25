#!/usr/bin/env python3
import subprocess, sys
CMDS=[
    [sys.executable,'scripts/validate_repo.py'],
    [sys.executable,'-m','unittest','discover','-s','tests','-v'],
    [sys.executable,'scripts/validate_application.py','profile/evidence.example.yaml','samples/application/Resume.sample.md','samples/application/Cover-Letter.sample.md'],
]
for cmd in CMDS:
    print('+',' '.join(cmd))
    r=subprocess.run(cmd)
    if r.returncode: raise SystemExit(r.returncode)
print('RELEASE GATE PASSED')
