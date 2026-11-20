# Group 4 Cortech tabs, batch 2 (Nov 18): the remaining 13. Loaded by mc7.py after pc6.py (constants from earlier groups too).
P=[]
def add(**k): P.append(k)
SEQC=CP+'furniture/endurance/sequoia-series-beds/'
FLUL='**Flammability Standards:** Passes UL 94 HB'
VEL='**Finish:** Veldura soft-touch exterior that contrasts with the molded base'
NOBOLT=('Bolt-down: Cortech has bolt-down plate instructions for this chair, fitted at the ballast door. They do not say whether the plate is sold separately, so I left floor mounting out.')
FLN=('Flammability: the Cortech spec sheet says the chair passes UL 94 HB. The Cortech web page also says CAL 133, but the spec sheet does not, so I used UL 94 HB only.')
CORXN='Antimicrobial: the Cortech spec sheet says "Infused with CORx Antibacterial" and tested to ISO 22196. I used the ISO 22196 test result.'
SUM_APPS=['Patient rooms, dayrooms, and lounges in behavioral healthcare facilities and psychiatric hospitals','Group rooms and visitor areas in residential treatment centers','Other secure settings that want a calm, residential look']
TBL_APPS2=['Dayrooms, lounges, and waiting areas in behavioral healthcare facilities and psychiatric hospitals','Dining and activity areas in residential treatment centers','Other secure settings that want a calm, residential look']
NIGHT_COLL=f"Explore Anchortex's [Behavioral Healthcare Anti-Ligature Furniture]({BH}) collection for more patient room furniture."
SB_SERIES=[x for x in FM_SERIES[:-1] if not x[1].startswith('**Can Dollies:**')]+[('b1','**Carts:** Kangaroo Carts and lids for laundry, trash, and material handling'),
  ('b1','**Secure Waste Bins:** The lockable SafeBin with a 35-gallon inner container')]
SEQ_FIN='**Finishes:** Heritage Oak, Natural Oak, Coastal Driftwood, Walnut, or Redwood wood grain (custom wood grain finishes available on request)'
SEQ_CRAFT='**Wood Grain:** Like natural wood, each piece varies slightly in color and grain'
SEQ_AWARD='**Award:** The Sequoia Series earned a 2025 Gold Nightingale Award in the Anti-Ligature and Reduced-Ligature Furnishings category'
TBL_FL='**Flammability Standards:** Laminate surfaces pass CAL 117; the base is flame retardant and passes California Technical Bulletin 133'
TBL_GG='**Environmental Certification:** GREENGUARD Gold (laminate tops not included)'
TBL_W='**Warranty:** Lifetime warranty on the base; 5-year warranty on the laminate top, against manufacturing defects'
TBL_TOP='**Top:** High-pressure laminate top with a Dura-Edge; it resists moisture and impact and cleans easily'
TBL_BASE='**Base:** One-piece rotationally molded high impact polyethylene; no steel or wood components'
TBL_ASM='**Assembly:** The base attaches to the top with tamper-resistant screws; hardware bit size is T40'
TBL_GGN='GREENGUARD Gold: the Cortech spec sheet says "Greenguard Gold Certified *Laminate Tops not included," which I read as the certification covering the base only. I wrote "(laminate tops not included)." Please check the wording.'
TBL_COL='**Base Colors:** '+COLORS18
def chair(model,name,vel,w,dims,wt,note_w,imgs,live_dims=None,extra_notes=()):
    S=model+'S'; full=f'Summit {"Veldura " if vel else ""}{name}'
    intro=[f'The **Cortech {full}** is a molded {name.lower()} with a calm, residential look for patient rooms, dayrooms, lounges, and group spaces in behavioral healthcare and other secure settings. '
           +('The Veldura soft-touch surface adds comfort and warmth without giving up durability.' if vel else 'Its rounded edges and smooth surfaces support safety, and it can stand alone or be arranged in groups.'),
           f'The chair is rotationally molded in one piece from high impact “no break” polyethylene, with no steel or wood components. It can be weighted at the factory, or the {S} can be ballasted with sandbags on site.']
    b=[NOSTEEL]+([VEL] if vel else [])+[f'**Dimensions:** {dims}',f'**Weight:** {wt}',
       f'**Weighting:** Factory sand ballasting optional; the {S} has a ballast door for adding sandbags on site that closes with tamper-resistant screws. Do not use loose sand',
       OUT,ISO22,FLUL,GGW,CLEAN2,COL18,LIFE,ISO]
    lab='Veldura' if vel else 'Standard'
    models=[f'**{model} – {lab}:** Without ballast door',f'**{S} – {lab} with Ballast Door:** Ballast door for adding sandbags on site']
    inst=[f'**Weighting:** Can be factory weighted, or add sandbags on site through the ballast door on the {S}; do not use loose sand. Hardware bit size is T27']
    notes=[SER_SUM,f'H1: Cortech calls it the {full}. I took out the extra words from your current title and added the {S}.',note_w]
    if live_dims: notes.append(live_dims)
    notes+=list(extra_notes)+[FLN,CORXN,NOBOLT,outn(f'the {full} is'),imgs]
    return dict(intro=intro,bullets=b,models=models,install=inst,notes=notes,
      apps=apps(f'The {full} suits rooms that need comfortable, durable seating that is hard to break or tamper with.',SUM_APPS,END_COLL),series=SUMMIT_SERIES)

