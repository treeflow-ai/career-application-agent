#!/usr/bin/env python3
import csv, sys
from pathlib import Path
KEY='canonical_url'

def read(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return rows, reader.fieldnames

def merge(base_path, update_path, out_path):
    with open(base_path,newline='',encoding='utf-8') as f:
        r=csv.DictReader(f); base=list(r); fields=r.fieldnames
    with open(update_path,newline='',encoding='utf-8') as f:
        r=csv.DictReader(f); updates=list(r); ufields=r.fieldnames
    if KEY not in (ufields or []): raise ValueError('updates must include canonical_url')
    unknown=set(ufields)-set(fields)
    if unknown: raise ValueError(f'unknown columns: {sorted(unknown)}')
    ix={row[KEY]:row for row in base}
    for u in updates:
        key=u[KEY]
        if key in ix:
            for k,v in u.items():
                if v!='': ix[key][k]=v
        else:
            row={k:'' for k in fields}; row.update(u); base.append(row); ix[key]=row
    with open(out_path,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(base)

if __name__=='__main__':
    if len(sys.argv)!=4: raise SystemExit('usage: merge_history.py BASE UPDATES OUT')
    merge(*sys.argv[1:])
