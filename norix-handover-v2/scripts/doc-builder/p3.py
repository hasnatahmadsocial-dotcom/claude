A='https://www.anchortex.com/products/'
NP='https://norix.com/product/'
U='https://norix.com/wp-content/uploads/'
BH='https://www.anchortex.com/collections/bh-behavioral-healthcare-furniture'
CDF='https://www.anchortex.com/collections/cd-correctional-furniture'
NX='https://www.anchortex.com/collections/norix-furniture'
GG='**Environmental Certification:** GREENGUARD and GREENGUARD Gold'
W10='**Warranty:** 10-year limited replacement warranty'
W5='**Warranty:** 5-year limited replacement warranty'
IND='**Intended Use:** Indoor use only'
USA='**Country of Manufacture:** USA'
S1000='**Static Load Testing:** Tested to 1,000 lbs'
LAMTOP='**Top:** High-pressure laminate over a 45 lb density M3 particle board core, with a 1.5” thick radiused molded edge that is pressure fused to the top'
TNUT='**Top Attachment:** Embedded T-nuts give a steel-to-steel connection between the top and base'
FIN='**Top Finishes:** Titanium Evolve, Wild Cherry, Kensington Maple, Asian Sun, Montana Walnut, Palisades Oak, Calcutta Marble, or Black Alicante laminate with a matching or black molded edge'
GAME='**Game Top:** Titanium Evolve laminate with a printed game board, black molded edge'
DUO='**DuoForm™ Top:** Fused layers of high-impact polyethylene with UV stabilizers, in Cove or Twilight, fastened to the base with rivnuts for a steel-to-steel connection'
SEATC='Twilight, Cove, Sage, Clay, Sand, Dove'
TBL_SERIES=[
('h3','[H2] About Norix Dayroom and Dining Tables'),
('p','Norix tables are made for dayrooms, dining halls, classrooms, and visitation areas in correctional and behavioral healthcare facilities, where furniture is used hard every day. The range covers molded-base tables such as the Jupiter and Molded X-Base, laminate X-Base tables, and steel-base tables such as the Leg Style, Multi-Purpose, Max-Master, and Oasis.'),
('p','Common characteristics of Norix tables include:'),
('b1','**Durable Tops:** High-pressure laminate over a dense particle board core, with molded or T-mold edges depending on the model'),
('b1','**Secure Connections:** Tops attach to the base with tamper-resistant hardware for a solid metal-to-metal connection'),
('b1','**Placement Options:** Depending on the model, tables can be ballasted, bolted to the floor, or set on tamper-resistant glides'),
('b1','**Easy Cleaning:** Smooth surfaces that stand up to routine cleaning in high-traffic areas'),
('b1','**Made in the USA:** Built by Norix in the United States'),
]
BLD_SERIES=[
('h3','[H2] About Norix Boulder Beam Seating'),
('p','Norix Boulder beam seating has been used in lobbies and waiting areas for years. Each unit pairs a powder-coated tubular steel frame with one-piece molded polyethylene seats, so it holds up to heavy public use and is easy to keep clean.'),
('p','Common characteristics of Boulder beam seating include:'),
('b1','**Welded Steel Frame:** Full circumference welds at every joint, with no nuts, bolts, or rivets to loosen over time'),
('b1','**Tamper-Resistant Seats:** Each seat is attached to an 11-gauge steel seat support with nine security screws'),
('b1','**Seamless Seats:** One-piece seat and back that does not absorb fluids'),
('b1','**Easy Cleaning:** Seats can be cleaned with bleach solutions and hospital-grade disinfectants'),
('b1','**TruColor™ Technology:** Fully compounded color for consistent color and durability'),
]
NXF=('Norix manufactures durable furniture for demanding environments, including behavioral healthcare facilities, psychiatric hospitals, correctional institutions, and residential treatment centers. Explore the full line of [Norix Furniture]('+NX+') at Anchortex.')
def apps(intro,seating=False):
    L=[('h3','[H2] Applications'),('p',intro),('p','Typical applications include:')]
    if seating: L+=[('b1','Lobbies, waiting rooms, and intake areas'),('b1','Correctional and detention facilities'),('b1','Behavioral healthcare facilities and psychiatric hospitals')]
    else: L+=[('b1','Dayrooms and dining halls in correctional and detention facilities'),('b1','Behavioral healthcare facilities and psychiatric hospitals'),('b1','Visitation areas, classrooms, and other common areas')]
    L.append(('p',f"Explore Anchortex's [Behavioral Healthcare Anti-Ligature Furniture]({BH}) and [Prison and Detention Furniture]({CDF}) collections for more institutional furniture."))
    return L
SER_NOTE_T='New series section: these tables are a new product group, so I wrote an "About Norix Dayroom and Dining Tables" section based on the Norix Tables Guide. It has no links to individual products. It is the same on all 18 table tabs, so please review it on the Jupiter Round Table tab.'
SER_REF_T='Series section: this is the same "About Norix Dayroom and Dining Tables" section as the Jupiter Round Table tab. Any changes you make there will be applied here too.'
P=[]
def add(**k): P.append(k)
# ---------- BOULDER ----------
add(tab='C212 - Boulder Armless Beam Seating',short='C212: Boulder Armless Beam Seating',
 handle='norix-c212-boulder-beam-seating-with-end-and-divider-arms',src=NP+'boulder/',
 specs=[('C212',U+'2025/08/C212-Boulder-Armless-Beam-Seating.pdf')],
 h1='Norix Boulder Armless Beam Seats – C212',cur_h1='Norix Boulder Durable Armless Beam Seats - C212',
 sub='Steel-Frame Beam Seating with Molded Seats for 2, 3, or 4 People in Lobbies and Waiting Areas',
 cur_sub='Norix Furniture C212-2, C212-3, C212-4 Boulder Beam Seating Bench without Arms',
 intro=['**Norix Boulder Armless Beam Seats** give lobbies and waiting areas sturdy in-line seating for two, three, or four people. The frame is bent and welded tubular steel, and each seat sits on its own welded steel plate, so the unit stays solid under heavy daily use.',
  'Each one-piece seat and back is rotationally molded from high-impact polyethylene and fastened to the frame through molded-in threaded steel inserts, which makes the seats hard to tamper with. The smooth surface resists blood, urine, feces, vinegar, salt solution, and chlorine solution, and it can be cleaned with bleach solutions and hospital-grade disinfectants.'],
 bullets=['**Frame:** 2” diameter, 14-gauge tubular steel, powder coated black, with 11-gauge steel seat supports','**Seats:** One-piece rotationally molded high-impact polyethylene seat and back with UV stabilizers','**Seat Dimensions:** 17” W × 16” D, 18” seat height','**Overall Dimensions:** 25” D × 31.4” H; width depends on the number of seats','**Seat Colors:** '+SEATC,'**Frame Color:** Black',S1000,'**Flammability Standards:** California Technical Bulletin 133, UL 1056, ASTM E1537, and NFPA 261',GG,W10,IND,USA],
 models=['**C212-2 – 2 Seats:** 44” W, 81 lbs','**C212-3 – 3 Seats:** 65” W, 110 lbs','**C212-4 – 4 Seats:** 86” W, 145 lbs'],
 install=['**Free-Standing or Bolt-Down:** Use free-standing on glides or bolt to the floor. Floor mounting hardware is included.','**Assembly:** None required'],
 apps=apps('Boulder Armless Beam Seats suit lobbies and waiting areas that need durable, easy-to-clean seating for several people at once.',True),series=BLD_SERIES,
 mt='Norix Boulder Armless Beam Seats - C212 at Anchortex',
 md='Shop Norix Boulder C212 armless beam seats. Welded steel frame with tamper-resistant molded seats for 2, 3, or 4 people in lobbies and waiting areas.',
 notes=['New series section: I wrote an "About Norix Boulder Beam Seating" section from the Norix Boulder page. It has no links to individual products and is the same on the C212 and C213 tabs.',
  'H1: the current H1 says "Durable." I removed it and changed the hyphen before the model number to an en dash.',
  'URL: the product URL ends in "with-end-and-divider-arms," but this is the armless model. I did not change the URL.',
  'Weights: all three variants are set to 255 lbs. Accurate weights are 81 lbs (C212-2), 110 lbs (C212-3), and 145 lbs (C212-4).',
  'Product images: the last image is named "Norix_Vesta_Colors." Please check that it shows the Boulder seat colors.'])
