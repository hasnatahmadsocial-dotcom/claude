# Evac+Chair / REX product tabs (keyword workflow, Nov 2026). content(d) builds the tab; run `python3 -I ep.py` for checks.
import json,re
A='https://www.anchortex.com/products/'
C='https://www.anchortex.com/collections/'
EVAC_COLL=f"[Evacuation Chairs and Stretchers]({C}work-place-safety-evacuation-chairs-and-stretchers)"
PRISON_HW=f"[Prison and Detention Hardware and Equipment]({C}prison-and-detention-hardware-and-equipment)"
BH_RESTR=f"[Patient Safety Restraints]({C}bh-patient-safety-restraints)"
REX_SERIES=[('h3','[H2] About Rapid Extraction REX Stretchers'),
 ('p','REX stretchers fold in three for compact storage and roll on airless all-terrain wheels, so one responder can move a patient over stairs, rough ground, and long distances.'),
 ('p','The REX line includes:'),
 ('b1','**REX ONE:** Multi-purpose extraction stretcher that converts to a backboard, mobile stretcher, or treatment cot'),
 ('b1','**REX DCS:** The REX ONE with a Descent Control System hand brake for stairs and steep ground'),
 ('b1','**REX DCS/CF:** The REX DCS for correctional facilities, with Humane Restraint cuffs and full body restraint straps')]
EVAC_BRAND=f"[Evac+Chair]({C}evac-chair)"
EVAC_SERIES=[('h3','[H2] About Evac+Chair Evacuation Chairs'),
 ('p','Evac+Chair makes stair evacuation chairs, powered stair chairs, evacuation sleds, and accessories for moving people with limited mobility on stairs, in an emergency or every day.'),
 ('p','The Evac+Chair line includes:'),
 ('b1','**Emergency evacuation chairs:** The 300H, 400H, 600H, and 750H stair evacuation chairs for controlled travel down the stairs'),
 ('b1','**Powered stair climbing chairs:** The battery powered Power 800 and Power 900 for going up and down the stairs'),
 ('b1','**Stair transport seat:** The IBEX 700H Tran-Seat for two-person transport up and down the stairs'),
 ('b1','**Evacuation sleds and mats:** The Evac+Sled, Ulti-Mat, and Evac+Sheet rescue sheet'),
 ('b1','**Accessories:** Comfy Seat, transfer seat, storage cabinets, anti-theft alarms, and the iEvac smoke and fire escape hood')]
EVAC_ABOUT=('p',f"Evac+Chair has made stairway evacuation chairs since 1982, and its chairs were designed in the United States. Explore the full line of {EVAC_BRAND} evacuation chairs at Anchortex.")
REX_ABOUT=('p','Rapid Extraction (REX EMS, LLC) of Glendora, California, designs and builds REX stretchers in the U.S.A., and REX stretchers won an EMS World Innovation Award.')
P=[]
def add(**k): P.append(k)
exec(open('pe1.py').read())
exec(open('pe2.py').read())
exec(open('pe3.py').read())
exec(open('pe4.py').read())
exec(open('pe5.py').read())
exec(open('pe6.py').read())
exec(open('pe7.py').read())
exec(open('pe8.py').read())
exec(open('pe9.py').read())
exec(open('pe10.py').read())
exec(open('pe11.py').read())
exec(open('pe12.py').read())
exec(open('pe13.py').read())
exec(open('pe14.py').read())
def content(d):
    URL=A+d['handle']
    sp=', '.join(f'[{n}]({u})' for n,u in d['specs'])
    lab='Spec sheets' if len(d['specs'])>1 else 'Spec sheet'
    src=', '.join(f'[{u}]({u})' for u in d['src'])
    p=[('h1',d['short']),('p',f"**Product URL:** [{URL}]({URL})"),('p',f"**Manufacturer page:** {src}"),('p',f"**{lab}:** {sp}"),
       ('p','**Keywords (Ricky\'s sheet):** '+d['kw']),
       ('h2','Recommended H1 and Subtitle'),('p',f"**H1:** {d['h1']}"),('p',f"**Current H1:** {d['cur_h1']}"),
       ('p',f"**Subtitle:** {d['sub']}"),('p',f"**Current subtitle:** {d['cur_sub']}"),
       ('h2','Revised Product Description'),('p','Headings marked [H2] should be set as H2 on the page.')]
    p+=[('p',x) for x in d['intro']]+[('b1',x) for x in d['bullets']]
    p.append(('p','**Available Models and Options**')); p+=[('b1',x) for x in d['models']]
    if d.get('install'): p.append(('p','**Installation and Options**')); p+=[('b1',x) for x in d['install']]
    p+=d['apps']+d.get('faq',[])+d['series']+[('h3','[H2] About Rapid Extraction' if d['brand']=='REX' else '[H2] About Evac+Chair'),d['about']]
    p+=[('h2','Meta Title and Description'),('p',f"**Meta title ({len(d['mt'])} characters):** {d['mt']}"),('p',f"**Current meta title:** {d['cur_mt']}"),
        ('p',f"**Meta description ({len(d['md'])} characters):** {d['md']}"),('p',f"**Current meta description ({len(d['cur_md'])} characters):** {d['cur_md']}")]
    p.append(('h2','Notes and Questions')); p+=[('n1',x) for x in d['notes']]
    return p
if __name__=='__main__':
    for d in P:
        c=content(d); s=json.dumps(c,ensure_ascii=False); e=[]
        if '—' in s: e.append('EMDASH')
        if not(50<=len(d['mt'])<=65): e.append('MT %d'%len(d['mt']))
        if not(140<=len(d['md'])<=195): e.append('MD %d'%len(d['md']))   # Ricky's team rule (Nov 23): <=195
        if not d['md'].startswith(d['h1'].split(' ')[0]) or 'Anchortex' not in d['md'].split('. ')[-1]: e.append('MD-RICKY (brand first + Anchortex action sentence)')
        if 'Model' in d['h1']: e.append('H1 has "Model" (Ricky/Andrew: only if it adds clarity)')
        if len(d['tab'])>50: e.append('TAB %d'%len(d['tab']))
        if d['h1'].count('–')!=1: e.append('H1 endash')
        for k,t in c:
            if '  ' in t: e.append('DBLSPACE:'+t[:40])
            if '–' in t and not (t.startswith('**H1:**') or re.match(r'\*\*[A-Z0-9][^*]* – [^*]*:\*\*',t)): e.append('ENDASH:'+t[:50])
            if re.search(r'\d"',t) and not t.startswith('**Current') and k!='n1': e.append('STRAIGHTQ:'+t[:50])
        body=' '.join(t for k,t in c if not t.startswith(('**Keywords','**Current','**Meta','**Product URL','**Manufacturer','**Spec'))).lower()
        print(d['tab'],'| mt',len(d['mt']),'md',len(d['md']),'| paras',len(c),e or 'ok')
        print('  keywords:',{k:body.count(k) for k in d['kwlist']})
