# usage: python3 -I ads/docnotes.py "<tab title prefix>" [all]
import json,sys
d=json.load(open('norix-nov24/doc/norix_orig_nov24g.json'))
def walk(x):
    if isinstance(x,dict):
        if 'tabProperties' in x: yield x
        for v in x.values(): yield from walk(v)
    elif isinstance(x,list):
        for v in x: yield from walk(v)
allp=len(sys.argv)>2
for t in walk(d):
    if t['tabProperties']['title'].startswith(sys.argv[1]):
        on=allp
        for el in t['documentTab']['body']['content']:
            if 'paragraph' in el:
                s=''
                for r in el['paragraph']['elements']:
                    tr=r.get('textRun')
                    if not tr: continue
                    st=tr.get('textStyle',{}); c=tr['content']
                    if st.get('strikethrough'): c='[STRIKE '+c.strip()+']'
                    elif st.get('backgroundColor'): c='[HL '+c.strip()+']'
                    s+=c
                if 'Notes and Q' in s or 'Available Models' in s: on=True
                if on and s.strip(): print(s.rstrip())
            elif 'table' in el and on: print('[TABLE]')
        break