add(tab='C213 - Boulder Beam Seating with End Arms',short='C213: Boulder Beam Seating with End Arms',
 handle='norix-c213-boulder-beam-seating-with-end-arms',src=NP+'boulder/',
 specs=[('C213',U+'2025/08/C213-Boulder-End-Arm-Beam-Seating.pdf')],
 h1='Norix Boulder Beam Seating with End Arms – C213',cur_h1='Norix Boulder Durable Beam Seating with End Arms - C213',
 sub='Steel-Frame Beam Seating with End Arms and Molded Seats for 2, 3, or 4 People',
 cur_sub='Norix Furniture C213-2, C213-3, C213-4 Boulder Beam Seating Benches with End Arms on Sides',
 intro=['**Norix Boulder Beam Seating with End Arms** gives lobbies and waiting areas in-line seating for two, three, or four people, with an arm at each end of the bench. The frame is bent and welded tubular steel, and each seat sits on its own welded steel plate, so the unit stays solid under heavy daily use.',
  'Each one-piece seat and back is rotationally molded from high-impact polyethylene and fastened to the frame through molded-in threaded steel inserts, which makes the seats hard to tamper with. The smooth surface resists blood, urine, feces, vinegar, salt solution, and chlorine solution, and it can be cleaned with bleach solutions and hospital-grade disinfectants.'],
 bullets=['**Frame:** 2” diameter, 14-gauge tubular steel, powder coated black, with 11-gauge steel seat supports','**Seats:** One-piece rotationally molded high-impact polyethylene seat and back with UV stabilizers','**Seat Dimensions:** 17” W × 16” D, 18” seat height','**Arm Height:** 24”','**Overall Dimensions:** 25” D × 31.4” H; width depends on the number of seats','**Seat Colors:** '+SEATC,'**Frame Color:** Black',S1000,'**Flammability Standards:** California Technical Bulletin 133, UL 1056, ASTM E1537, and NFPA 261',GG,W10,IND,USA],
 models=['**C213-2 – 2 Seats:** 44” W, 87 lbs','**C213-3 – 3 Seats:** 65” W, 118 lbs','**C213-4 – 4 Seats:** 86” W, 153 lbs'],
 install=['**Free-Standing or Bolt-Down:** Use free-standing on glides or bolt to the floor. Floor mounting hardware is included.','**Assembly:** None required'],
 apps=apps('Boulder Beam Seating with End Arms suits lobbies and waiting areas where people need arm support getting in and out of their seats.',True),series=BLD_SERIES,
 mt='Norix Boulder Beam Seating with End Arms - C213 at Anchortex',
 md='Shop Norix Boulder C213 beam seating with end arms. Welded steel frame and tamper-resistant molded seats for 2, 3, or 4 people in lobbies and waiting areas.',
 notes=['Series section: this is the same "About Norix Boulder Beam Seating" section as the C212 tab. Any changes you make there will be applied here too.',
  'H1: the current H1 says "Durable." I removed it and changed the hyphen before the model number to an en dash.',
  'Width: your current description says the C213-3 is 86” wide. The spec sheet and price list both say 65”, so I used 65”.',
  'Weights: all three variants are set to 255 lbs. Accurate weights are 87 lbs (C213-2), 118 lbs (C213-3), and 153 lbs (C213-4).',
  'Product images: the last image is named "Norix_Flux_Colors." Please check that it shows the Boulder seat colors.'])
# ---------- JUPITER ----------
JUP_INTRO2='The base is rotationally molded from high-impact polyethylene with UV stabilizers and has a lightly textured surface that is easy to clean with bleach solutions and hospital-grade disinfectants. The cylinder base is made to be weighted on site with up to 200 lbs of dry sand or gravel, or Norix can ballast it at the factory. Ballast or a bolt-down kit is required to validate the warranty.'
add(tab='CY3600 / CY4200 / CY4800 - Jupiter Round Table',short='CY3600 / CY4200 / CY4800: Jupiter Round Table',
 handle='norix-jupiter-round-top-table-w-cylinder-base',src=NP+'jupiter/',
 specs=[('CY3600 / CY4200 / CY4800',U+'2024/12/CY3600CY3636CY4200CY4242CY4800-Jupiter-Table.pdf')],
 h1='Norix Jupiter Cylinder Base Table with Round Top – CY3600 / CY4200 / CY4800',cur_h1='Norix Jupiter Durable Cylinder Base Table with Round Top',
 sub='Ballasted Molded Cylinder Base Table with Laminate or Game Top for Dayrooms and Dining Areas',
 cur_sub='Norix Furniture CY3600, CY4200, CY4800 - Jupiter Round Top Table with Cylinder Base',
 intro=['The **Norix Jupiter Cylinder Base Table with Round Top** pairs a molded polyethylene cylinder base with a high-pressure laminate top, for dayrooms, dining areas, and classrooms in correctional and behavioral healthcare facilities. It comes in 36”, 42”, and 48” round sizes, with a solid laminate top or a game top.',JUP_INTRO2],
 bullets=['**Base:** Rotationally molded high-impact polyethylene cylinder with UV stabilizers, color Raven',LAMTOP,TNUT,'**Top Sizes:** 36”, 42”, or 48” round','**Height:** 29.3”','**Weight:** 68 to 103 lbs, depending on size (without ballast)',FIN,GAME,S1000,'**Flammability Standards:** California Technical Bulletin 133, UL 1056, and ASTM E1537',GG,W10,IND,USA],
 models=['**CY3600 – 36” Round:** Solid top or game top, 68 lbs','**CY4200 – 42” Round:** Solid top or game top, 82 lbs','**CY4800 – 48” Round:** Solid top or game top, 103 lbs'],
 install=['**Ballasting:** Fill the base on site with up to 200 lbs of dry sand or gravel (not supplied), or order factory ballasting. Ballast or a bolt-down kit is required to validate the warranty.','**Assembly:** Some assembly required; see the Norix instructions'],
 apps=apps('The Norix Jupiter Round Table suits dayrooms and dining areas that need a heavy, stable table that can still be moved when the room layout changes.'),series=TBL_SERIES,
 mt='Norix Jupiter Round Cylinder Base Table at Anchortex',
 md='Shop the Norix Jupiter round table with molded cylinder base. 36, 42, or 48 inch laminate or game top, ballasted for dayrooms and dining areas.',
 notes=[SER_NOTE_T,
  'H1: the current H1 says "Durable" and has no model numbers. I removed "Durable" and added the three model numbers.',
  'Meta title: all three model numbers would make it longer than 65 characters, so I left them out of the meta title.',
  'Weights: all six variants are set to 255 lbs. Accurate weights are 68 lbs (CY3600), 82 lbs (CY4200), and 103 lbs (CY4800). The game top versions weigh the same as the solid tops.'])
