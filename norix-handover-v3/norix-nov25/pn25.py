# Norix batch 11/25/2026: 13 Hondo Nuevo products (sheet "ANC" rows 255-293). Sources: live pages (live/, page/, cur.json, live_summary.txt),
# norix.com Hondo Nuevo pages (site/hn-*.html, site/hondo-series.html), 40 Norix spec sheets (spec/HN*.txt, all printed 9/24), Hondo Nuevo brochure 2023
# (spec/Hondo_Nuevo_Brochure_2023.txt), price list April 2026 pp. 24-27 (data/pricer.txt), design guide (seat colors), seating guide Sep 2026.
# Findings: only molded plinth / rocker / stool sheets say "Ligature resistant design with no internal openings" (steel + wood legs do not);
# seat colors Twilight, Sage, Clay, Sienna, Dove, Raven (6; live pages say "5"); price list HN800 plinth + rocker 110 lbs vs spec 103 (spec used);
# footstool ballast 30 lbs (others 50); stool cannot be ballasted, no options; ottoman + footstool: spec lists ganging kit, price list has no ganging.
# Norix rules: MT ends " at Anchortex"; MD "Norix <product> is ... Shop it at Anchortex." (<=195); "**Assembly:** None required" bullet;
# Andrew Nov 24 (Forte): Prison link deleted, Transitional Housing not linked -> BH link only.
import json as _j
LINKS=f"Explore Anchortex's [Behavioral Healthcare Anti-Ligature Furniture]({BH}) collection for more institutional furniture."
PH=_j.load(open('norix_photos.json'))
HONDO_SERIES=[
('h3','[H2] About Norix Hondo Nuevo Seating'),
('p','Norix Hondo Nuevo is a modular soft seating series for facilities where furniture has to be robust, including behavioral healthcare and correctional facilities, healthcare, education, and hospitality interiors. Every piece has a one-piece, rotationally molded vinyl skin over a foam core, and the pieces can be mixed and ganged to build flexible seating arrangements.'),
('p','The Hondo Nuevo series includes:'),
('b1','**Chairs:** 30” arm chair, high back chair, and 30” and 24” armless chairs'),
('b1','**Sectional Seats:** Left arm and right arm sectional seats, and a seat wedge with a back'),
('b1','**Benches:** Bench, bench wedge, and cube'),
('b1','**Ottomans and Stools:** Round ottoman, footstool, and stool'),
('b1','**Bases:** Molded plinth base, molded wood-grain legs, or steel legs, plus a rocker base for the arm chair and high back chair'),
]
HONDO_NEW='New series section: the 13 Hondo Nuevo products in this batch share an "About Norix Hondo Nuevo Seating" section based on the Norix Hondo Nuevo brochure, price list, and website. It has no links to individual products. Please review it here; any changes will be applied to all 13 Hondo Nuevo tabs.'
HONDO_REF='Series section: same "About Norix Hondo Nuevo Seating" section as the HN800 Arm Chair tab.'
CONSTR='**Construction:** One-piece, rotationally molded 0.25” flexible PVC skin with a softer feel, filled with polyurethane foam and fixed to a ⅝” oriented strand board base plate'
TRU='**TruColor Polymer:** Fully compounded color for consistent color and durability'
DRIP='**Fluid Resistant:** Smooth surface is impervious to fluids and resists punctures and peeling; a fabricated drip edge lets fluids run to the floor instead of into the base'
CHEM='**Chemical Resistance:** Resists blood, vinegar, urine, feces, salt solution, and chlorine solution'
TAMP='**Tamper Resistant:** The seat is fastened to the base with tamper-resistant Torx hardware'
SEATC='**Seat Colors:** Twilight, Sage, Clay, Sienna, Dove, or Raven'
LOAD='**Static Load Testing:** Tested to 750 lbs'
PERF='**Performance Standards:** Dynamic drop tested to twice the ANSI/BIFMA X5.4 impact force (250 lbs from 18”); tested to 184 lbs puncture resistance (ASTM D4833); meets ANSI/BIFMA X5.4'
FLAM='**Flammability Standards:** California Technical Bulletins 133 and 117; UL 1056; ASTM E1537; NFPA 261'
CLEAN='**Cleaning:** Purple Power cleaner for routine cleaning, World’s Best Sensitive Surface Graffiti Remover for tougher stains, and a thin layer of Black Magic Protectant every two months'
DYE='**Dye Transfer:** Indigo denim dyes and some inks can stain lighter colors permanently; clean stains as soon as possible'
BASE_DESC={'850':'Molded Plinth Base','851':'Rocker Base','860':'Molded Wood-Grain Legs','855':'Steel Legs'}
BASE_COL={'850':'Sienna, Dove, or Raven','851':'Sienna, Dove, or Raven','860':'Maple or Walnut','855':'Metallic Silver'}
BASE_MAT={'850':'rotationally molded LLDPE plinth base','851':'rotationally molded LLDPE rocker base','860':'rotationally molded LLDPE legs with a wood-grain texture','855':'welded 1.5” square steel tube base'}
NAME_COL={'twilight':'Twilight','tw':'Twilight','sage':'Sage','sa':'Sage','sg':'Sage','clay':'Clay','cl':'Clay','sienna':'Sienna','sn':'Sienna','dove':'Dove','dv':'Dove','raven':'Raven','rv':'Raven'}
BASE_CODE={'mldsn':'plinth base, Sienna','mlddv':'plinth base, Dove','mldrv':'plinth base, Raven','mldmp':'wood-grain legs, Maple','mldwn':'wood-grain legs, Walnut','st':'steel legs','rocker':'rocker base'}
OLDC=['graphite','lagoon','pine_cone','wild_berry']

