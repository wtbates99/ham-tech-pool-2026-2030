import re, json

with open('pool.txt', encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f]

header_re = re.compile(r'^(T\d[A-Z]\d\d)\s*\(([A-D])\)(?:\s*\[(.*?)\])?\s*$')

questions = []
cur = None
mode = None  # 'q' or 'a'
subelement = None
group_desc = {}

for i, line in enumerate(lines):
    stripped = line.strip()
    m = header_re.match(stripped)
    if m:
        if cur:
            questions.append(cur)
        code, ans, ref = m.groups()
        cur = {'code': code, 'answer': ans, 'ref': ref or '', 'question': '', 'options': {'A':'','B':'','C':'','D':''}}
        mode = 'q'
        continue
    if stripped == '~~':
        continue
    if cur is None:
        continue
    optm = re.match(r'^([A-D])\.\s+(.*)$', stripped)
    if optm:
        letter, text = optm.groups()
        cur['options'][letter] = text
        mode = 'a'
        continue
    if stripped == '' or 'End of question pool' in stripped:
        continue
    if mode == 'q' and not stripped.startswith('SUBELEMENT'):
        cur['question'] = (cur['question'] + ' ' + stripped).strip()
    elif mode == 'a':
        # continuation of last option
        last = None
        for l in ['A','B','C','D']:
            if cur['options'][l]:
                last = l
        if last:
            cur['options'][last] += ' ' + stripped

if cur:
    questions.append(cur)

print(len(questions))
# sanity check a few
for q in questions[:2] + questions[-2:]:
    print(json.dumps(q, indent=2))

with open('questions.json', 'w') as f:
    json.dump(questions, f, indent=1)