add(tab='CY3636 / CY4242 - Jupiter Square Table',short='CY3636 / CY4242: Jupiter Square Table',
 handle='norix-jupiter-square-top-table-w-cylinder-base',src=NP+'jupiter/',
 specs=[('CY3636 / CY4242',U+'2024/12/CY3600CY3636CY4200CY4242CY4800-Jupiter-Table.pdf'),('CY4242-DF',U+'2025/04/CY4242-DF-Jupiter-Table-DuoForm-Top.pdf')],
 h1='Norix Jupiter Cylinder Base Table with Square Top – CY3636 / CY4242',cur_h1='Norix Jupiter Durable Cylinder Base Table with Square Top',
 sub='Ballasted Molded Cylinder Base Table with Laminate, Game, or DuoForm Top for Dayrooms and Dining Areas',
 cur_sub='Norix Furniture CY3636, CY4242 - Jupiter Square Top Table with Cylinder Base, CY4242-DF Jupiter Table with DuoForm Top',
 intro=['The **Norix Jupiter Cylinder Base Table with Square Top** pairs a molded polyethylene cylinder base with a square top, for dayrooms, dining areas, and classrooms in correctional and behavioral healthcare facilities. It comes in 36” and 42” square sizes with a laminate solid top or game top. The 42” size is also available with a molded DuoForm™ top.',JUP_INTRO2],
 bullets=['**Base:** Rotationally molded high-impact polyethylene cylinder with UV stabilizers, color Raven',LAMTOP,TNUT,DUO,'**Top Sizes:** 36” or 42” square','**Height:** 29.3” (29.5” with DuoForm™ top)','**Weight:** 45 to 99 lbs, depending on size and top (without ballast)',FIN,GAME,S1000,'**Flammability Standards:** California Technical Bulletin 133, UL 1056, and ASTM E1537',GG,'**Warranty:** 10-year limited replacement warranty (5 years for the DuoForm™ top)',IND,USA],
 models=['**CY3636 – 36” Square:** Laminate solid top or game top, 80 lbs','**CY4242 – 42” Square:** Laminate solid top or game top, 99 lbs','**CY4242-DF – 42” Square DuoForm™:** Molded polyethylene top, 45 lbs'],
 install=['**Ballasting:** Fill the base on site with up to 200 lbs of dry sand or gravel (not supplied), or order factory ballasting. Ballast or a bolt-down kit is required to validate the warranty.','**Concealment Plate:** Optional for the DuoForm™ model','**Assembly:** Some assembly required; see the Norix instructions'],
 apps=apps('The Norix Jupiter Square Table suits dayrooms and dining areas that need a heavy, stable table that can still be moved when the room layout changes.'),series=TBL_SERIES,
 mt='Norix Jupiter Square Cylinder Base Table - CY3636 / CY4242',
 md='Shop the Norix Jupiter square table with molded cylinder base. 36 or 42 inch laminate, game, or DuoForm top, ballasted for dayrooms and dining areas.',
 notes=[SER_REF_T,
  'H1: the current H1 says "Durable" and has no model numbers. I removed "Durable" and added the model numbers.',
  'Meta title: adding "at Anchortex" would make it more than 65 characters, so I left it off.',
  'Price: the CY4242-DF DuoForm variant is $1,760. The Norix list price is $1,200, so at your usual 80% of list it would be $960. Can you check this price?',
  'DuoForm warranty: the DuoForm top has a 5-year warranty, not 10 years, so I listed it separately.',
  'Indoor use: the Norix price list says the DuoForm top is weather and UV resistant and suits outdoor spaces, but the DuoForm spec sheet says indoor use only. I followed the spec sheet.',
  'Weights: all five variants are set to 255 lbs. Accurate weights are 80 lbs (CY3636), 99 lbs (CY4242), and 45 lbs (CY4242-DF). The game top versions weigh the same as the solid tops.'])
# ---------- X-BASE ----------
LXB_BASE='**Base:** Two interlocking panels of 1-5/8” thick, 45 lb density particle board, faced on both sides with high-pressure laminate and banded with heavy-duty T-molding that is glued and steel pinned every 12”'
LXB_INTRO2='The base is made from two interlocking laminate panels joined to the top with an intermediate mounting plate. The top is high-pressure laminate over a dense particle board core with a radiused molded edge, attached through embedded T-nuts for a steel-to-steel connection. No installation is needed.'
add(tab='XB3600 / XB4200 / XB4800 - X-Base Round Table',short='XB3600 / XB4200 / XB4800: Laminate X-Base Round Table',
 handle='norix-laminate-x-base-table-with-round-top',src=NP+'x-base/',
 specs=[('XB3600 / XB4200 / XB4800',U+'2024/12/XB3600XB3636XB4200XB4242XB4800-X-Base-Table.pdf')],
 h1='Norix Laminate X-Base Table with Round Top – XB3600 / XB4200 / XB4800',cur_h1='Norix Durable Laminate X-Base Table with Round Top',
 sub='Round Laminate Table with Interlocking X-Base That Defines Each Seating Position',
 cur_sub='Norix Furniture XB3600, XB4200, XB4800 Round Top Table with X-Base',
 intro=['The **Norix Laminate X-Base Table with Round Top** uses an X-shaped base to give each person a defined space at the table, which helps in dayrooms and dining areas in correctional and behavioral healthcare facilities. It comes in 36”, 42”, and 48” round sizes, with a solid laminate top or a game top.',LXB_INTRO2],
 bullets=[LXB_BASE,LAMTOP,TNUT,'**Top Sizes:** 36”, 42”, or 48” round','**Height:** 29.3”','**Weight:** 126 to 164 lbs, depending on size',FIN,GAME,S1000,GG,W10,IND,USA],
 models=['**XB3600 – 36” Round:** Solid top or game top, 126 lbs','**XB4200 – 42” Round:** Solid top or game top, 142 lbs','**XB4800 – 48” Round:** Solid top or game top, 164 lbs'],
 install=['**Installation:** None required','**Optional Top:** 1-1/4” thick laminate top with black vinyl T-mold edge','**Assembly:** See the Norix instructions'],
 apps=apps('The Norix Laminate X-Base Round Table suits dayrooms and dining areas where a defined place for each person helps keep order at the table.'),series=TBL_SERIES,
 mt='Norix Laminate X-Base Table with Round Top at Anchortex',
 md='Shop the Norix laminate X-Base table with round top. 36, 42, or 48 inch solid or game top with an X-base that defines each seat, for dayrooms and dining.',
 notes=[SER_REF_T,
  'H1: the current H1 says "Durable" and has no model numbers. I removed "Durable" and added the model numbers.',
  'Meta title: the model numbers would make it longer than 65 characters, so I left them out.',
  'Variant names: the round tables are named "XB3600 - 36x36," "XB4200 - 42x42," and "XB4800 - 48x48." These are round tops, so they should be "36” Round," "42” Round," and "48” Round." Would you like them renamed?',
  'Weights: all six variants are set to 255 lbs. Accurate weights are 126 lbs (XB3600), 142 lbs (XB4200), and 164 lbs (XB4800). The game top versions weigh the same as the solid tops.'])
