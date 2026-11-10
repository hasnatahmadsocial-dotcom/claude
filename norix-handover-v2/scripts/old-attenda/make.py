import sys,json
exec(open('/tmp/claude-0/-home-claude/cfa6e804-8b87-569e-b391-80a01c05d6c7/scratchpad/nx/at_common.py').read())
exec(open('/tmp/claude-0/-home-claude/cfa6e804-8b87-569e-b391-80a01c05d6c7/scratchpad/at2/products.py').read())
def content(d):
    URL=A+d['handle']
    sp=', '.join(f'[{n}]({u})' for n,u in d['specs'])
    p=[('h1',d['short']),
       ('p',f"**Product URL:** [{URL}]({URL})"),
       ('p',f"**Manufacturer page:** [{d['src']}]({d['src']})"),
       ('p',f"**Spec sheet{'s' if len(d['specs'])>1 else ''}:** {sp}"),
       ('h2','Recommended H1 and Subtitle'),
       ('p',f"**H1:** {d['h1']}"),('p',f"**Current H1:** {d['cur_h1']}"),
       ('p',f"**Subtitle:** {d['sub']}"),('p',f"**Current subtitle:** {d['cur_sub']}"),
       ('h2','Revised Product Description'),
       ('p','Headings marked [H2] should be set as H2 on the page.')]
    p+= [('p',x) for x in d['intro']]
    p+= [('b1',x) for x in d['bullets']]
    if d['models']:
        p.append(('p','**Available Models and Options**')); p+=[('b1',x) for x in d['models']]
    p.append(('p','**Installation and Options**')); p+=[('b1',x) for x in d['install']]
    p+= at_apps(d['apps'])+AT_SERIES+meta(d['mt'],d['md'])
    p.append(('h2','Notes and Questions')); p+=[('n1',x) for x in d['notes']]
    return p
if __name__=='__main__':
    i=int(sys.argv[1]); tab=sys.argv[2]
    r=build(tab,content(P[i]))
    s=json.dumps(r,ensure_ascii=False)
    assert '—' not in s, 'emdash'
    json.dump(r,open(f'/tmp/claude-0/-home-claude/cfa6e804-8b87-569e-b391-80a01c05d6c7/scratchpad/at2/req_{i}.json','w'))
    print(i,len(r),len(s))
