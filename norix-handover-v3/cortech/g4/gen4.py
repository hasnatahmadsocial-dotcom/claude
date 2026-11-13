import sys,html,re,json
exec(open('mc4.py').read().split("if __name__")[0])
def md2html(md):
    out='';i=0
    tok=re.compile(r'\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)')
    for m in tok.finditer(md):
        out+=html.escape(md[i:m.start()],quote=False)
        if m.group(1) is not None: out+='<strong>'+html.escape(m.group(1),quote=False)+'</strong>'
        else: out+=f'<a href="{m.group(3)}">'+html.escape(m.group(2),quote=False)+'</a>'
        i=m.end()
    return out+html.escape(md[i:],quote=False)
def gen(d):
    c=content(d); items=[]; on=False
    for k,md in c:
        t=parse(md)[0]
        if t.startswith('Headings marked'): on=True; continue
        if t.startswith('Meta Title and Description'): break
        if not on: continue
        if k=='b1': items.append(('li',md2html(md)))
        elif k in('h2','h3'): items.append(('h2',html.escape(t.replace('[H2] ',''),quote=False)))
        else: items.append(('p',md2html(md)))
    out=[];i=0
    while i<len(items):
        k,s=items[i]
        if k!='li': out.append(f'<{k}>{s}</{k}>'); i+=1; continue
        out.append('<ul>')
        while i<len(items) and items[i][0]=='li': out.append(f'  <li>{items[i][1]}</li>'); i+=1
        out.append('</ul>')
    return '\n'.join(out)+'\n'
if __name__=='__main__':
    key=sys.argv[1]; d=[x for x in P if x['tab'].startswith(key)][0]
    h=gen(d); open(sys.argv[2],'w').write(h)
    print(h)
    print('CHECK em:',h.count('—'),'en:',h.count('–'),'[:',h.count('['),'dblspace:',len(re.findall(r'\S  +\S',h)),'emptyli:',h.count('<li></li>'),'degrees:',h.count('degrees'))
    print('LINKS',re.findall(r'href="([^"]+)"',h)); print('H2',re.findall(r'<h2>([^<]+)',h))
    print('H1',d['h1']); print('SUB',d['sub']); print('MT',len(d['mt']),d['mt']); print('MD',len(d['md']),d['md'])