add(tab='XB3636 / XB4242 - Laminate X-Base Square Table',short='XB3636 / XB4242: Laminate X-Base Square Table',
 handle='norix-laminate-x-base-table-with-square-top',src=NP+'x-base/',
 specs=[('XB3636 / XB4242',U+'2024/12/XB3600XB3636XB4200XB4242XB4800-X-Base-Table.pdf')],
 h1='Norix Laminate X-Base Table with Square Top – XB3636 / XB4242',cur_h1='Norix - X‑Base Table with Square Top - High‑Pressure Laminate Surface and X Base - Models XB3636 / XB4242',
 sub='Square Laminate Table with Interlocking X-Base That Defines Each Seating Position',
 cur_sub='Norix Furniture XB3636, XB4242 Square Top Table with X-Base',
 intro=['The **Norix Laminate X-Base Table with Square Top** uses an X-shaped base to give each person a defined space at the table, which helps in dayrooms and dining areas in correctional and behavioral healthcare facilities. It comes in 36” and 42” square sizes, with a solid laminate top or a game top.',LXB_INTRO2],
 bullets=[LXB_BASE,LAMTOP,TNUT,'**Top Sizes:** 36” or 42” square','**Height:** 29.3”','**Weight:** 139 lbs (36”) or 162 lbs (42”)',FIN,GAME,S1000,GG,W10,IND,USA],
 models=['**XB3636 – 36” Square:** Solid top or game top, 139 lbs','**XB4242 – 42” Square:** Solid top or game top, 162 lbs'],
 install=['**Installation:** None required','**Optional Top:** 1-1/4” thick laminate top with black vinyl T-mold edge','**Assembly:** See the Norix instructions'],
 apps=apps('The Norix Laminate X-Base Square Table suits dayrooms and dining areas where a defined place for each person helps keep order at the table.'),series=TBL_SERIES,
 mt='Norix Laminate X-Base Square Table - XB3636 / XB4242 at Anchortex',
 md='Shop the Norix XB3636 / XB4242 laminate X-Base table with square top. Solid or game top with an X-base that defines each seat, for dayrooms and dining.',
 notes=[SER_REF_T,
  'H1: the current H1 has extra dashes, "Models," and a long description. I used the same format as the other table pages.',
  'Weights: all four variants are set to 255 lbs. Accurate weights are 139 lbs (XB3636) and 162 lbs (XB4242). The game top versions weigh the same as the solid tops.'])
MXB_BASE='**Base:** Rotationally molded high-impact polyethylene X-base with UV stabilizers and a lightly textured surface, with fully concealed hardware'
MXB_INTRO2='The molded base resists blood, urine, feces, vinegar, salt solution, and chlorine solution, and it can be cleaned with bleach solutions and hospital-grade disinfectants. The X shape gives each person a defined space, which helps reduce kicking and passing contraband under the table. The base must be bolted down or ballasted with about 150 lbs of dry sand or gravel to validate the warranty.'
add(tab='XB4200-MA / XB4800-MA - Molded X-Base Round Table',short='XB4200-MA / XB4800-MA: Molded X-Base Round Table',
 handle='norix-molded-x-base-table-with-round-top',src=NP+'x-base/',
 specs=[('XB4200-MA / XB4800-MA',U+'2024/12/XBXXXX-MA-Molded-X-Base-Table.pdf')],
 h1='Norix Molded X-Base Table with Round Top – XB4200-MA / XB4800-MA',cur_h1='Norix - X‑Base Table with Round Top - High‑Pressure Laminate Surface and X Base - Models XB3600, XB4200, XB4800',
 sub='Round Laminate Table with Molded Polyethylene X-Base and Concealed Hardware for Secure Settings',
 cur_sub='Norix Furniture XB3600, XB4200, XB4800 Round Top Table with X-Base',
 intro=['The **Norix Molded X-Base Table with Round Top** combines a rotationally molded polyethylene X-base with a high-pressure laminate top, for dayrooms and dining areas in correctional and behavioral healthcare facilities. It comes in 42” and 48” round sizes, with a solid laminate top or a game top.',MXB_INTRO2],
 bullets=[MXB_BASE,LAMTOP,TNUT,'**Top Sizes:** 42” or 48” round','**Height:** 31.1”','**Weight:** 100 lbs (42”) or 118 lbs (48”), without ballast',FIN,GAME,S1000,'**Flammability Standards:** California Technical Bulletin 133 and ASTM E1537',GG,W10,IND,USA],
 models=['**XB4200-MA – 42” Round:** Solid top or game top, 100 lbs','**XB4800-MA – 48” Round:** Solid top or game top, 118 lbs'],
 install=['**Ballasting or Bolt-Down:** Ballast with about 150 lbs of dry sand or gravel (not supplied), order factory ballasting, or use the bolt-down option. One of these is required to validate the warranty.','**Assembly:** See the Norix instructions'],
 apps=apps('The Norix Molded X-Base Round Table suits dayrooms and dining areas where concealed hardware and a defined place for each person help keep the room secure.'),series=TBL_SERIES,
 mt='Norix Molded X-Base Round Table - XB4200-MA / XB4800-MA',
 md='Shop the Norix molded X-Base table with round top. 42 or 48 inch laminate or game top on a molded base with concealed hardware for dayrooms and dining.',
 notes=[SER_REF_T,
  'H1: the current H1 says "High-Pressure Laminate Surface and X Base" and lists the XB3600, which is not made with a molded base. I used "Molded X-Base" and the Norix model numbers XB4200-MA and XB4800-MA. Your current subtitle also lists the XB3600.',
  'Meta title: adding "at Anchortex" would make it more than 65 characters, so I left it off.',
  'SKUs: all four variants use the same SKU, N700283. Should each variant have its own SKU?',
  'Ballast: the spec sheet says to ballast with 150 lbs but also says the base holds up to 200 lbs, so I wrote "about 150 lbs."',
  'Weights: all four variants are set to 255 lbs. Accurate weights are 100 lbs (XB4200-MA) and 118 lbs (XB4800-MA). The game top versions weigh the same as the solid tops.'])
add(tab='XB3636-MA / XB4242-MA - Molded X-Base Square',short='XB3636-MA / XB4242-MA: Molded X-Base Square Table',
 handle='norix-molded-x-base-table-with-square-top',src=NP+'x-base/',
 specs=[('XB3636-MA / XB4242-MA',U+'2024/12/XBXXXX-MA-Molded-X-Base-Table.pdf'),('XB4242-DF',U+'2025/04/XB4242-DF-Molded-X-Base-Table-DuoForm-Top.pdf')],
 h1='Norix Molded X-Base Table with Square Top – XB3636-MA / XB4242-MA',cur_h1='Norix Durable Molded X-Base Table with Square Top',
 sub='Square Table with Molded Polyethylene X-Base and Laminate, Game, or DuoForm Top for Secure Settings',
 cur_sub='Norix Furniture XB3636, XB4242 Square Top Table with Molded X-Base - Standard Top or DuoForm Top',
 intro=['The **Norix Molded X-Base Table with Square Top** combines a rotationally molded polyethylene X-base with a square top, for dayrooms and dining areas in correctional and behavioral healthcare facilities. It comes in 36” and 42” square sizes with a laminate solid top or game top. The 42” size is also available with a molded DuoForm™ top.',MXB_INTRO2],
 bullets=[MXB_BASE,LAMTOP,TNUT,DUO,'**Top Sizes:** 36” or 42” square','**Height:** 31.1” (31.3” with DuoForm™ top)','**Weight:** 66 to 116 lbs, depending on size and top (without ballast)',FIN,GAME,S1000,'**Flammability Standards:** California Technical Bulletin 133 and ASTM E1537',GG,'**Warranty:** 10-year limited replacement warranty (5 years for the DuoForm™ top)',IND,USA],
 models=['**XB3636-MA – 36” Square:** Laminate solid top or game top, 97 lbs','**XB4242-MA – 42” Square:** Laminate solid top or game top, 116 lbs','**XB4242-DF – 42” Square DuoForm™:** Molded polyethylene top, 66 lbs'],
 install=['**Ballasting or Bolt-Down:** Ballast with about 150 lbs of dry sand or gravel (not supplied), order factory ballasting, or use the bolt-down option. One of these is required to validate the warranty.','**Assembly:** See the Norix instructions'],
 apps=apps('The Norix Molded X-Base Square Table suits dayrooms and dining areas where concealed hardware and a defined place for each person help keep the room secure.'),series=TBL_SERIES,
 mt='Norix Molded X-Base Square Table - XB3636-MA / XB4242-MA',
 md='Shop the Norix molded X-Base table with square top. 36 or 42 inch laminate, game, or DuoForm top on a molded base with concealed hardware for dayrooms.',
 notes=[SER_REF_T,
  'H1: the current H1 says "Durable" and has no model numbers. I removed "Durable" and added the Norix model numbers.',
  'Meta title: adding "at Anchortex" would make it more than 65 characters, so I left it off.',
  'Prices: all five variants are priced at $0.00. Norix list prices are $1,750 (36” solid), $2,037 (36” game), $1,900 (42” solid), $2,187 (42” game), and $1,700 (42” DuoForm). At your usual 80% of list, they would be $1,400, $1,629.60, $1,520, $1,749.60, and $1,360. Can you confirm the prices?',
  'SKUs: all five variants use the same SKU, N700280. Should each variant have its own SKU?',
  'DuoForm warranty: the DuoForm top has a 5-year warranty, not 10 years, so I listed it separately.',
  'Weights: all five variants are set to 255 lbs. Accurate weights are 97 lbs (XB3636-MA), 116 lbs (XB4242-MA), and 66 lbs (XB4242-DF). The game top versions weigh the same as the solid tops.'])
