# Print every TABLE in a Google Doc JSON (cmp2.py skips tables; Andrew put SKUs/URLs in one).
# Usage: python3 -I scripts/doc_tables.py <docjson>
import json,sys
d=json.load(open(sys.argv[1]))['content']
def txt(cell):
    s=''
    for el in cell['content']:
        p=el.get('paragraph')
        if p:
            for r in p['elements']:
                tr=r.get('textRun')
                if tr: s+=tr['content']
    return s.replace('\n',' ').replace('\u000b',' / ').strip()
for t in d['tabs']:
    for el in t['documentTab']['body']['content']:
        if 'table' in el:
            print(t['tabProperties']['title'],'@',el['startIndex'])
            for row in el['table']['tableRows']: print('   ',[txt(c) for c in row['tableCells']])
