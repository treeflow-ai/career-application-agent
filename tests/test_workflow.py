import sys, unittest, tempfile, csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from verify_posting_snapshot import classify
from validate_application import validate_text, load_evidence
from merge_history import merge

class WorkflowTests(unittest.TestCase):
    def test_open_snapshot_signal(self):
        t=(ROOT/'samples/posting-snapshots/open.sample.html').read_text(encoding='utf-8')
        self.assertEqual(classify(t),'OPEN_SIGNAL')
    def test_closed_snapshot(self):
        t=(ROOT/'samples/posting-snapshots/closed.sample.html').read_text(encoding='utf-8')
        self.assertEqual(classify(t),'CLOSED')
    def test_unknown_snapshot(self):
        self.assertEqual(classify('<html>generic careers page</html>'),'UNKNOWN')
    def test_grounded_sample(self):
        ev=load_evidence(ROOT/'profile/evidence.example.yaml')
        text=(ROOT/'samples/application/Resume.sample.md').read_text(encoding='utf-8')
        self.assertEqual(validate_text(text,ev),[])
    def test_unknown_evidence_fails(self):
        ev=load_evidence(ROOT/'profile/evidence.example.yaml')
        errs=validate_text('Claim `[skill_example_unknown]`',ev)
        self.assertTrue(any('not claimable' in e for e in errs))
    def test_fake_evidence_fails(self):
        ev=load_evidence(ROOT/'profile/evidence.example.yaml')
        self.assertTrue(validate_text('Claim `[does_not_exist]`',ev))
    def test_python_text_io_declares_utf8(self):
        """Public scripts/tests must not depend on the host OS default text encoding."""
        import re
        offenders=[]
        for folder in ('scripts','tests'):
            for py in (ROOT/folder).glob('*.py'):
                text=py.read_text(encoding='utf-8')
                for lineno,line in enumerate(text.splitlines(),1):
                    if re.search(r'\.read_text\(\s*\)', line):
                        offenders.append(f'{py.relative_to(ROOT)}:{lineno}: bare read_text()')
                    if re.search(r'\.write_text\([^)]*\)\s*$', line) and 'encoding=' not in line:
                        offenders.append(f'{py.relative_to(ROOT)}:{lineno}: write_text() without encoding')
        self.assertEqual(offenders, [], '\n'.join(offenders))

    def test_history_blank_update_preserves_value(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d); base=d/'b.csv'; up=d/'u.csv'; out=d/'o.csv'
            base.write_text('canonical_url,application_status,notes\nhttps://careers.example.com/1,READY_TO_APPLY,keep\n', encoding='utf-8')
            up.write_text('canonical_url,application_status,notes\nhttps://careers.example.com/1,APPLIED,\n', encoding='utf-8')
            merge(base,up,out)
            with out.open(newline='', encoding='utf-8') as f:
                rows=list(csv.DictReader(f))
            self.assertEqual(rows[0]['application_status'],'APPLIED')
            self.assertEqual(rows[0]['notes'],'keep')

if __name__=='__main__': unittest.main()