# ---------- LEG STYLE ----------
LS_LEGS='**Legs:** 4” or 2-1/2” diameter, 14-gauge steel tubing welded to a 6” × 6” × 1/4” steel mounting plate, with tamper-resistant adjustable leveling glides'
LS_INTRO2='Each leg is steel tubing welded to a steel mounting plate and fastened to the top with tamper-resistant screws and embedded T-nuts, for a steel-to-steel connection. The radiused molded edge is permanently fused to the top, which makes it comfortable and well suited to food service. Legs come with tamper-resistant floor glides, and bolt-down is available.'
LS_COLORS='**Leg Colors:** Black or metallic silver'
LS_INST=['**Glides or Bolt-Down:** Tamper-resistant leveling glides are standard. Bolt-down is optional, with hardware included.','**Assembly:** See the Norix instructions']
add(tab='LS3072 / LS3096 - Leg Style Rectangle Table',short='LS3072 / LS3096: Leg Style Rectangle Table',
 handle='norix-leg-style-rectangle-table',src=NP+'leg-style/',
 specs=[('LS3072 / LS3096',U+'2024/12/LS3072LS3096LS3636LS4242LS4800-Leg-Style-Table.pdf')],
 h1='Norix Leg Style Table with Rectangle Top – LS3072 / LS3096',cur_h1='Norix - Rectangle Table with Steel Legs - Laminated Top - Models LS3072 / LS3096',
 sub='Rectangle Laminate Table with Welded Steel Legs for Dining Halls, Dayrooms, and Classrooms',
 cur_sub='Norix Furniture LS3072, LS3096 - Rectangle Table with Legs',
 intro=['The **Norix Leg Style Table with Rectangle Top** is a four-leg laminate table built for continuous daily use in dining halls, dayrooms, and classrooms in correctional and behavioral healthcare facilities. It comes in 30” × 72” and 30” × 96” sizes, with 4” legs or 2-1/2” legs for a more residential look.',LS_INTRO2],
 bullets=[LS_LEGS,LAMTOP,'**Top Sizes:** 30” × 72” or 30” × 96”','**Height:** 29”','**Weight:** 124 to 142 lbs (LS3072) or 166 to 190 lbs (LS3096), depending on leg size',FIN,LS_COLORS,S1000,GG,W10,IND,USA],
 models=['**LS3072 – 30” × 72”:** Solid top, up to 142 lbs','**LS3096 – 30” × 96”:** Solid top, up to 190 lbs'],
 install=LS_INST,
 apps=apps('The Norix Leg Style Rectangle Table suits dining halls and dayrooms that need long tables for group seating.'),series=TBL_SERIES,
 mt='Norix Leg Style Table with Rectangle Top - LS3072 / LS3096',
 md='Shop the Norix LS3072 / LS3096 Leg Style rectangle table. Laminate top with molded edge on welded steel legs, with glides or bolt-down, for dining halls.',
 notes=[SER_REF_T,
  'H1: the current H1 has extra dashes and "Models." I used the same format as the other table pages.',
  'Meta title: adding "at Anchortex" would make it more than 65 characters, so I left it off.',
  'Weights: the spec sheet gives a weight range for each size, which depends on the leg size. Both variants are set to 255 lbs. I suggest the upper weights, 142 lbs (LS3072) and 190 lbs (LS3096), which match your current page.',
  'Variant names: the variants are named "30x72 Solid Top" and "30x96 Solid Top" with no model number. Would you like "LS3072 - 30x72 Solid Top" and "LS3096 - 30x96 Solid Top"?'])
add(tab='LS4800 - Leg Style Round Table',short='LS4800: Leg Style Round Table',
 handle='norix-round-top-leg-style-table',src=NP+'leg-style/',
 specs=[('LS4800',U+'2024/12/LS3072LS3096LS3636LS4242LS4800-Leg-Style-Table.pdf')],
 h1='Norix Leg Style Table with Round Top – LS4800',cur_h1='Norix - Round‑Top Table with Embedded Legs - Tamper Resistant - Model LS4800',
 sub='48” Round Laminate Table with Welded Steel Legs and Solid or Game Top',
 cur_sub='Norix Furniture LS4800 Round Table with Legs',
 intro=['The **Norix Leg Style Table with Round Top** is a 48” round, four-leg laminate table built for continuous daily use in dayrooms, dining areas, and classrooms in correctional and behavioral healthcare facilities. It comes with a solid laminate top or a game top, and 4” legs or 2-1/2” legs for a more residential look.',LS_INTRO2],
 bullets=[LS_LEGS,LAMTOP,'**Top Size:** 48” round','**Height:** 29”','**Weight:** 122 to 138 lbs, depending on leg size',FIN,GAME,LS_COLORS,S1000,GG,W10,IND,USA],
 models=['**LS4800 – 48” Round:** Solid top or game top, up to 138 lbs'],
 install=LS_INST,
 apps=apps('The Norix Leg Style Round Table suits dayrooms and dining areas that need a durable table for group activities and meals.'),series=TBL_SERIES,
 mt='Norix Leg Style Table with Round Top - LS4800 at Anchortex',
 md='Shop the Norix LS4800 Leg Style round table. 48 inch laminate solid or game top on welded steel legs, with glides or bolt-down, for dayrooms and dining.',
 notes=[SER_REF_T,
  'H1: the current H1 has extra dashes, "Embedded Legs," and "Model." I used the same format as the other table pages.',
  'Weights: the spec sheet gives 122 to 138 lbs, depending on the leg size. Both variants are set to 255 lbs. I suggest 138 lbs, which matches your current page and the price list.'])
add(tab='LS3636 / LS4242 - Leg Style Square Table',short='LS3636 / LS4242: Leg Style Square Table',
 handle='norix-square-top-leg-style-table',src=NP+'leg-style/',
 specs=[('LS3636 / LS4242',U+'2024/12/LS3072LS3096LS3636LS4242LS4800-Leg-Style-Table.pdf')],
 h1='Norix Leg Style Table with Square Top – LS3636 / LS4242',cur_h1='Norix - Leg‑Style Table with Square‑Top - Steel Leg Design - Models LS3636 / LS4242',
 sub='Square Laminate Table with Welded Steel Legs and Solid or Game Top',
 cur_sub='Norix Furniture LS3636, LS4242 Square Table with Legs',
 intro=['The **Norix Leg Style Table with Square Top** is a four-leg laminate table built for continuous daily use in dayrooms, dining areas, and classrooms in correctional and behavioral healthcare facilities. It comes in 36” and 42” square sizes with a solid laminate top or a game top, and 4” legs or 2-1/2” legs for a more residential look.',LS_INTRO2],
 bullets=[LS_LEGS,LAMTOP,'**Top Sizes:** 36” or 42” square','**Height:** 29”','**Weight:** 107 to 115 lbs (LS3636) or 121 to 137 lbs (LS4242), depending on leg size',FIN,GAME,LS_COLORS,S1000,GG,W10,IND,USA],
 models=['**LS3636 – 36” Square:** Solid top or game top, up to 115 lbs','**LS4242 – 42” Square:** Solid top or game top, up to 137 lbs'],
 install=LS_INST,
 apps=apps('The Norix Leg Style Square Table suits dayrooms and dining areas that need a durable table for small groups.'),series=TBL_SERIES,
 mt='Norix Leg Style Square Table - LS3636 / LS4242 at Anchortex',
 md='Shop the Norix LS3636 / LS4242 Leg Style square table. Laminate solid or game top on welded steel legs, with glides or bolt-down, for dayrooms and dining.',
 notes=[SER_REF_T,
  'H1: the current H1 has extra dashes, "Steel Leg Design," and "Models." I used the same format as the other table pages.',
  'Weights: the spec sheet gives a weight range for each size, which depends on the leg size. All four variants are set to 255 lbs. I suggest the upper weights, 115 lbs (LS3636) and 137 lbs (LS4242), which match your current page and the price list.',
  'Variant names: these variants say "Plain Top," while the other Leg Style pages say "Solid Top." Would you like them renamed "Solid Top" to match?'])