# 1. HookMax HM
add(tab='HM - Cortech HookMax Ligature Resistant Hook',short='HM: Cortech HookMax Ligature Resistant Wall Hook',
 handle='cortech-hm-ligature-resistant-hookmax-wall-hook',src=[HOOKC+'hookmax/'],
 specs=[('HM',CU+'HookMax-Spec-Sheet.pdf')],
 h1='Cortech HookMax Ligature Resistant Wall Hook – HM',
 cur_h1='Cortech Ligature Resistant HookMax Wall Hook - HM',
 sub='Flexible Wall Hook That Bends and Releases at a Maximum 10 lb Load, Sold in Packs of 5',
 cur_sub='Cortech USA HM Hookmax Anti-Ligature Hooks',
 intro=['The **Cortech HookMax Ligature Resistant Wall Hook** holds clothing and towels in resident rooms, bathrooms, and common areas of behavioral healthcare and correctional facilities. It releases at a maximum load of 10 lbs: the hook bends, the item or ligature slides off, and the hook returns to its shape.',
  'The hook has a PC/ABS core and a flexible TPU outer piece that helps prevent injury, and it releases in all directions, so it can be placed close to furniture and doors. It comes in five colors and is sold in packs of 5.'],
 bullets=['**Material:** PC/ABS core with a flexible TPU outer piece',
  '**Dimensions:** 1.24”W×0.85”D×2.05”H',
  '**Release:** Releases in all directions (360°) at a maximum 10 lb load, then returns to its shape',
  '**Testing:** Load release tests with a string, shoelace, or rope made from bedsheets release at a maximum of 10 lbs',
  '**Mounting:** Mount to a flat surface so the hook fits tightly against the wall',
  '**Care:** Resistant to alcohol and most detergents',
  '**Colors:** White, Gray, Black, Beige, or Magenta',
  '**Packaging:** Sold in packs of 5. Price is per pack',
  '**Warranty:** 3-year warranty for the intended use; full warranty against manufacturing defects',
  '**Country of Manufacture:** Designed and produced in Sweden'],
 models=['**HookMax, 5 Pack:** HMWH - White, HMGY - Gray, HMBK - Black, HMBE - Beige, HMMG - Magenta'],
 install=[],
 apps=apps('The HookMax suits rooms where residents need a place to hang clothing and towels without creating a ligature point.',
  ['Resident rooms and bathrooms in behavioral healthcare facilities and psychiatric hospitals','Cells and common areas in correctional facilities and jails','Residential treatment centers and shelters'],HOOK_COLL),
 series=HOOK_SERIES,
 mt='Cortech HookMax Ligature Resistant Wall Hook - HM at Anchortex',
 md='Shop the Cortech HookMax ligature resistant wall hook. A flexible hook that bends and releases at a maximum 10 lb load so ligatures slide off. Packs of 5.',
 notes=[SER_HOOK,
  'H1: Cortech calls it the Ligature Resistant HookMax. I put "HookMax" first and used "Wall Hook," to match the HookMax+ page.',
  'Colors: your variant is "HM - Pack of 5" with no color option. Cortech sells the HookMax in five colors (HMWH White, HMGY Gray, HMBK Black, HMBE Beige, HMMG Magenta). How do customers choose a color? Would you like color variants?',
  'Weight and size: your variant is set to 5 lbs. The Cortech spec sheet does not give a weight. The dimensions are for one hook.',
  'Country of manufacture: the Cortech spec sheet says the HookMax is designed and produced in Sweden, so I added it.',
  'Mounting: the Cortech spec sheet says to mount the hook to a flat surface for a tight fit, but does not say how it attaches (screws or adhesive), so I left that out.',
  'I left out "Patent pending," to match the other pages.',
  'Product images: the page has one image. I did not find other HookMax photos on the Cortech website.'])

# 2. Summit Lounge Chair 320
c=chair('320','Lounge Chair',False,None,'29”W×59”D×35”H','50 lbs',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet says 50 lbs, so I used 50 lbs.',
  'Product images: the page has five images, including two Summit color charts. The Cortech product page has photos of the Summit Lounge Chair in all 18 colors and a photo with a Summit Side Table. Would you like me to add them?',
  live_dims='Dimensions: your current page says 29”H×27”W×29”D, which are the Summit Accent Chair dimensions. The Cortech spec sheet says 35”H×29”W×59”D for the lounge chair, so I used those.')
add(tab='320 - Cortech Summit Lounge Chair',short='320 / 320S: Cortech Summit Lounge Chair',
 handle='cortech-320-summit-lounge-chair',src=[SUMC+'summit-lounge-chair/'],
 specs=[('320 / 321',CU+'Summit-Lounge-Chair-spec-sheet.pdf')],
 h1='Cortech Summit Lounge Chair – 320 / 320S',
 cur_h1='Cortech Summit - Lounge Chair - One‑Piece Rotationally Molded Ergonomic Design - Model 320',
 sub='One-Piece Molded Lounge Chair with a Residential Look and an Optional Ballast Door',
 cur_sub='Cortech 320 Summit Lounge Chair',
 mt='Cortech Summit Molded Lounge Chair - 320 / 320S at Anchortex',
 md='Shop the Cortech Summit Lounge Chair, a one-piece molded lounge chair with a calm, residential look and an optional ballast door, rated for outdoor use.',**c)

