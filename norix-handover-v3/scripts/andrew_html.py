# Andrew's inline comments from a Google Doc's public HTML export.
# Use when read_doc fails because the doc is too big (main Cortech doc since Nov 19).
# Usage: python3 -I scripts/andrew_html.py <doc.html> [product-filter ...]
#   get the HTML first:
#   curl -sSL -o <dir>/main.html "https://docs.google.com/document/d/<DOC_ID>/export?format=html"
# Prints, per product (H1 line), every paragraph holding highlighted ([HL ...]) or struck ([STRIKE ...]) text,
# with the whole paragraph so you see the context. Filters match the H1 text (e.g. "86484" "310 /").
import re, sys, html as H
src = open(sys.argv[1], encoding='utf-8').read()
filt = sys.argv[2:]
css = re.search(r'<style[^>]*>(.*?)</style>', src, re.S).group(1)
rules = re.findall(r'\.(c\d+)\{([^}]*)\}', css)
HL = {c for c, b in rules if re.search(r'background-color:#(?!ffffff)[0-9a-f]{6}', b, re.I)}
ST = {c for c, b in rules if 'line-through' in b}
body = src[src.find('<body'):]
cur = None; shown = set()
for m in re.finditer(r'<(h1|h2|h3|p|li)\b[^>]*>(.*?)</\1>', body, re.S):
    tag, inner = m.group(1), m.group(2)
    out = ''; marked = False
    for s in re.finditer(r'<span class="([^"]*)"[^>]*>(.*?)</span>', inner, re.S):
        cls = set(s.group(1).split()); t = H.unescape(re.sub(r'<[^>]+>', '', s.group(2))).replace('\xa0', ' ')
        if cls & ST: out += f'[STRIKE {t}]'; marked = True
        elif cls & HL: out += f'[HL {t}]'; marked = True
        else: out += t
    if tag == 'h1': cur = out.strip(); continue
    if not marked or (filt and not any(f in (cur or '') for f in filt)): continue
    if cur not in shown: print('\n#####', cur); shown.add(cur)
    print(('  - ' if tag == 'li' else '  ') + out.strip())