# ---------- MAX-MASTER ----------
MM_INTRO2='Each seat has its own leg, which gives the table more stability than a single pedestal base. The legs are 3” diameter, 14-gauge steel tubing with a 10” radius bend that makes it easy to clean under the table. The seats are high-density, color-impregnated composite that resists scratches and stains, and Torx® tamper-resistant hardware holds everything together. Tables can be bolted to the floor or set on tamper-resistant glides.'
MM_LEGS='**Legs:** 3” diameter, 14-gauge curved steel tubing with fully welded 6” × 6” × 1/4” steel mounting plates'
MM_SEATS='**Seats:** 13” diameter Super Slammer Stone compression-molded composite, scratch and stain resistant'
MM_H='**Heights:** 31.8” table top, 18.9” seat'
MM_COL='**Seat Colors:** Twilight, Cove, Sand, Raven, or stainless steel'
MM_LEGC='**Leg Colors:** Black or metallic silver'
def mm_inst(ss_seats):
    return ['**Bolt-Down or Glides:** Bolt to the floor with the concealed concrete expansion anchors included, or use the optional tamper-resistant leg glides. Glides cannot be added in the field to a table ordered for bolt-down.','**Clear Leg Protectors:** Optional clear PVC protectors, 3” diameter × 6” high, specified when ordering','**Stainless Steel Seats:** Optional 12” stainless steel seats, which lower the seat height to 18.25” ('+ss_seats+')','**ADA Version:** Available for bolt-down tables, with the seating arranged for wheelchair access','**Assembly:** Secure the base to the top and attach the seats; see the Norix instructions']
MM_REF='Series section: this is the same "About Norix Dayroom and Dining Tables" section as the Jupiter Round Table tab. Any changes you make there will be applied here too.'
MM_CODE='Model number: your current pages use "M4-4200" style numbers, but the Norix spec sheet and price list use "M44200." I used the Norix numbers. Would you prefer the format on your current pages?'
MM_OPT='Variant options: the variants are "Bolt Down Plate," "Clear Leg Protector," and "Leg Glides." Per the Norix price list, bolt-down has no extra charge and leg protectors and glides are add-ons, which matches your current prices.'
def mm(seats,shape,size,code,handle,weight,cur_h1,cur_sub,footprint,top_note,models,ss,game=True,extra_notes=(),wnote=''):
    nm=f'Max-Master {seats} Seat {shape} Table'
    tops=[LAMTOP,'**Top Attachment:** Embedded T-nuts give a steel-to-steel connection between the top and legs',f'**Top Size:** {size}',f'**Overall Footprint:** {footprint}',MM_H,f'**Weight:** {weight}',FIN]+([GAME] if game else [])+([top_note] if top_note else [])
    add(tab=f'{code} - {nm}',short=f'{code}: {nm}',handle=handle,src=NP+'max-master/',
     specs=[('Max-Master',U+'2020/11/M44200-Max-Master-Table-9.pdf')],
     h1=f'Norix {nm} – {code}',cur_h1=cur_h1,
     sub=(size.replace(' round',' Round') if shape=='Round' else size+' Rectangle')+f' Table with {seats} Attached Composite Seats for Dining Halls and Dayrooms',
     cur_sub=cur_sub,
     intro=[f'The **Norix {nm}** is a {size} table with {seats} attached seats, built for the daily demands of dining halls and dayrooms in correctional and behavioral healthcare facilities.',MM_INTRO2],
     bullets=[MM_LEGS,MM_SEATS]+tops+[MM_COL,MM_LEGC,S1000,GG,W10,IND,USA],
     models=models,install=mm_inst(ss),
     apps=apps(f'The Norix {nm} suits dining halls and dayrooms where fixed seating and a sturdy table need to hold up to constant use.'),series=TBL_SERIES,
     mt=f'Norix {nm} - {code} at Anchortex',
     md=None,notes=[MM_REF,MM_CODE]+list(extra_notes)+[MM_OPT,wnote])
mm(4,'Round','42” round','M44200','norix-max-master-4-seat-round-table','183 lbs (laminate top) or 174 lbs (stainless steel top)',
 'Norix Max-Master - 42” Round Metal Table with 4 Seats - Model M4-4200','Norix Furniture M4-4200 Max-Master 4 Seat Round Table','76” × 76”',
 '**Stainless Steel Top:** Optional 18-gauge stainless steel over a sound-deadening Quietcore particle board core, with a 1-1/4” edge',
 ['**M44200 – Laminate Solid Top:** 183 lbs','**M44200 – Laminate Game Top:** 183 lbs','**M44200 – Stainless Steel Quietcore Top:** 174 lbs'],'$520 list for a set of 4',
 extra_notes=['H1: the current H1 has extra dashes, "Metal Table," and "Model." I used the same format as the other table pages.'],
 wnote='Weights: all nine variants are set to 255 lbs. Accurate weights are 183 lbs for the laminate solid and game tops and 174 lbs for the stainless steel Quietcore top.')
mm(6,'Rectangle','30” × 72”','M63072','norix-max-master-6-seat-rectangle-table','280 lbs',
 'Norix Max-Master Durable 6 Seat Rectangle Table','Norix Furniture Rectangle Top Max-Master Table M6-3072','63” × 72”',
 '**Stainless Steel Top:** Optional 10-gauge 304 stainless steel with a 1-1/2” drop edge, which changes the height to 30.5”',
 ['**M63072 – Laminate Solid Top:** 280 lbs'],'$780 list for a set of 6',game=False,
 extra_notes=['H1: the current H1 says "Durable" and has no model number. I removed "Durable" and added the model number.','Game top: Norix does not offer a laminate game top for the 30” × 72” size, which matches your current variants.'],
 wnote='Weights: all three variants are set to 255 lbs. The accurate weight is 280 lbs.')
mm(6,'Round','54” round','M65400','norix-max-master-6-seat-round-table','270 lbs (laminate top) or 230 lbs (stainless steel top)',
 'Norix Max-Master Durable 6 Seat Round Table','Norix Furniture Round Max-Master Table M6-5400','88” × 88”',
 '**Stainless Steel Top:** Optional 18-gauge stainless steel over a sound-deadening Quietcore particle board core, with a 1-1/4” edge',
 ['**M65400 – Laminate Solid Top:** 270 lbs','**M65400 – Laminate Game Top:** 270 lbs','**M65400 – Stainless Steel Quietcore Top:** 230 lbs'],'$780 list for a set of 6',
 extra_notes=['H1: the current H1 says "Durable" and has no model number. I removed "Durable" and added the model number.'],
 wnote='Weights: all nine variants are set to 255 lbs. Accurate weights are 270 lbs for the laminate solid and game tops and 230 lbs for the stainless steel Quietcore top.')