# 3. Summit Veldura Lounge Chair 321
c=chair('321','Lounge Chair',True,None,'29”W×59”D×35”H','50 lbs',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet gives 50 lbs for the Summit Lounge Chair and no separate weight for the Veldura version, so I used 50 lbs.',
  'Product images: the page has five images, including two Summit color charts. The Cortech product page has photos of the Summit Veldura Lounge Chair in all 18 colors and a photo with a Summit Side Table. Would you like me to add them?',
  live_dims='Dimensions: your current page says 29”H×27”W×29”D, which are the Summit Accent Chair dimensions. The Cortech spec sheet says 35”H×29”W×59”D for the lounge chair, so I used those.',
  extra_notes=['Your current page says "Model 320S has a ballast door." I used 321S, the Veldura model on the Cortech spec sheet.'])
add(tab='321 - Cortech Summit Veldura Lounge Chair',short='321 / 321S: Cortech Summit Veldura Lounge Chair',
 handle='cortech-321-summit-veldura-lounge-chair',src=[SUMC+'summit-veldura-lounge-chair/'],
 specs=[('320 / 321',CU+'Summit-Lounge-Chair-spec-sheet.pdf')],
 h1='Cortech Summit Veldura Lounge Chair – 321 / 321S',
 cur_h1='Cortech Summit Lounge Chair with Veldura - One-Piece Rotationally Molded - Model 321',
 sub='One-Piece Molded Lounge Chair with a Veldura Soft-Touch Finish and an Optional Ballast Door',
 cur_sub='Cortech 321 Summit Veldura Lounge Chair with Veldura Soft-Touch Exterior',
 mt='Cortech Summit Veldura Lounge Chair - 321 / 321S at Anchortex',
 md='Shop the Cortech Summit Veldura Lounge Chair, a one-piece molded chair with a Veldura soft-touch finish and an optional ballast door, rated for outdoor use.',**c)

# 4. Summit Side Table 342 / 343
add(tab='342 / 343 - Cortech Summit Side Table',short='342 / 343: Cortech Summit Side Table',
 handle='cortech-342-343-summit-side-table',src=[CP+'furniture/tables/summit-side-table/'],
 specs=[('342 / 343',CU+'Summit-Side-Table-spec-sheet-1.pdf'),('Assembly',CU+'Summit-Side-Table-Assembly-Instructions.pdf'),('Bolt-down',CU+'Stool-Side-Table-Bolt-Down-Installation-Instructions.pdf')],
 h1='Cortech Summit Side Table – 342 / 343',
 cur_h1='Cortech Summit Side Table - Molded Base with Laminate Top - Models 342 & 343',
 sub='Low Side Table with a Molded Base and a Laminate Delta Top, in Small or Medium Sizes',
 cur_sub='Cortech 342 Summit Low Table with Small Delta Top, Cortech 343 Summit Low Table with Mid Delta Top',
 intro=['The **Cortech Summit Side Table** is a low side table with a molded base and a laminate delta top, for lounges, dayrooms, waiting areas, and patient spaces in behavioral healthcare and other secure settings. It coordinates with Summit seating for a calm, residential look.',
  'The one-piece molded base has no seams or joints to tamper with. The table is designed to be weighted with sandbags in the base.'],
 bullets=[TBL_BASE,TBL_TOP,
  '**Sizes:** Small delta top (342 / 342S) or medium delta top (343 / 343S)',
  '**Dimensions:** 22”W×22”D×18”H',
  '**Weight:** 23 lbs (top 11 lbs, base 12 lbs)',
  '**Weighting:** The base can be filled with sandbags; do not use loose sand. Optional bolt-down plates available',
  TBL_FL,TBL_GG,CLEAN2,TBL_COL,TBL_W,ISO],
 models=['**342 – Small Delta Top:** Without ballast door','**342S – Small Delta Top with Ballast Door:** Ballast door for adding sandbags','**343 – Medium Delta Top:** Without ballast door','**343S – Medium Delta Top with Ballast Door:** Ballast door for adding sandbags'],
 install=[TBL_ASM,'**Weighting:** Add sandbags through the ballast door in the base on the 342S and 343S; do not use loose sand. Ballast door bit size is T27'],
 apps=apps('The Summit Side Table suits lounges and patient areas that want a small, stable table that is easy to clean.',TBL_APPS2,END_COLL),
 series=SUMMIT_SERIES,
 mt='Cortech Summit Side Table - 342 / 343 at Anchortex',
 md='Shop the Cortech Summit Side Table, a low side table with a one-piece molded base and a laminate delta top in small or medium sizes for behavioral health rooms.',
 notes=[SER_SUM,
  'H1: I took out "Molded Base with Laminate Top" and "Models."',
  'Variant names: your variants are 342S and 343S, "with ballast door." The Cortech spec sheet lists 342 and 343 only, with no S models. Can you check the model numbers with Cortech?',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet says 23 lbs (top 11 lbs, base 12 lbs), so I used 23 lbs.',
  'Dimensions: the Cortech spec sheet gives one size (22”×22”×18”H) and does not give a separate size for the medium top.',
  TBL_GGN,
  'Bolt-down plates: the Cortech spec sheet says optional bolt-down plates are available, and Cortech has bolt-down instructions for the side table, but there is no model number for the plates. The FAQ on the Cortech product page says the side table cannot be bolted down. I used the spec sheet. Can you check with Cortech?',
  'Product images: the page has three images, including a Summit color chart. The Cortech product page has two photos of the side table with Summit chairs. Would you like me to add them?'])