def pick(page,bases):
    """one Norix photo per base type, each in a different current seat color (stool: 3 colors)"""
    out=[];used=set()
    want={'850':('mldsn','mlddv','mldrv'),'860':('mldmp','mldwn'),'855':('st',),'851':('rocker',)}
    files=[f.split('/')[-1].replace('.jpg','') for f in PH[page]]
    def cols(n): return [NAME_COL[p] for p in n.split('_') if p in NAME_COL]
    if page=='stool':
        for n in files:
            c=cols(n)
            if c and c[0] not in used and len(out)<3: used.add(c[0]); out.append(f'{n}.jpg ({c[0]})')
        return out
    for b in bases:
        for n in files:
            c=cols(n); code=[p for p in n.split('_') if p in BASE_CODE]
            if c and code and code[0] in want[b] and c[0] not in used:
                used.add(c[0]); out.append(f'{n}.jpg ({c[0]} seat, {BASE_CODE[code[0]]})'); break
    return out

def C(h): return CUR[h]

def photo_note(h,page,bases,extra=''):
    p=LIVE[h]['images']; n=len(p)
    old=[i['src'].split('/')[-1].split('?')[0] for i in p if any(c in i['src'].lower() for c in OLDC)]
    wrong=[i for i in p if i['alt'] and 'HN825' in i['alt'] and 'HN825' not in h.upper()]
    s=f'Images: the {n} current images are kept.'
    if old: s+=f' {len(old)} of them {"shows" if len(old)==1 else "show"} seat colors Norix no longer offers (Graphite, Lagoon, Pine Cone, or Wild Berry): {", ".join(old)}.'
    if wrong: s+=f' The base close-ups ({", ".join(i["src"].split("/")[-1].split("?")[0] for i in wrong)}) have the alt text "Norix HN825-series Hondo Nuevo Seat Wedge," which is the wrong product.'
    pk=pick(page,bases)
    if pk: s+=' Norix has photos in the current colors (600×600). Would you like me to add '+('these' if len(pk)>1 else 'this')+': '+'; '.join(pk)+'?'
    if old: s+=' And should the old-color photos be removed?'
    return s+extra

def price_note(h,lst):
    v=LIVE[h]['variants']; ok=[]
    for x in v:
        t=x['title']; b='851' if 'Rocker' in t else '860' if 'Wood' in t else '855' if 'Steel' in t else '850'
        L=lst[b]; ok.append(abs(float(x['price'])-0.8*L)<0.01 and abs(float(x['compare_at_price'])-L)<0.01)
    s=' and '.join(f"${float(x['price']):,.2f}" for x in v)
    who=f'all {len(v)} variants are' if len(v)>1 else 'the price is'
    return ('Prices checked: ' if all(ok) else 'PRICE CHECK FAILED: ')+f'{who} 80% of the Norix list price ({", ".join("$"+format(lst[k],",") for k in lst)} list), with compare-at = list. No change.'