mm(8,'Rectangle','30” × 96”','M83096','norix-max-master-8-seat-rectangle-table','375 lbs',
 'Norix Max‑Master - Rectangle Table with 8‑Seats - 30” x 96” - Model M8-3096','Norix Furniture Rectangle Max-Master Table M8-3096','63” × 96”',
 '**Stainless Steel Top:** Optional 10-gauge 304 stainless steel with a 1-1/2” drop edge, which changes the height to 30.5”',
 ['**M83096 – Laminate Solid Top:** 375 lbs','**M83096 – Laminate Game Top:** 375 lbs'],'$1,040 list for a set of 8',
 extra_notes=['H1: the current H1 has extra dashes, the size, and "Model." I used the same format as the other table pages.'],
 wnote='Weights: all six variants are set to 255 lbs. The accurate weight is 375 lbs.')
mm(8,'Round','60” round','M86000','norix-max-master-8-seat-round-table','372 lbs',
 'Norix Max-Master Durable 8 Seat Round Table','Norix Furniture Round Max-Master Table M8-6000','94” × 94”',None,
 ['**M86000 – Laminate Solid Top:** 372 lbs','**M86000 – Laminate Game Top:** 372 lbs'],'$1,040 list for a set of 8',
 extra_notes=['H1: the current H1 says "Durable" and has no model number. I removed "Durable" and added the model number.'],
 wnote='Weights: all six variants are set to 255 lbs. The accurate weight is 372 lbs.')
MD={'M44200':'Shop the Norix Max-Master M44200 4 seat round table. 42 inch laminate or stainless top with composite seats on steel legs for dining halls and dayrooms.',
 'M63072':'Shop the Norix Max-Master M63072 6 seat rectangle table. 30 x 72 inch laminate top with composite seats on curved steel legs for dining halls and dayrooms.',
 'M65400':'Shop the Norix Max-Master M65400 6 seat round table. 54 inch laminate or stainless top with composite seats on steel legs for dining halls and dayrooms.',
 'M83096':'Shop the Norix Max-Master M83096 8 seat rectangle table. 30 x 96 inch laminate or game top with composite seats on steel legs for dining halls.',
 'M86000':'Shop the Norix Max-Master M86000 8 seat round table. 60 inch laminate or game top with composite seats on curved steel legs for dining halls and dayrooms.'}
for d in P:
    if d['md'] is None: d['md']=MD[d['tab'].split(' ')[0]]
# ---------- MULTI-PURPOSE ----------
MP_TOP='**Top:** Decorative high-pressure laminate over a 45 lb density M3 particle board core with embedded T-nuts and a backer sheet, edged with glued and pinned black vinyl T-molding, 1-1/4” thick'
MP_FIN='**Top Finishes:** Titanium Evolve, Wild Cherry, Calcutta Marble, or Black Alicante with a black edge, or Kensington Maple, Asian Sun, Montana Walnut, or Palisades Oak with a bark edge'
MP_GAME='**Game Top:** Titanium Evolve laminate with a printed game board, black edge'
MP_BCOL='**Base Colors:** Black or metallic silver'
MP_TAIL=['**Static Load Testing:** Tested to 500 lbs',GG,W10,IND,USA]
MP_INST=['**Glides:** Tamper-resistant leveling glides are included','**Assembly:** Ships knocked down to save on freight, with Torx® tamper-resistant hardware; see the Norix instructions']
def mp_intro(shape_text,base):
    return [f'The **Norix Multi-Purpose Table with {shape_text}** is a lighter-weight laminate table on a welded steel {base}, for classrooms, dayrooms, and program rooms in correctional and behavioral healthcare facilities.',
     'The base is 1-3/4” 12-gauge steel tubing, fully welded and sealed on the exposed ends, so there are no openings to hide contraband. It is powder coated for scratch and corrosion resistance, and tamper-resistant glides allow leveling. The top fastens to the base with tamper-resistant security screws for a solid metal-to-metal connection.']
MP_BASE_T='**Base:** Steel T-base of 1-3/4” 12-gauge tubing, fully welded and sealed, with tamper-resistant leveling glides'
MP_BASE_X='**Base:** Steel X-base of 1-3/4” 12-gauge tubing, fully welded and sealed, with tamper-resistant leveling glides'
MPREF=SER_REF_T
add(tab='MP1860 / MP2460 / MP3060 - Multi-Purpose Table',short='MP1860 / MP2460 / MP3060: Multi-Purpose Rectangle Table',
 handle='norix-rectangle-top-multi-purpose-table',src=NP+'multi-purpose/',
 specs=[('MP1860 / MP2460 / MP3060',U+'2024/12/MP1860-Multi-Purpose-Table.pdf')],
 h1='Norix Multi-Purpose Table with Rectangle Top – MP1860 / MP2460 / MP3060',cur_h1='Norix Rectangle‑Top Multi‑Purpose Table - High‑Pressure Solid Top - Models MP1860 / MP2460 / MP3060',
 sub='Rectangle Laminate Table on a Sealed Steel T-Base for Classrooms and Program Rooms',
 cur_sub='Norix Furniture Rectangle Top Multi-Purpose Table MP1860, MP2460, MP3060',
 intro=mp_intro('Rectangle Top','T-base')[:1]+['It comes in three 60” long sizes: 18”, 24”, or 30” deep.']+mp_intro('Rectangle Top','T-base')[1:],
 bullets=[MP_BASE_T,MP_TOP,'**Top Sizes:** 18” × 60”, 24” × 60”, or 30” × 60”','**Height:** 29”','**Weight:** 59 to 91 lbs, depending on size',MP_FIN,MP_BCOL]+MP_TAIL,
 models=['**MP1860 – 18” × 60”:** Solid top, 59 lbs','**MP2460 – 24” × 60”:** Solid top, 74 lbs','**MP3060 – 30” × 60”:** Solid top, 91 lbs'],
 install=MP_INST,
 apps=apps('The Norix Multi-Purpose Rectangle Table suits classrooms and program rooms that need a lighter table that is still tamper resistant.'),series=TBL_SERIES,
 mt='Norix Multi-Purpose Table with Rectangle Top at Anchortex',
 md='Shop the Norix MP1860, MP2460, and MP3060 multi-purpose rectangle table. Laminate top on a sealed steel T-base with tamper-resistant glides for classrooms.',
 notes=[MPREF,
  'H1: the current H1 has extra dashes, "High-Pressure Solid Top," and "Models." I used the same format as the other table pages.',
  'Meta title: the three model numbers would make it longer than 65 characters, so I left them out.',
  'Static load: the Multi-Purpose spec sheet says 500 lbs, not 1,000 lbs like the other Norix tables, so I used 500 lbs.',
  'Weights: all three variants are set to 255 lbs. Accurate weights are 59 lbs (MP1860), 74 lbs (MP2460), and 91 lbs (MP3060).'])