# 5. Summit Mid-Range Table 353 / 354
add(tab='353 / 354 - Cortech Summit Mid-Range Table',short='353 / 354: Cortech Summit Mid-Range Table',
 handle='cortech-353-354-summit-mid-range-table',src=[SUMC+'summit-mid-range-table/'],
 specs=[('353 / 354',CU+'Summit-Mid-Range-Table-spec-sheet-2.pdf')],
 h1='Cortech Summit Mid-Range Table – 353 / 354',
 cur_h1='Cortech Summit - Mid-Range Table - Molded Base with Laminate Top - Models 353 & 354',
 sub='Mid-Height Table with a Molded Base and a Laminate Delta Top, with an Optional Ballast Door',
 cur_sub='Cortech 353 Mid-Range Table with Mid-Size Delta Top, Cortech 354 Mid-Range Table with Large Delta Top',
 intro=['The **Cortech Summit Mid-Range Table** is a mid-height table with a molded base and a laminate delta top, for lounges, dayrooms, and patient-focused spaces in behavioral healthcare and other secure settings. It coordinates with Summit seating for a calm, residential look.',
  'The one-piece molded base has no exposed seams or hardware. The table is designed to be weighted.'],
 bullets=[TBL_BASE,TBL_TOP,
  '**Sizes:** Mid delta top (353) or large delta top (354)',
  '**Dimensions:** 39”W×38”D×25”H',
  '**Weight:** 51 lbs (top 36 lbs, base 15 lbs)',
  '**Weighting:** The base can be filled with sandbags; the 353S and 354S have an access door. Do not use loose sand. Optional bolt-down plates available',
  TBL_FL,TBL_GG,CLEAN2,TBL_COL,TBL_W,ISO],
 models=['**353 – Mid Delta Top:** Without access door','**353S – Mid Delta Top with Access Door:** Ballast door for adding sandbags',
  '**354 – Large Delta Top:** Without access door','**354S – Large Delta Top with Access Door:** Ballast door for adding sandbags'],
 install=[TBL_ASM,'**Weighting:** Add sandbags through the access door on the 353S or 354S; do not use loose sand'],
 apps=apps('The Summit Mid-Range Table suits lounges and dayrooms that want a stable, easy-to-clean table at a comfortable height.',TBL_APPS2,END_COLL),
 series=SUMMIT_SERIES,
 mt='Cortech Summit Mid-Range Table - 353 / 354 at Anchortex',
 md='Shop the Cortech Summit Mid-Range Table, a mid-height table with a one-piece molded base and a laminate delta top, with an optional ballast door for weighting.',
 notes=[SER_SUM,
  'H1: I took out "Molded Base with Laminate Top" and "Models."',
  'Variants: your page has only the 353S and 354S (with ballast door). The Cortech spec sheet also lists the 353 and 354 without an access door. I listed all four in Available Models. Would you like the two models without a door added as variants?',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet says 51 lbs (top 36 lbs, base 15 lbs), so I used 51 lbs.',
  'Dimensions: the Cortech spec sheet gives one size (39”W×38”D×25”H) and one weight for both tops.',
  'Bolt-down plates: the Cortech spec sheet says optional bolt-down plates are available, but there is no model number for them. The FAQ on the Cortech product page says the table cannot be bolted down (it names the Summit Side Table, so it looks copied). I used the spec sheet.',
  TBL_GGN,
  'Product images: the page has three images, including a Summit color chart. The Cortech product page has photos of the Mid-Range Table in all 18 base colors. Would you like me to add them?'])