def hondo(n,h,page,code,name,short,h1,sub,intro,size,seat,wts,lst,opts,apps_p,mt,md,first=False,ballast=50,lig_all=False,extra_notes=(),extra_bul=(),models_extra=()):
    bases=list(wts)
    has={b:True for b in bases}
    lig=('**Ligature Resistant:** Ligature-resistant design with no internal openings' if lig_all else
         '**Ligature Resistant:** The molded plinth base'+(' and rocker base models have' if '851' in has else ' model has')+' a ligature-resistant design with no internal openings')
    wtxt='; '.join(f'{BASE_DESC[b].lower()} {wts[b]} lbs' for b in bases)
    bul=[CONSTR,TRU,DRIP,CHEM,TAMP,lig]+list(extra_bul)+[x for x in (size,seat) if x]+([f'**Weight:** {wts[bases[0]]} lbs'] if len(bases)==1 else [f'**Weight:** {wtxt[0].upper()+wtxt[1:]}'])
    bul+=[SEATC]
    if len(bases)==1: bul.append('**Base Color:** Molded plinth base in Sienna, Dove, or Raven') if page!='stool' else None
    if len(bases)>1:
        bc='; '.join(f'{BASE_DESC[b].lower()} in {BASE_COL[b]}' for b in bases)
        bul.append('**Base Colors:** '+bc[0].upper()+bc[1:])
    bul+=[LOAD,PERF,FLAM,GG,CLEAN,DYE,W10,IND,USA]
    models=[f'**{code}.HN{b} – {BASE_DESC[b]}:** {BASE_MAT[b][0].upper()+BASE_MAT[b][1:]}, {BASE_COL[b]+", " if page!="stool" else ""}{wts[b]} lbs' for b in bases]+list(models_extra)
    if opts: models.append(opts)
    inst=['**Assembly:** None required']
    if opts and 'anging' in opts: inst.append('**Ganging and Bolt-Down:** Attach ganging and bolt-down brackets when required; see Norix instructions. Bolt-down kits must be specified when ordering (factory assembled)')
    elif opts and 'olt-down' in opts: inst.append('**Bolt-Down:** Bolt-down kits must be specified when ordering (factory assembled)')
    if ballast: inst.append(f'**Ballast:** The molded plinth base{" and rocker base" if "851" in has else ""} can be factory ballasted with {ballast} lbs of dry sand or gravel; ballasting must be specified when ordering and cannot be added on site')
    apps=[('h3','[H2] Applications'),('p',apps_p),('p','Typical applications include:'),
      ('b1','Dayrooms, lounges, and activity rooms in behavioral healthcare facilities and psychiatric hospitals'),
      ('b1','Lobbies, waiting rooms, and visitation areas'),
      ('b1','Dayrooms and visitation rooms in correctional and detention facilities'),
      ('b1','Transitional housing, shelters, and other intensive-use interiors'),
      ('p',LINKS)]
    notes=[HONDO_NEW if first else HONDO_REF,
      price_note(h,lst),
      'Ligature resistance: on the Norix spec sheets, only the molded plinth base'+(' and rocker' if '851' in has else '')+' versions say "ligature resistant design with no internal openings"; the steel leg and molded wood-grain leg versions do not. Our current page says "Anti-Ligature" for all versions, so the new copy says it only for the plinth base'+(' and rocker' if '851' in has else '')+'.' if not lig_all else 'Ligature resistance: the spec sheet says "ligature resistant design with no internal openings."',
      'Colors: our current page says "choice of 5 durable seat colors" but lists 6. The price list and design guide give 6 seat colors: Twilight, Sage, Clay, Sienna, Dove, and Raven. Corrected.',
      ]+list(extra_notes)+[
      photo_note(h,page,bases),
      'Removed: the long old series paragraph and the long old "About Norix Furniture" paragraph; replaced with the new Hondo Nuevo section and the standard paragraph used on all Norix pages.',
      'Collections: the product is in Behavioral Healthcare, Prison and Detention Furniture, Transitional Housing, and Norix Furniture. Following your note on the Forté tabs, the collections sentence links only to Behavioral Healthcare Anti-Ligature Furniture.']
    specs=[(f'{code}.HN{b} {name} ({BASE_DESC[b]})',SPEC[(code,b)]) for b in bases]+[('Hondo Nuevo Brochure',U+'2023/06/Hondo_Nuevo_Brochure_2023.pdf')]
    add(tab=f'{code} - Hondo Nuevo {name}',short=short,handle=h,src=NP+'hondo-nuevo-'+page+'/',specs=specs,
        h1=h1,cur_h1=C(h)['cur_h1'],sub=sub,cur_sub=C(h)['cur_sub'],intro=intro,bullets=bul,models=models,install=inst,
        apps=apps,series=HONDO_SERIES,mt=mt,cur_mt=C(h)['cur_mt'],md=md,cur_md=C(h)['cur_md'],notes=notes)