add(tab='MP3600 / MP4200 - Multi-Purpose Round Table',short='MP3600 / MP4200: Multi-Purpose Round Table',
 handle='norix-round-top-multi-purpose-table',src=NP+'multi-purpose/',
 specs=[('MP3600 / MP4200',U+'2024/12/MP1860-Multi-Purpose-Table.pdf')],
 h1='Norix Multi-Purpose Table with Round Top – MP3600 / MP4200',cur_h1='Norix Durable Multi-Purpose Table with Round Top',
 sub='Round Laminate Table on a Sealed Steel X-Base with Solid or Game Top',
 cur_sub='Norix Furniture Round Top Multi-Purpose Table MP-3600, MP-4200',
 intro=mp_intro('Round Top','X-base')[:1]+['It comes in 36” and 42” round sizes, with a solid laminate top or a game top.']+mp_intro('Round Top','X-base')[1:],
 bullets=[MP_BASE_X,MP_TOP,'**Top Sizes:** 36” or 42” round','**Height:** 29”','**Weight:** 53 lbs (36”) or 66 lbs (42”)',MP_FIN,MP_GAME,MP_BCOL]+MP_TAIL,
 models=['**MP3600 – 36” Round:** Solid top or game top, 53 lbs','**MP4200 – 42” Round:** Solid top or game top, 66 lbs'],
 install=MP_INST,
 apps=apps('The Norix Multi-Purpose Round Table suits classrooms, dayrooms, and program rooms that need a lighter table that is still tamper resistant.'),series=TBL_SERIES,
 mt='Norix Multi-Purpose Table with Round Top - MP3600 / MP4200',
 md='Shop the Norix MP3600 / MP4200 multi-purpose round table. 36 or 42 inch laminate solid or game top on a sealed steel X-base for classrooms and dayrooms.',
 notes=[MPREF,
  'H1: the current H1 says "Durable" and has no model numbers. I removed "Durable" and added the model numbers.',
  'Meta title: adding "at Anchortex" would make it more than 65 characters, so I left it off.',
  'Static load: the Multi-Purpose spec sheet says 500 lbs, not 1,000 lbs like the other Norix tables, so I used 500 lbs.',
  'Weights: all four variants are set to 255 lbs. Accurate weights are 53 lbs (MP3600) and 66 lbs (MP4200). The game top versions weigh the same as the solid tops.'])
add(tab='MP3636 / MP4242 - Multi-Purpose Square Table',short='MP3636 / MP4242: Multi-Purpose Square Table',
 handle='norix-square-top-multi-purpose-table',src=NP+'multi-purpose/',
 specs=[('MP3636 / MP4242',U+'2024/12/MP1860-Multi-Purpose-Table.pdf')],
 h1='Norix Multi-Purpose Table with Square Top – MP3636 / MP4242',cur_h1='Norix Durable Multi-Purpose Table with Square Top',
 sub='Square Laminate Table on a Sealed Steel X-Base with Solid or Game Top',
 cur_sub='Norix Furniture Square Top Multi-Purpose Table MP3636, MP4242',
 intro=mp_intro('Square Top','X-base')[:1]+['It comes in 36” and 42” square sizes, with a solid laminate top or a game top.']+mp_intro('Square Top','X-base')[1:],
 bullets=[MP_BASE_X,MP_TOP,'**Top Sizes:** 36” or 42” square','**Height:** 29”','**Weight:** 63 lbs (36”) or 79 lbs (42”)',MP_FIN,MP_GAME,MP_BCOL]+MP_TAIL,
 models=['**MP3636 – 36” Square:** Solid top or game top, 63 lbs','**MP4242 – 42” Square:** Solid top or game top, 79 lbs'],
 install=MP_INST,
 apps=apps('The Norix Multi-Purpose Square Table suits classrooms, dayrooms, and program rooms that need a lighter table that is still tamper resistant.'),series=TBL_SERIES,
 mt='Norix Multi-Purpose Table with Square Top - MP3636 / MP4242',
 md='Shop the Norix MP3636 / MP4242 multi-purpose square table. 36 or 42 inch laminate solid or game top on a sealed steel X-base for classrooms and dayrooms.',
 notes=[MPREF,
  'H1: the current H1 says "Durable" and has no model numbers. I removed "Durable" and added the model numbers.',
  'Meta title: adding "at Anchortex" would make it more than 65 characters, so I left it off.',
  'Static load: the Multi-Purpose spec sheet says 500 lbs, not 1,000 lbs like the other Norix tables, so I used 500 lbs.',
  'Weights: all four variants are set to 255 lbs. Accurate weights are 63 lbs (MP3636) and 79 lbs (MP4242). The game top versions weigh the same as the solid tops.'])
# ---------- OASIS ----------
add(tab='O43048 / O43072 - Oasis Cafeteria Table',short='O43048 / O43072: Oasis Cafeteria Table',
 handle='norix-oasis-cafeteria-table',src=NP+'oasis/',
 specs=[('O43048 / O43072',U+'2024/12/O43048O43072-Oasis-Series-Cluster-Seating.pdf')],
 h1='Norix Oasis Cafeteria Table – O43048 / O43072',cur_h1='Norix Oasis - 4-Seat Cafeteria Table with Rectangle Top - Model O4-3048 / O4-3072',
 sub='4-Seat Rectangle Cluster Table with Fixed or Swivel Molded Seats for Dayrooms, Dining, and Visitation',
 cur_sub='Norix Furniture Oasis Table O4-3048, O4-3072 Rectangle Table For Prisons, Detention Centers and Behavioral Health Care Facilities',
 intro=['The **Norix Oasis Cafeteria Table** is a four-seat cluster table made for dayrooms, dining halls, and visitation areas in prisons, detention centers, and behavioral healthcare facilities. Unlike a stool, each molded seat has a back for support, and swivel seats make it easier to sit down and get up.',
  'The heavy steel frame is fully welded and supports both the top and the seats. The one-piece seats are rotationally molded from high-impact polyethylene and attach through molded-in threaded steel inserts, and all connections use Torx® security hardware. The table comes in 30” × 48” and 30” × 72” sizes, with a laminate solid top, game top, or stainless steel inlay top.'],
 bullets=['**Frame:** Fully welded 3” × 1-1/2” rectangle tube and 2” square steel tube, with 10-gauge steel top and seat mounting plates',LAMTOP,'**Stainless Steel Inlay Top:** Type 304 stainless steel with a radiused Slammer Stone edge, 1-1/4” thick',TNUT,'**Seats:** One-piece rotationally molded high-impact polyethylene with back support, fixed or swivel','**Top Sizes:** 30” × 48” or 30” × 72”','**Heights:** 31” table, 18.3” seat, 34” seat back','**Seat Width:** 17”','**Weight:** 220 lbs (30” × 48”) or 280 lbs (30” × 72”)',FIN,GAME,'**Seat Colors:** '+SEATC,S1000,GG,W10,IND,USA],
 models=['**O43048 – 30” × 48”:** Laminate solid top, game top, or stainless steel inlay top with fixed seats, 220 lbs','**O43072 – 30” × 72”:** Laminate solid top or stainless steel inlay top, with fixed or swivel seats, 280 lbs'],
 install=['**Glides or Bolt-Down:** Free-standing with tamper-resistant glides, or bolt-down with concealed concrete expansion anchors included in the bolt-down kit','**Swivel Seats:** 12-gauge powder-coated swivel mechanism with 60° rotation','**ADA Version:** Available in the 30” × 72” size','**Assembly:** See the Norix instructions'],
 apps=apps('The Norix Oasis Cafeteria Table suits dining halls, dayrooms, and visitation areas where people need more back support than a stool gives.'),series=TBL_SERIES,
 mt='Norix Oasis Cafeteria Table - O43048 / O43072 at Anchortex',
 md='Shop the Norix Oasis cafeteria table with 4 fixed or swivel molded seats. 30 x 48 or 30 x 72 inch laminate or stainless top for dayrooms and dining halls.',
 notes=[SER_REF_T,
  'H1: the current H1 has extra dashes, "4-Seat," and "Model." I used the same format as the other table pages.',
  'Model number: your current page uses "O4-3048" and "O4-3072," but the Norix spec sheet uses "O43048" and "O43072." I used the Norix numbers. Would you prefer the format on your current page?',
  'Leg options: your current description lists 4” and 2.5” leg glides and bolt-down. These match the Norix Leg Style tables, and the Oasis spec sheet does not mention leg sizes, so I left them out.',
  'Weights: all seven variants are set to 255 lbs. Accurate weights are 220 lbs (30” × 48”) and 280 lbs (30” × 72”). Norix does not list a separate weight for the stainless steel inlay top.'])