# 6. Summit All Purpose Table 361 / 363 / 364
add(tab='361 / 363 / 364 - Cortech Summit All Purpose Table',short='361 / 363 / 364: Cortech Summit All Purpose Table',
 handle='cortech-361-363-364-summit-all-purpose-table',src=[SUMC+'summit-table/'],
 specs=[('361 / 363 / 364',CU+'Summit-Table-spec-sheet-2.pdf'),('Concealed mounting',CU+'Summit-Concealed-Mounting-Instructions.pdf')],
 h1='Cortech Summit All Purpose Table – 361 / 363 / 364',
 cur_h1='Cortech Summit All-Purpose Table - Molded Base with Laminate Top - Models 361, 363 & 364',
 sub='Dining Height Table with a Molded Base and a 42” Round or Delta Laminate Top',
 cur_sub='Cortech 361 363 364 All Purpose table with Delta Top or 42" Round Top',
 intro=['The **Cortech Summit All Purpose Table** is a dining height table with a molded base and a laminate top, for dining areas, dayrooms, and activity rooms in behavioral healthcare and other secure settings. It comes with a 42” round top or a medium or large delta top.',
  'The one-piece molded base has no exposed seams. The base can be filled with sandbags, and the table can also be bolted to the floor.'],
 bullets=[TBL_BASE,
  '**Top:** High-pressure laminate top with a Dura-Edge, in Gray Nebula with a black edge; it resists moisture and impact and cleans easily',
  '**Sizes:** 42” round top (361 / 361S), medium delta top (363 / 363S), or large delta top (364 / 364S)',
  '**Dimensions:** 42”W×42”D×29”H (42” round top) or 44”W×43”D×29”H (delta top)',
  '**Weight:** Base 16 lbs; delta top 45 lbs; 42” round top 56 lbs',
  '**Game Top:** Optional game top for the 42” round table (361GT)',
  '**Weighting:** The base can be filled with sandbags; do not use loose sand',
  '**Floor Mounting:** Optional concealed mounting',
  TBL_FL,TBL_GG,CLEAN2,TBL_COL,TBL_W,ISO],
 models=['**361 – 42” Round Plain Top:** Gray Nebula laminate, black edge','**361S – 42” Round Plain Top with Ballast Door:** Gray Nebula laminate, black edge','**361GT – 42” Round Game Top:** Game top',
  '**363 – Medium Delta Top:** Gray Nebula laminate, black edge','**363S – Medium Delta Top with Ballast Door:** Gray Nebula laminate, black edge','**364 – Large Delta Top:** Gray Nebula laminate, black edge','**364S – Large Delta Top with Ballast Door:** Gray Nebula laminate, black edge'],
 install=[TBL_ASM,'**Floor Mounting:** Optional concealed mounting with stud plates; concrete anchors and security Torx bolts are included; see Cortech instructions',
  '**Weighting:** Add sandbags through the ballast door in the base on the 361S, 363S, and 364S; do not use loose sand. Ballast door bit size is T27'],
 apps=apps('The Summit All Purpose Table suits dining and activity areas that want a durable table with a calm, residential look.',
  ['Dining rooms and dayrooms in behavioral healthcare facilities and psychiatric hospitals','Activity and group rooms in residential treatment centers','Other secure settings that serve meals or hold group activities'],END_COLL),
 series=SUMMIT_SERIES,
 mt='Cortech Summit All Purpose Table - 361 / 363 / 364 at Anchortex',
 md='Shop the Cortech Summit All Purpose Table, a dining-height table with a one-piece molded base and a 42” round or delta laminate top, with an optional game top.',
 notes=[SER_SUM,
  'H1: I wrote "All Purpose" without the hyphen, as Cortech does, and took out "Molded Base with Laminate Top" and "Models."',
  'Variant names: your variants are 361S, 363S, and 364S, "with ballast door." The Cortech spec sheet lists 361, 361GT, 363, and 364, with no S models. Can you check the model numbers with Cortech? Your page does not have the 361GT game top as a variant.',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet gives the base (16 lbs) and tops (delta 45 lbs, round 56 lbs) separately, so the tables weigh about 72 lbs (round) and 61 lbs (delta). I used these totals for the worksheet.',
  'Dimensions: the Cortech spec sheet gives one size for the delta top table (44”W×43”D×29”H) and does not give separate sizes for the medium and large delta tops.',
  'Top color: the Cortech spec sheet lists the tops in Gray Nebula with a black edge.',
  TBL_GGN,
  'Concealed mounting: the Cortech concealed mounting instructions show the stud plates, concrete anchors, and security Torx bolts as included. They do not give a model number or say whether the mounting kit is sold separately.',
  'Product images: the page has four images, including a Summit color chart. The Cortech product page has photos of the 42” round table in all 18 base colors. Would you like me to add them?'])

# 7. Sequoia Bed 210
add(tab='210 - Cortech Sequoia Molded Wood Grain Bed',short='210: Cortech Sequoia Molded Wood Grain Bed',
 handle='cortech-210-sequoia-molded-wood-grain-behavioral-health-bed',src=[SEQC+'molded-wood-grain-bed/'],
 specs=[('210',CU+'Sequoia-Bed-spec-sheet.pdf'),('Installation',CU+'Sequoia-Bed-Instructions.pdf')],
 h1='Cortech Sequoia Molded Wood Grain Bed – 210 / 210S2',
 cur_h1='Cortech Sequoia Durable Molded Wood Grain Behavioral Health Bed - 210',
 sub='One-Piece Molded Platform Bed with a Wood Grain Finish, Rounded Edges, and Optional Ballast Doors',
 cur_sub='Cortech 210 Sequoia Behavioral Health Bed with Molded Wood Grain Finish',
 intro=['The **Cortech Sequoia Molded Wood Grain Bed** is a one-piece molded platform bed with a wood grain finish, for patient rooms in behavioral healthcare facilities and other secure settings. It brings the warmth of a residential wood bed with the strength and cleanability of molded polyethylene.',
  'The bed is rotationally molded as a single unit from high impact “no break” polyethylene, and its rounded edges and sloped surfaces help reduce ligature risk. It can be bolted to the floor or weighted with sandbags through optional underside ballast doors.'],
 bullets=['**Material:** One-piece rotationally molded high impact “no break” polyethylene; no steel or wood components',
  '**Dimensions:** 82”L×42”W×18”H',
  '**Weight:** 126 lbs',
  '**Mattress:** Fits a 36”×80” mattress up to 6” thick (sold separately)',
  '**Safety:** Rounded edges and sloped surfaces help reduce ligature risk',
  '**Storage:** No shelves or storage',
  '**Ballast Doors:** Optional underside ballast doors for adding sandbags, secured with tamper-resistant screws; do not use loose sand',
  '**Floor Mounting:** Bolts to the floor with a concealed corner mounting system',
  SEQ_FIN,SEQ_CRAFT,ISO22,FL,SEQ_AWARD,LIFE,ISO],
 models=['**210 – Standard:** Without ballast doors','**210S2 – With Ballast Doors:** Underside ballast doors for adding sandbags'],
 install=['**Floor Mounting:** Mounting brackets, concrete anchors, and security Torx bolts are included; see Cortech instructions',
  '**Ballast Doors:** Add sandbags through the underside ballast doors on the 210S2; do not use loose sand. Hardware bit size is T27'],
 apps=apps('The Sequoia Bed suits patient rooms that want a warm, residential look without giving up safety or durability.',
  ['Patient rooms in behavioral healthcare facilities and psychiatric hospitals','Residential treatment centers and secure treatment programs','Other secure settings that want a residential bedroom'],BED_COLL),
 series=BED_SERIES,
 mt='Cortech Sequoia Molded Wood Grain Bed - 210 at Anchortex',
 md='Shop the Cortech Sequoia Bed, a one-piece molded platform bed with a wood grain finish, rounded edges, and optional ballast doors for behavioral health rooms.',
 notes=[SER_BED,
  'H1: Cortech calls it the Sequoia Molded Wood Grain Platform Bed. I took out "Durable" and "Behavioral Health," and added the 210S2.',
  'Weight: your variants are set to 126 lbs, which matches the Cortech spec sheet.',
  'Finishes: your current page lists four finishes. The Cortech spec sheet also lists Redwood (210RW), so I added it.',
  '210S2: your variant says "2 ballast doors." The Cortech spec sheet says the underside ballast doors are optional but does not give the number of doors or a model number. I kept your 210S2 variant.',
  'Mounting hardware: the Cortech installation instructions say the mounting brackets, concrete anchors, and security Torx bolts are included. Your current page lists a 210KIT bolt-down hardware kit. Is the kit still sold separately?',
  'Award: the Nightingale Award comes from your current page and the Cortech web page.',
  'I left out GREENGUARD Gold, UL 94 HB, and "Patent Pending," since the Cortech spec sheet does not say these.',
  'Product images: the page has five images, including a Sequoia finish chart. The Cortech product page has photos of the bed in all five finishes, including Redwood. Would you like me to add the Redwood photo?'])