import re as _re
SPEC={}
for _u in open('spec/urls.txt').read().split():
    _m=_re.search(r'/(HN\d+[RL]?)\.HN(\d+)-',_u)
    if _m: SPEC[(_m[1],_m[2])]=_u
LIVE={h:_j.load(open(f'live/{h}.json'))['product'] for h in CUR}
OPT='**Options:** Ganging kit (C011-023, or C011-025 for steel legs), locking ganging kit (C011-019, or C011-024 for steel legs), bolt-down kit, and factory ballasting (50 lbs, molded plinth base only)'
OPT_R='**Options:** Ganging kit (C011-023, or C011-025 for steel legs), locking ganging kit (C011-019, or C011-024 for steel legs), and bolt-down kit for the plinth, wood-grain leg, and steel leg models; factory ballasting (50 lbs) for the molded plinth base and rocker base'
APP_CHAIR='The {} suits lounges, dayrooms, and waiting areas where people sit for long periods, and where seating has to be comfortable, easy to clean, and hard to damage or move.'
APP_MOD='The {} suits lounges, dayrooms, and waiting areas where Hondo Nuevo pieces are combined into longer runs of seating that are easy to clean and hard to damage or move.'

# 1. HN800 Arm Chair (4 variants incl. rocker)
h='norix-hn800-series-hondo-nuevo-arm-chair-n700400'
hondo(1,h,'arm-chair','HN800','Arm Chair','HN800: Hondo Nuevo Arm Chair',
 'Norix Hondo Nuevo Modular Arm Chair – HN800',
 'Heavy-Duty 30” Soft Seating Arm Chair with a Seamless Vinyl Shell, on a Molded Plinth Base, Rocker Base, Wood-Grain Legs, or Steel Legs',
 ['The **Norix Hondo Nuevo Arm Chair** is a heavy-duty modular lounge chair for intensive-use rooms in behavioral healthcare and correctional facilities. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit with good lumbar support, and the arm height and generous seat width help residents with reduced mobility sit down and get up.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, a rocker base, molded wood-grain legs, or steel legs. The chair can be ganged with other Hondo Nuevo pieces, bolted down, or factory ballasted on the plinth and rocker bases.'],
 '**Overall Size:** 30”W×31”D×32”H','**Seat:** 18.5” seat height and 21” seat width, with a 26” arm height',
 {'850':103,'851':103,'860':103,'855':115},{'850':2187,'860':2296,'855':2406,'851':2187},OPT_R,APP_CHAIR.format('Norix Hondo Nuevo Arm Chair'),
 'Norix Hondo Nuevo Modular Arm Chair - HN800 at Anchortex',
 'Norix Hondo Nuevo Arm Chair is a heavy-duty modular lounge chair with a seamless vinyl shell, on a plinth base, rocker base, wood-grain legs, or steel legs. Shop it at Anchortex.',
 first=True,
 extra_notes=['Weight: the spec sheets give 103 lbs for the molded plinth base and the rocker base; the price list and our current page say 110 lbs. I used the spec sheets (103 lbs, as in the worksheet rows 255 and 258).',
  'SKU: the rocker base variant has SKU N700400, while the other three are N700400-01, -02, and -03. Should the rocker be N700400-04? (No change made.)',
  'Rocker base: the rocker cannot be ganged or bolted down (price list "N/A"); it can be factory ballasted.'])

