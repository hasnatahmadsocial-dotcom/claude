# Full-text version of andrew_html.py: prints EVERY paragraph of the matching tab(s), with Andrew's marks inline.
# Usage: python3 -I scripts/andrew_html2.py <doc.html> <H1 prefix> [--marked]   (--marked = only paragraphs with marks)
import re, sys, html as H
from html.parser import HTMLParser
src=open(sys.argv[1],encoding='utf-8').read(); pref=sys.argv[2]; only='--marked' in sys.argv
css=re.search(r'<style[^>]*>(.*?)</style>',src,re.S).group(1)
rules=re.findall(r'\.(c\d+)\{([^}]*)\}',css)
HL={c for c,b in rules if re.search(r'background-color:#(?!ffffff)[0-9a-f]{6}',b,re.I)}
ST={c for c,b in rules if 'line-through' in b}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.paras=[]; s.stack=[]; s.cur=None
    def handle_starttag(s,t,a):
        a=dict(a)
        if t in('h1','h2','h3','p','li'): s.cur=[t,[]]; s.stack=[]
        if t=='span' and s.cur is not None: s.stack.append(set((a.get('class') or '').split()))
    def handle_endtag(s,t):
        if t=='span' and s.stack: s.stack.pop()
        if t in('h1','h2','h3','p','li') and s.cur: s.paras.append(s.cur); s.cur=None
    def handle_data(s,d):
        if s.cur is None: return
        cls=set().union(*s.stack) if s.stack else set()
        k='S' if cls&ST else 'H' if cls&HL else ''
        s.cur[1].append((k,d.replace('\xa0',' ')))
p=P(); p.feed(src[src.find('<body'):])
cur=None
for t,runs in p.paras:
    txt=''.join(d for k,d in runs)
    if t=='h1': cur=txt.strip()
    if not(cur and cur.startswith(pref)): continue
    out='';last=None
    for k,d in runs:
        if k!=last:
            if last: out+=']'
            if k: out+='[HL ' if k=='H' else '[STRIKE '
            last=k
        out+=d
    if last: out+=']'
    if only and '[HL' not in out and '[STRIKE' not in out: continue
    print(t,'|',out)