# 8. Sequoia Nightstand 215
add(tab='215 - Cortech Sequoia Molded Wood Grain Nightstand',short='215: Cortech Sequoia Molded Wood Grain Nightstand',
 handle='cortech-215-sequoia-molded-wood-grain-night-stand',src=[SEQC+'sequoia-molded-wood-grain-nightstand/'],
 specs=[('215',CU+'Sequoia-Nightstand-Spec-Sheet.pdf'),('Installation',CU+'Sequoia-Nightstand-Instructions.pdf')],
 h1='Cortech Sequoia Molded Wood Grain Nightstand – 215',
 cur_h1='Cortech Sequoia - Night Stand with Wood‑Grain Finish - One‑Piece Molded Construction - Model 215',
 sub='One-Piece Molded Nightstand with a Wood Grain Finish and Rounded Edges, to Match the Sequoia Bed',
 cur_sub='Cortech 215 Sequoia Night Stand with Molded Wood Grain Finish for Behavioral Health Care Facilities',
 intro=['The **Cortech Sequoia Molded Wood Grain Nightstand** is a one-piece molded nightstand with a wood grain finish, for patient rooms in behavioral healthcare facilities and other secure settings. It matches the Sequoia Bed for a warm, residential room.',
  'The nightstand is rotationally molded as a single unit from high impact polyethylene, with no metal or wood components, and its rounded edges and sloped surfaces help reduce ligature risk.'],
 bullets=['**Material:** One-piece rotationally molded high impact polyethylene; no metal or wood components',
  '**Dimensions:** 18”W×16”D×21”H',
  '**Weight:** 26 lbs',
  '**Safety:** Rounded edges and sloped surfaces help reduce ligature risk',
  '**Floor Mounting:** Bolts to the floor',
  SEQ_FIN,SEQ_CRAFT,
  '**Antimicrobial:** Infused with CORx antimicrobial compound',
  FL,SEQ_AWARD,LIFE,ISO],
 models=['**215 – Sequoia Nightstand:** Heritage Oak, Natural Oak, Coastal Driftwood, Walnut, or Redwood'],
 install=['**Floor Mounting:** Bolt to the floor through four holes drilled through the nightstand; see Cortech instructions'],
 apps=apps('The Sequoia Nightstand suits patient rooms that want a warm, residential look to match the Sequoia Bed.',
  ['Patient rooms in behavioral healthcare facilities and psychiatric hospitals','Residential treatment centers and secure treatment programs','Other secure settings that want a residential bedroom'],NIGHT_COLL),
 series=BED_SERIES,
 mt='Cortech Sequoia Molded Wood Grain Nightstand - 215 at Anchortex',
 md='Shop the Cortech Sequoia Nightstand, a one-piece molded nightstand with a wood grain finish and rounded edges, made to match the Sequoia Bed in patient rooms.',
 notes=[SER_BED,
  'H1: Cortech calls it the Sequoia Molded Wood Grain Nightstand. I used that and took out the extra words.',
  'Weight: your variant is set to 29 lbs. The Cortech spec sheet says 26 lbs, so I used 26 lbs.',
  'Variant name: your variant says "215 - Sequoia Night Standard." Would you like it renamed "215 - Sequoia Nightstand"?',
  'Dimensions: the Cortech spec sheet lists 21”H×18”W×16”D, but the drawing on the second page shows about 21.5”, 17.5”, and 22”. I used the listed size.',
  'Ballast doors: the second page of the Cortech spec sheet lists "Options: Ballast doors," but the first page does not, and there is no ballast model. I left it out.',
  'Floor mounting hardware: the Cortech spec sheet says "hardware of your choice," but the installation instructions list four tamper-resistant Torx screws and washers as included. I left the hardware out of the description. Can you check with Cortech?',
  'Finishes: your current page lists four finishes. The Cortech spec sheet also lists Redwood (215RW), so I added it. Your variant has no finish option. How do customers choose a finish?',
  'Collection link: the nightstand is only in your Behavioral Healthcare Anti-Ligature Furniture collection, so I linked that one.',
  'I left out GREENGUARD Gold, UL 94 HB, and "Patent Pending," since the Cortech spec sheet does not say these.',
  'Product images: the page has five images, including a Sequoia finish chart. The Cortech product page has a Redwood nightstand photo. Would you like me to add it?'])

