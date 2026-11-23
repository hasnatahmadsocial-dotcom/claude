# Collection description HTML from collection_draft.py body (= doc tab text), plus check against the doc snapshot.
import re,html,json,sys
exec(open('collection_draft.py').read())
def inl(s):
    s=html.escape(s,quote=False)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    return re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
out=[];i=0
while i<len(body):
    k,t=body[i]
    if k=='b':
        out.append('<ul>')
        while i<len(body) and body[i][0]=='b': out.append(f'  <li>{inl(body[i][1])}</li>'); i+=1
        out.append('</ul>'); continue
    out.append(f'<{k}>{inl(t)}</{k}>'); i+=1
h='\n'.join(out)+'\n'
open('../shopify-html/EVAC-COLLECTION.html','w').write(h)
# compare with doc tab paragraphs (strip markup)
d=json.load(open(sys.argv[1]))['content']
t=[t for t in d['tabs'] if t['tabProperties']['title'].startswith('Collection')][0]
paras=[''.join(r.get('textRun',{}).get('content','') for r in el['paragraph']['elements']).strip() for el in t['documentTab']['body']['content'] if 'paragraph' in el]
plain=lambda s: re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',s).replace('**','')
miss=[plain(x) for k,x in body if plain(x) not in paras]
print('paragraphs',len(body),'not found in doc:',miss)
print('EMDASH' if '—' in h else 'no em dash','| double space' if '  ' in h else '| no double space')
links=re.findall(r'href="([^"]+)"',h); print('links',links)
