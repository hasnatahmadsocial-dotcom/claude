import json,sys,html
F,TID,OUT=sys.argv[1],sys.argv[2],sys.argv[3]
d=json.load(open(F)); t=[t for t in d['content']['tabs'] if t['tabProperties']['tabId']==TID][0]
def runs(p):
    out=''
    for e in p['elements']:
        tr=e.get('textRun')
        if not tr: continue
        c=tr['content'].replace('\n','')
        if not c: continue
        s=html.escape(c,quote=False)
        ts=tr['textStyle']
        if ts.get('link'): s=f'<a href="{ts["link"]["url"]}">{s}</a>'
        if ts.get('bold'): s=f'<strong>{s}</strong>'
        out+=s
    return out.replace('</strong><strong>','')
lines=[];on=False;lvl=-1
def close_to(n):
    global lvl
    while lvl>n:
        if lvl==1: lines.append('  </ul>\n  </li>')
        else: lines.append('</ul>')
        lvl-=1
pending_li=None
items=[]
for el in t['documentTab']['body']['content']:
    p=el.get('paragraph')
    if not p: continue
    txt=''.join(e.get('textRun',{}).get('content','') for e in p['elements']).strip()
    if txt.startswith('Headings marked'): on=True; continue
    if txt.startswith('Meta Title and Description'): break
    if not on or not txt: continue
    if 'bullet' in p: items.append(('li',p['bullet'].get('nestingLevel',0),runs(p)))
    elif p['paragraphStyle'].get('namedStyleType','').startswith('HEADING'): items.append(('h2',0,html.escape(txt.replace('[H2] ',''),quote=False)))
    else: items.append(('p',0,runs(p)))
out=[];i=0
while i<len(items):
    k,l,s=items[i]
    if k!='li': out.append(f'<{k}>{s}</{k}>'); i+=1; continue
    out.append('<ul>')
    while i<len(items) and items[i][0]=='li':
        k,l,s=items[i]
        nxt=items[i+1] if i+1<len(items) else None
        if nxt and nxt[0]=='li' and nxt[1]==1:
            out.append(f'  <li>{s}'); out.append('  <ul>'); i+=1
            while i<len(items) and items[i][0]=='li' and items[i][1]==1:
                out.append(f'    <li>{items[i][2]}</li>'); i+=1
            out.append('  </ul>'); out.append('  </li>')
        else: out.append(f'  <li>{s}</li>'); i+=1
    out.append('</ul>')
h='\n'.join(out)+'\n'
open(OUT,'w').write(h); print(h); print('EMDASH' if '—' in h else 'ok')