# 9. SafeBin 35
add(tab='35 - Cortech SafeBin Trash Receptacle',short='35: Cortech SafeBin Trash Receptacle',
 handle='cortech-35-safebin-trash-receptacle',src=[FM+'safebin/'],
 specs=[('35',CU+'35-gal-SafeBin-spec-sheet.pdf'),('Installation',CU+'Safebin-Installation-Instructions.pdf')],
 h1='Cortech SafeBin Lockable Trash Receptacle – 35',
 cur_h1='Cortech Safebin Trash Receptacle',
 sub='Lockable Molded Trash Receptacle with a Tamper-Resistant Chute and a 35-Gallon Inner Container',
 cur_sub='Cortech 35BK Safebin Trash Receptacle',
 intro=['The **Cortech SafeBin Lockable Trash Receptacle** is a molded trash receptacle for behavioral healthcare and correctional facilities. Its tamper-resistant waste chute keeps the liner and discarded items out of reach, and an integrated lock with a master key keeps the bin closed.',
  'The SafeBin is rotationally molded without metal hinges, bolts to the floor or wall, and holds a 35-gallon inner container that can be used with or without trash liners. It is rated for outdoor use.'],
 bullets=['**Construction:** Rotationally molded, with no metal hinges',
  '**Capacity:** 35-gallon inner container, for use with or without trash liners',
  '**Waste Chute:** Tamper-resistant chute prevents access to the liner and discarded items',
  '**Lock:** Integrated lock with master key',
  '**Mounting:** Bolts to the floor or wall',
  '**Cleaning:** Slightly sloped bottom interior for easy cleaning and drainage',
  '**Weight:** 115 lbs',
  OUT,
  '**Colors:** Black top with a body in '+COLORS18,
  '**Warranty:** 10-year warranty against manufacturing defects',ISO],
 models=['**35 – SafeBin:** Body color of your choice with a black top'],
 install=['**Floor or Wall Mounting:** Bolt to the floor or wall through four pilot holes; concrete anchors, hex bolts, and washers are included; see Cortech instructions'],
 apps=apps('The SafeBin suits secure areas where staff need to keep trash and liners out of residents’ reach.',
  ['Housing units, dayrooms, common areas and outdoor spaces in correctional facilities and jails','Patient areas in behavioral healthcare facilities and psychiatric hospitals','Kitchens and other secure areas that need a locked trash receptacle'],TRASH_COLL),
 series=SB_SERIES,
 mt='Cortech SafeBin Lockable Trash Receptacle - 35 at Anchortex',
 md='Shop the Cortech SafeBin, a lockable molded trash receptacle with a tamper-resistant chute and a 35-gallon inner container that bolts to the floor or wall.',
 notes=[SER_FM+' I added a "Secure Waste Bins" line for the SafeBin. Would you like it added to the other facilities maintenance pages too?',
  'H1: Cortech writes "SafeBin" with a capital B. I added "Lockable" and the model number 35.',
  'Weight: your variant is set to 115 lbs, which matches the Cortech spec sheet.',
  'Dimensions: the Cortech spec sheet does not give dimensions, so I left them out.',
  'Variant name: your variant is "35_BK - Safebin." Cortech model numbers are 35 plus the body color code plus BK (black top), for example 35AQBK. Your variant has no color option. How do customers choose a body color?',
  'Colors: your current page lists 12 body colors. The Cortech spec sheet lists 18, so I used the Cortech list.',
  'Mounting hardware: the Cortech installation instructions say the concrete anchors, hex bolts, and washers are included.',
  outn('the SafeBin is'),
  'Collection links: the SafeBin is in your Prison Janitorial and Sanitation Supplies and Kitchen and Food Service collections, so I linked those two.',
  'I left out "Patent Pending."',
  'Product images: the page has four images, including a color chart. The Cortech product page has two SafeBin photos (closed and with the door open). Would you like me to add them?'])

# 10. Summit Guest Chair 300
c=chair('300','Guest Chair',False,None,'22”W×23”D×31”H','21 lbs',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet says 21 lbs, so I used 21 lbs.',
  'Product images: the page has five images, including two Summit color charts. The Cortech product page has photos of the Summit Guest Chair in all 18 colors and a dining room photo. Would you like me to add them?')