# 2. HN805R Right Arm Sectional
h='norix-hn805r-series-hondo-nuevo-right-arm-sectional-seat-n700401'
hondo(2,h,'right-arm-sectional','HN805R','Right Arm Sectional','HN805R: Hondo Nuevo Right Arm Sectional Seat',
 'Norix Hondo Nuevo Right Arm Sectional Seat – HN805R',
 'Modular Sectional Seat with One Arm and a Seamless Vinyl Shell, for Building Hondo Nuevo Sofas and Seating Runs',
 ['The **Norix Hondo Nuevo Right Arm Sectional Seat** is a modular seat with a single arm, used with other Hondo Nuevo pieces to build sofas and longer seating runs in behavioral healthcare and correctional facilities. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit with good lumbar support.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The seat can be ganged to the left arm sectional, armless chairs, and wedges, bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 30”W×31”D×32”H','**Seat:** 18.5” seat height, with a 26” arm height',
 {'850':99,'860':93,'855':104},{'850':2129,'860':2235,'855':2341},OPT,APP_MOD.format('Norix Hondo Nuevo Right Arm Sectional Seat'),
 'Norix Hondo Nuevo Right Arm Sectional Seat - HN805R at Anchortex',
 'Norix Hondo Nuevo Right Arm Sectional Seat is a one-arm modular seat with a seamless vinyl shell, for building Hondo Nuevo sofas and seating runs. Shop it at Anchortex.')

# 3. HN805L Left Arm Sectional
h='norix-hn805l-series-hondo-nuevo-left-arm-sectional-seat-n700402'
hondo(3,h,'left-arm-sectional','HN805L','Left Arm Sectional','HN805L: Hondo Nuevo Left Arm Sectional Seat',
 'Norix Hondo Nuevo Left Arm Sectional Seat – HN805L',
 'Modular Sectional Seat with One Arm and a Seamless Vinyl Shell, for Building Hondo Nuevo Sofas and Seating Runs',
 ['The **Norix Hondo Nuevo Left Arm Sectional Seat** is a modular seat with a single arm, used with other Hondo Nuevo pieces to build sofas and longer seating runs in behavioral healthcare and correctional facilities. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit with good lumbar support.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The seat can be ganged to the right arm sectional, armless chairs, and wedges, bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 30”W×31”D×32”H','**Seat:** 18.5” seat height, with a 26” arm height',
 {'850':99,'860':93,'855':104},{'850':2129,'860':2235,'855':2341},OPT,APP_MOD.format('Norix Hondo Nuevo Left Arm Sectional Seat'),
 'Norix Hondo Nuevo Left Arm Sectional Seat - HN805L at Anchortex',
 'Norix Hondo Nuevo Left Arm Sectional Seat is a one-arm modular seat with a seamless vinyl shell, for building Hondo Nuevo sofas and seating runs. Shop it at Anchortex.')

# 4. HN810 30" Armless
h='norix-hn810-series-hondo-nuevo-30-armless-chair-n700403'
hondo(4,h,'thirty-inch-armless','HN810','30” Armless Chair','HN810: Hondo Nuevo 30” Armless Chair',
 'Norix Hondo Nuevo 30” Armless Chair – HN810',
 'Wide Armless Modular Chair with a Seamless Vinyl Shell, for Use Alone or Ganged into Hondo Nuevo Seating Runs',
 ['The **Norix Hondo Nuevo 30” Armless Chair** is a wide armless modular chair for lounges and dayrooms in behavioral healthcare and correctional facilities. Use it on its own or gang it between sectional seats and wedges to build a sofa or a longer seating run. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit with good lumbar support.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The chair can be ganged, bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 30”W×30”D×32”H','**Seat:** 18.5” seat height',
 {'850':96,'860':90,'855':101},{'850':1926,'860':2023,'855':2119},OPT,APP_MOD.format('Norix Hondo Nuevo 30” Armless Chair'),
 'Norix Hondo Nuevo 30” Armless Chair - HN810 at Anchortex',
 'Norix Hondo Nuevo 30” Armless Chair is a wide modular chair with a seamless vinyl shell that can be used alone or ganged into Hondo Nuevo seating runs. Shop it at Anchortex.',
 extra_notes=['Name: our current H1 calls it an "Armless Sectional Chair"; Norix calls it the "Hondo Nuevo 30 Inch Armless." I used "30” Armless Chair" so it is clear how it differs from the 24” HN820.'])

# 5. HN820 24" Armless
h='norix-hn820-series-hondo-nuevo-24-armless-chair-n700404'
hondo(5,h,'twenty-four-inch-armless','HN820','24” Armless Chair','HN820: Hondo Nuevo 24” Armless Chair',
 'Norix Hondo Nuevo 24” Narrow Armless Chair – HN820',
 'Space-Saving Armless Modular Chair with a Seamless Vinyl Shell, for Use Alone or Ganged into Hondo Nuevo Seating Runs',
 ['The **Norix Hondo Nuevo 24” Armless Chair** is a narrow armless modular chair for lounges, dayrooms, and waiting areas in behavioral healthcare and correctional facilities where space is tight. Use it on its own or gang it with other Hondo Nuevo pieces. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit with good lumbar support.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The chair can be ganged, bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 24”W×30”D×32”H','**Seat:** 18.5” seat height',
 {'850':77,'860':73,'855':83},{'850':1748,'860':1853,'855':1922},OPT,APP_MOD.format('Norix Hondo Nuevo 24” Armless Chair'),
 'Norix Hondo Nuevo 24” Narrow Armless Chair - HN820 at Anchortex',
 'Norix Hondo Nuevo 24” Armless Chair is a narrow modular chair with a seamless vinyl shell for tight spaces, used alone or ganged into seating runs. Shop it at Anchortex.',
 extra_notes=['H1: our current H1 says "Models HN820/HN850," but HN850 is the molded plinth base code, not a model. The new H1 uses HN820 only.'])

# 6. HN815 Cube
h='norix-hn815-series-hondo-nuevo-cube-n700405'
hondo(6,h,'cube','HN815','Cube','HN815: Hondo Nuevo Cube',
 'Norix Hondo Nuevo Cube Seat – HN815',
 'Square Backless Modular Seat with a Seamless Vinyl Shell, for Lounges, Dayrooms, and Hondo Nuevo Seating Groups',
 ['The **Norix Hondo Nuevo Cube** is a square, backless modular seat for lounges, dayrooms, and waiting areas in behavioral healthcare and correctional facilities. Use it as extra seating on its own or gang it with other Hondo Nuevo pieces. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The cube can be ganged, bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 30”W×30”D×18.5”H','**Seat:** 18.5” seat height, backless',
 {'850':73,'860':66,'855':78},{'850':1515,'860':1589,'855':1667},OPT,APP_MOD.format('Norix Hondo Nuevo Cube'),
 'Norix Hondo Nuevo Modular Cube Seat - HN815 at Anchortex',
 'Norix Hondo Nuevo Cube is a square, backless modular seat with a seamless vinyl shell, used alone or ganged with other Hondo Nuevo seating. Shop it at Anchortex.',
 extra_notes=['Use: our current subtitle calls it a "Cube Sectional Seat Table." Norix lists it with the seating and gives a seat height, so I described it as a seat, not a table.'])

# 7. HN830 Bench
h='norix-hn830-series-hondo-nuevo-bench-wedge-seat-n700406'
hondo(7,h,'bench','HN830','Bench','HN830: Hondo Nuevo Bench',
 'Norix Hondo Nuevo Modular Bench Seat – HN830',
 'Backless Modular Bench Seat with a Seamless Vinyl Shell, for Use Alone or Ganged into Hondo Nuevo Seating Runs',
 ['The **Norix Hondo Nuevo Bench** is a backless modular bench seat for lounges, dayrooms, and waiting areas in behavioral healthcare and correctional facilities. Use it on its own or gang it with bench wedges and other Hondo Nuevo pieces to build longer or curved benches. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The bench can be ganged, bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 24”W×30”D×18.5”H','**Seat:** 18.5” seat height, backless',
 {'850':62,'860':57,'855':66},{'850':1399,'860':1469,'855':1539},OPT,APP_MOD.format('Norix Hondo Nuevo Bench'),
 'Norix Hondo Nuevo Modular Bench Seat - HN830 at Anchortex',
 'Norix Hondo Nuevo Bench is a backless modular bench seat with a seamless vinyl shell, used alone or ganged with wedges into longer or curved benches. Shop it at Anchortex.',
 extra_notes=['URL: the page address ends "...hn830-series-hondo-nuevo-bench-wedge-seat...," but this product is the straight bench (the bench wedge is HN835). The URL was not changed.'])

# 8. HN835 Bench Wedge
h='norix-hn835-series-hondo-nuevo-bench-wedge-seat-n700407'
hondo(8,h,'bench-wedge','HN835','Bench Wedge','HN835: Hondo Nuevo Bench Wedge',
 'Norix Hondo Nuevo Bench Wedge Seat – HN835',
 'Backless Wedge-Shaped Modular Seat with a Seamless Vinyl Shell, for Building Curved Hondo Nuevo Benches',
 ['The **Norix Hondo Nuevo Bench Wedge** is a backless, wedge-shaped modular seat for building curved and angled benches with other Hondo Nuevo pieces in behavioral healthcare and correctional facilities. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The bench wedge can be ganged, bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 31.5”W×30”D×18.5”H','**Seat:** 18.5” seat height, backless',
 {'850':53,'860':47,'855':57},{'850':1357,'860':1425,'855':1494},OPT,APP_MOD.format('Norix Hondo Nuevo Bench Wedge'),
 'Norix Hondo Nuevo Bench Wedge Seat - HN835 at Anchortex',
 'Norix Hondo Nuevo Bench Wedge is a backless, wedge-shaped modular seat with a seamless vinyl shell for building curved Hondo Nuevo benches. Shop it at Anchortex.')

# 9. HN825 Seat Wedge
h='norix-hn825-series-hondo-nuevo-seat-wedge-n700408'
hondo(9,h,'seat-wedge','HN825','Seat Wedge','HN825: Hondo Nuevo Seat Wedge',
 'Norix Hondo Nuevo Seat Wedge with Back – HN825',
 'Wedge-Shaped Modular Seat with a Back and a Seamless Vinyl Shell, for Building Curved Hondo Nuevo Sofas',
 ['The **Norix Hondo Nuevo Seat Wedge** is a wedge-shaped modular seat with a back, used between sectional seats and armless chairs to build curved and angled sofas in behavioral healthcare and correctional facilities. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit with good lumbar support.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The seat wedge can be ganged, bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 31.5”W×30”D×32”H','**Seat:** 18.5” seat height',
 {'850':76,'860':76,'855':81},{'850':1628,'860':1711,'855':1791},OPT,APP_MOD.format('Norix Hondo Nuevo Seat Wedge'),
 'Norix Hondo Nuevo Seat Wedge with Back - HN825 at Anchortex',
 'Norix Hondo Nuevo Seat Wedge is a wedge-shaped modular seat with a back and a seamless vinyl shell, for building curved Hondo Nuevo sofas. Shop it at Anchortex.')

# 10. HN840 Stool (plinth only)
h='norix-hn840-hondo-nuevo-stool-n700409'
hondo(10,h,'stool','HN840','Stool','HN840: Hondo Nuevo Stool',
 'Norix Hondo Nuevo Round Stool with Molded Plinth Base – HN840',
 'Lightweight 18” Round Soft Seat with a Seamless Vinyl Shell, for Dayrooms, Lounges, and Activity Rooms',
 ['The **Norix Hondo Nuevo Stool** is a lightweight, 18” round soft seat on a molded plinth base, for dayrooms, lounges, and activity rooms in behavioral healthcare and correctional facilities. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit, and at 23 lbs it is easy to move around a room.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and the seat is fastened to the base with tamper-resistant hardware. The stool comes on a molded plinth base only, and it cannot be ballasted, ganged, or bolted down.'],
 '**Overall Size:** 18” diameter×18.5”H','**Seat:** 18.5” seat height, backless',
 {'850':23},{'850':700},None,'The Norix Hondo Nuevo Stool suits rooms that need light, movable extra seating that is soft, easy to clean, and hard to damage.',
 'Norix Hondo Nuevo Round Stool - HN840 at Anchortex',
 'Norix Hondo Nuevo Stool is a lightweight, 18 inch round soft seat with a seamless vinyl shell on a molded plinth base, for dayrooms and lounges. Shop it at Anchortex.',
 ballast=0,lig_all=True,
 extra_notes=['Options: the price list says the stool cannot be ballasted, and the spec sheet lists no options (no ganging or bolt-down), so none are listed.'])

# 11. HN845 Round Ottoman
h='norix-hn845-series-hondo-nuevo-round-ottoman-n700410'
hondo(11,h,'round-ottoman','HN845','Round Ottoman','HN845: Hondo Nuevo Round Ottoman',
 'Norix Hondo Nuevo 30” Round Ottoman – HN845',
 'Large Round Backless Soft Seat with a Seamless Vinyl Shell, on a Molded Plinth Base, Wood-Grain Legs, or Steel Legs',
 ['The **Norix Hondo Nuevo Round Ottoman** is a large, 30” round backless soft seat for lounges, dayrooms, and waiting areas in behavioral healthcare and correctional facilities. It adds seating from every side in the middle of a room or alongside other Hondo Nuevo pieces. A one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The ottoman can be bolted down, or factory ballasted on the plinth base.'],
 '**Overall Size:** 30” diameter×18.5”H','**Seat:** 18.5” seat height, backless',
 {'850':62,'860':56,'855':65},{'850':1399,'860':1469,'855':1539},'**Options:** Bolt-down kit and factory ballasting (50 lbs, molded plinth base only)','The Norix Hondo Nuevo Round Ottoman suits lounges, dayrooms, and waiting areas that need extra seating in the middle of a room, with furniture that is easy to clean and hard to damage or move.',
 'Norix Hondo Nuevo 30” Round Ottoman - HN845 at Anchortex',
 'Norix Hondo Nuevo Round Ottoman is a large, 30 inch round backless soft seat with a seamless vinyl shell, on a plinth base, wood-grain legs, or steel legs. Shop it at Anchortex.',
 extra_notes=['Ganging: the spec sheets list a ganging kit for the ottoman, but the price list has no ganging kit for it (only bolt-down and ballasting). I listed only bolt-down and ballasting. Is a ganging kit available?'])

# 12. HN880 High Back Chair (4 variants incl. rocker)
h='norix-hn880-series-hondo-nuevo-high-back-chair-n700411'
hondo(12,h,'high-back','HN880','High Back Chair','HN880: Hondo Nuevo High Back Chair',
 'Norix Hondo Nuevo High Back Arm Chair – HN880',
 'Heavy-Duty High Back Lounge Chair with Arms and a Seamless Vinyl Shell, on a Molded Plinth Base, Rocker Base, Wood-Grain Legs, or Steel Legs',
 ['The **Norix Hondo Nuevo High Back Chair** is a heavy-duty, 44” high lounge chair with arms for intensive-use rooms in behavioral healthcare and correctional facilities. The high back supports the head and shoulders, and a one-piece, rotationally molded vinyl skin over a foam core gives a cushioned sit with good lumbar support. The arm height and generous seat width help residents with reduced mobility sit down and get up.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, a rocker base, molded wood-grain legs, or steel legs. The chair can be ganged with other Hondo Nuevo pieces, bolted down, or factory ballasted on the plinth and rocker bases.'],
 '**Overall Size:** 30”W×31”D×44”H','**Seat:** 18.5” seat height and 21” seat width, with a 26” arm height',
 {'850':127,'851':127,'860':121,'855':132},{'850':2453,'851':2453,'860':2562,'855':2594},OPT_R,APP_CHAIR.format('Norix Hondo Nuevo High Back Chair'),
 'Norix Hondo Nuevo High Back Arm Chair - HN880 at Anchortex',
 'Norix Hondo Nuevo High Back Chair is a heavy-duty, 44 inch high lounge chair with arms and a seamless vinyl shell, on a plinth, rocker, wood-grain, or steel base. Shop it at Anchortex.',
 extra_notes=['Rocker base: the rocker cannot be ganged or bolted down (price list "N/A"); it can be factory ballasted.'])

# 13. HN885 Footstool (ballast 30)
h='norix-hn885-series-hondo-nuevo-footstool-n700412'
hondo(13,h,'footstool','HN885','Footstool','HN885: Hondo Nuevo Footstool',
 'Norix Hondo Nuevo Footstool – HN885',
 'Low Soft Footrest with a Seamless Vinyl Shell, to Pair with Hondo Nuevo Chairs on a Plinth Base, Wood-Grain Legs, or Steel Legs',
 ['The **Norix Hondo Nuevo Footstool** is a low, cushioned footrest that pairs with the Hondo Nuevo arm chair and high back chair in lounges and dayrooms in behavioral healthcare and correctional facilities. A one-piece, rotationally molded vinyl skin over a foam core gives a soft, durable surface.',
  'The seamless, fluid-resistant surface is easy to clean and sanitize, and a drip edge keeps fluids from running into the base. Choose a molded plinth base, molded wood-grain legs, or steel legs. The footstool can be bolted down, or factory ballasted with 30 lbs on the plinth base.'],
 '**Overall Size:** 20.8”W×17.6”D×15.5”H','',
 {'850':29,'860':28,'855':35},{'850':1013,'860':1081,'855':1150},'**Options:** Bolt-down kit and factory ballasting (30 lbs, molded plinth base only)',
 'The Norix Hondo Nuevo Footstool suits lounges and dayrooms where residents need a comfortable place to rest their feet, with furniture that is easy to clean and hard to damage.',
 'Norix Hondo Nuevo Modular Footstool - HN885 at Anchortex',
 'Norix Hondo Nuevo Footstool is a low, cushioned footrest with a seamless vinyl shell that pairs with Hondo Nuevo chairs, on a plinth base, wood legs, or steel legs. Shop it at Anchortex.',
 ballast=30,
 extra_notes=['Ballast: the footstool plinth base takes 30 lbs of ballast (the other Hondo Nuevo plinth bases take 50 lbs), per the spec sheet and price list.',
  'Ganging: the spec sheets list a ganging kit for the footstool, but the price list has no ganging kit for it (only bolt-down and ballasting). I listed only bolt-down and ballasting. Is a ganging kit available?'])