add(tab='300 - Cortech Summit Guest Chair',short='300 / 300S: Cortech Summit Guest Chair',
 handle='cortech-300-summit-guest-chair',src=[SUMC+'summit-chair/'],
 specs=[('300 / 301',CU+'Summit-Chair-spec-sheet.pdf'),('Bolt-down',CU+'Summit-Chair-Bolt-Down-Installation-Instructions.pdf')],
 h1='Cortech Summit Guest Chair – 300 / 300S',
 cur_h1='Cortech Summit Durable Guest Chair - 300',
 sub='One-Piece Molded Guest Chair with a Residential Look and an Optional Ballast Door',
 cur_sub='Cortech 300 Summit Guest Chair',
 mt='Cortech Summit Molded Guest Chair - 300 / 300S at Anchortex',
 md='Shop the Cortech Summit Guest Chair, a one-piece molded guest chair with a calm, residential look and an optional ballast door, rated for outdoor use.',**c)

# 11. Summit Veldura Guest Chair 301
c=chair('301','Guest Chair',True,None,'22”W×23”D×31”H','21 lbs',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet gives 21 lbs for the Summit Guest Chair and no separate weight for the Veldura version, so I used 21 lbs.',
  'Product images: the page has four images, including two Summit color charts. The Cortech product page has photos of the Summit Veldura Guest Chair in all 18 colors. Would you like me to add them?',
  extra_notes=['SKUs: both of your variants have the same SKU (C601214-01). Should the 301S be C601214-02?',
   'Your current page says "Model 300S has a ballast door." I used 301S, the Veldura model on the Cortech spec sheet.'])
add(tab='301 - Cortech Summit Veldura Guest Chair',short='301 / 301S: Cortech Summit Veldura Guest Chair',
 handle='cortech-301-summit-veldura-guest-chair',src=[SUMC+'summit-veldura-guest-chair/'],
 specs=[('300 / 301',CU+'Summit-Chair-spec-sheet.pdf'),('Bolt-down',CU+'Summit-Chair-Bolt-Down-Installation-Instructions.pdf')],
 h1='Cortech Summit Veldura Guest Chair – 301 / 301S',
 cur_h1='Cortech Summit Veldura Soft-Touch Durable Guest Chair - 301',
 sub='One-Piece Molded Guest Chair with a Veldura Soft-Touch Finish and an Optional Ballast Door',
 cur_sub='Cortech 301 Summit Veldura Guest Chair with Veldura Soft-Touch Exterior',
 mt='Cortech Summit Veldura Guest Chair - 301 / 301S at Anchortex',
 md='Shop the Cortech Summit Veldura Guest Chair. A one-piece molded chair with a Veldura soft-touch finish and an optional ballast door, rated for outdoor use.',**c)

# 12. Summit Veldura Accent Chair 311
c=chair('311','Accent Chair',True,None,'27”W×29”D×29”H','27 lbs',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet gives 27 lbs for the Summit Accent Chair and no separate weight for the Veldura version, so I used 27 lbs.',
  'Product images: the page has four images, including two Summit color charts. The Cortech product page has one more photo (Summit Veldura Accent Chairs in Canvas). Would you like me to add it?')
add(tab='311 - Cortech Summit Veldura Accent Chair',short='311 / 311S: Cortech Summit Veldura Accent Chair',
 handle='cortech-311-summit-veldura-accent-chair',src=[SUMC+'summit-veldura-accent-chair/'],
 specs=[('310 / 311',CU+'Summit-Accent-Chair-spec-sheet.pdf'),('Bolt-down',CU+'Accent-Chair-Bolt-Down-Installation-Instructions.pdf')],
 h1='Cortech Summit Veldura Accent Chair – 311 / 311S',
 cur_h1='Cortech Summit Veldura Soft-Touch Durable Accent Chair - 311',
 sub='One-Piece Molded Accent Chair with a Veldura Soft-Touch Finish and an Optional Ballast Door',
 cur_sub='Cortech 311 Summit Veldura Accent Chair with Veldura Soft-Touch Exterior',
 mt='Cortech Summit Veldura Accent Chair - 311 / 311S at Anchortex',
 md='Shop the Cortech Summit Veldura Accent Chair. A one-piece molded chair with a Veldura soft-touch finish and an optional ballast door, rated for outdoor use.',**c)

# 13. Summit Accent Chair 310
c=chair('310','Accent Chair',False,None,'27”W×29”D×29”H','27 lbs',
  'Weight: your variants are set to 255 lbs, which looks like a placeholder. The Cortech spec sheet says 27 lbs, so I used 27 lbs.',
  'Product images: the page has four images, including two Summit color charts. The Cortech product page has one more photo (Summit Accent Chair in Claylight). Would you like me to add it?')
add(tab='310 - Cortech Summit Accent Chair',short='310 / 310S: Cortech Summit Accent Chair',
 handle='cortech-310-summit-accent-chair',src=[SUMC+'summit-accent-chair/'],
 specs=[('310 / 311',CU+'Summit-Accent-Chair-spec-sheet.pdf'),('Bolt-down',CU+'Accent-Chair-Bolt-Down-Installation-Instructions.pdf')],
 h1='Cortech Summit Accent Chair – 310 / 310S',
 cur_h1='Cortech Summit Durable Accent Chair - 310',
 sub='One-Piece Molded Accent Chair with a Residential Look and an Optional Ballast Door',
 cur_sub='Cortech 310 Summit Accent Chair',
 mt='Cortech Summit Molded Accent Chair - 310 / 310S at Anchortex',
 md='Shop the Cortech Summit Accent Chair. A one-piece molded accent chair with a calm, residential look and an optional ballast door, rated for outdoor use.',**c)
