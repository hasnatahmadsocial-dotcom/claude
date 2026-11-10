exec(open('p3.py').read().split('P=[]')[0])
NXF=NXF.replace('psychiatric hospitals, correctional','psychiatric hospitals, police stations, correctional')
TBL5=[x if not x[1].startswith('Norix tables are made') else ('p','Norix tables are made for dayrooms, dining halls, classrooms, and visitation areas in correctional and behavioral healthcare facilities, where furniture is used hard every day. The range covers molded-base tables such as the Jupiter, Evvolve, and Molded X-Base; Laminate X-Base tables; and steel-base tables such as the Leg Style, Multi-Purpose, Max-Master, and Oasis.') for x in TBL_SERIES]
P=[]
def add(**k): P.append(k)
EVF='**Plain Top Finishes:** Titanium Evolve, Wild Cherry, Kensington Maple, Asian Sun, Montana Walnut, Palisades Oak, Calcutta Marble, or Black Alicante laminate with a matching or black molded edge'
EXT='Citrus, Tranquil, Malibu, Cobalt, Wisteria, LUX Ivory, and LUX Onyx with a 6-piece minimum per color'
LAM='**Laminate Top:** High-pressure laminate over a 45 lb density M3 particle board core, with a 1½” thick radiused molded edge that is pressure fused to the top'
TN='**Top Attachment:** Embedded T-nuts give the laminate top a steel-to-steel connection to the base'
SER_NOTE5='Series section: I used your new wording, with semicolons, "Laminate" capitalized, and "Evvolve" added to the molded-base tables. I will make the same change on all the table pages.'
NEWNOTE='New product: this page is not on Anchortex yet. Once you send the URL and SKUs, I will create it in Shopify as a draft product with the Norix photos.'
add(new=True,tab='EJ3600 / EJ3636 - Evvolve Jr. Table',short='EJ3600 / EJ3636: Evvolve Jr. Table (New Product)',
 src=NP+'evvolve-jr/',specs=[('EJ3600 / EJ3636',U+'2026/04/EJXXXX-Evvolve-Jr-Table.pdf')],
 h1='Norix Evvolve Jr. Table with Round or Square Top – EJ3600 / EJ3636',
 sub='Lower-Height Ballasted Molded Base Table for Youth Dayrooms, Classrooms, and Dining Areas',
 intro=['The **Norix Evvolve Jr. Table** has the same ribbed molded base and safety features as the Norix Evvolve Table, at a lower 26.1” height made for adolescent environments. It comes in 36” round and 36” square sizes, with a plain laminate top or a game top.',
  'Norix designed the ribbed base around rotational symmetry, a pattern linked to a calm, comforting environment. The tapered shape adds stability when the base is ballasted and leaves room to clean around it. The base is made to be weighted on site with 200 lbs of dry sand, or Norix can ballast it at the factory. Ballast or a bolt-down kit is required to validate the warranty.'],
 bullets=['**Base:** One-piece rotationally molded high-impact polyethylene with UV stabilizers and a ribbed, tapered design',LAM,TN,
  '**Top Sizes:** 36” round or 36” square','**Height:** 26.1”','**Weight:** 73 lbs (round) or 76 lbs (square), without ballast',EVF,
  '**Game Top:** Optional Titanium Evolve laminate with a printed game board, black molded edge',
  '**Base Colors:** Twilight, Cove, Dove, Sienna, or Raven; '+EXT,
  '**Easy Cleaning:** The base resists blood, vinegar, urine, feces, salt solution, and chlorine solution, and can be cleaned with bleach solutions and hospital-grade disinfectants',
  S1000,'**Flammability Standards:** California Technical Bulletin 133 and ASTM E1537',GG,W10,IND,USA],
 models=['**EJ3600 – 36” Round:** Plain top or game top, 73 lbs','**EJ3636 – 36” Square:** Plain top or game top, 76 lbs'],
 install=['**Ballasting:** Fill the base on site with 200 lbs of dry sand (not supplied), or order factory ballasting. Ballast or a bolt-down kit is required to validate the warranty.',
  '**Bolt-Down:** Optional bolt-down kit','**Assembly:** Some assembly required; see Norix instructions'],
 apps=[('h3','[H2] Applications'),('p','The Norix Evvolve Jr. Table suits youth facilities, where a lower table fits the people using it.'),('p','Typical applications include:'),
  ('b1','Juvenile detention and youth correctional facilities'),('b1','Adolescent behavioral healthcare units and residential treatment centers'),('b1','Classrooms, dayrooms, and dining areas for young people'),
  ('p',f"Explore Anchortex's [Behavioral Healthcare Anti-Ligature Furniture]({BH}) and [Prison and Detention Furniture]({CDF}) collections for more institutional furniture.")],
 series=TBL5,
 mt='Norix Evvolve Jr. Table - EJ3600 / EJ3636 at Anchortex',
 md='Shop the Norix Evvolve Jr. table. A lower 26.1 inch molded base table with 36 inch round or square laminate or game top for youth dayrooms and classrooms.',
 notes=[NEWNOTE,SER_NOTE5,
  'Name: Norix calls this product both "Evvolve Junior" and "Evvolve Jr." I used "Evvolve Jr.," spelled with two Vs like the Evvolve Table.',
  'Proposed variants: Size (EJ3600 - 36" Round, EJ3636 - 36"x36" Square) and Top (Plain Top, Game Top), for four variants. Norix list prices are $1,300 (36” round) and $1,400 (36” square), with no extra charge for the game top. At your usual 80% of list, they would be $1,040 and $1,120.',
  'Game top: the Norix price list includes the Titanium Evolve game top for the Evvolve Jr., but the Norix web page does not list it. I included it as an option. Should I leave it out?',
  'Weights for the worksheet: 73 lbs (EJ3600) and 76 lbs (EJ3636), 26.1” high.'])
add(new=True,tab='EV3696 / CY3696 - Double Pedestal Table',short='EV3696 / CY3696: Double Pedestal Table (New Product)',
 src=NP+'double-pedestal-table/',specs=[('EV3696 / CY3696',U+'2026/04/DPXXXX-Double-Pedestal-Table-1.pdf')],
 h1='Norix Double Pedestal Table – EV3696 / CY3696',
 sub='36”×96” Laminate Table on Two Molded Bases for Up to Eight People, with Wheelchair Access',
 intro=['The **Norix Double Pedestal Table** is a 36”×96” laminate table on two molded polyethylene bases, with room for up to eight people to dine, work, or gather in dayrooms and dining areas of behavioral healthcare and correctional facilities. It comes with Evvolve bases or Jupiter bases.',
  'With a base at each end, the open space under the top meets ADA accessibility requirements for wheelchairs and other mobility aids, which a single pedestal table cannot do. The bases are made to be ballasted on site with 400 lbs of dry sand (200 lbs per base), or Norix can ballast them at the factory. Ballast or a bolt-down kit is required to validate the warranty.'],
 bullets=['**Bases:** Two one-piece rotationally molded high-impact polyethylene bases with UV stabilizers, in the ribbed Evvolve style or the cylinder Jupiter style',LAM,TN,
  '**Top Size:** 36”×96”','**Height:** 31.1” (Evvolve bases) or 29.3” (Jupiter bases)','**Space Between Bases:** 31” (Evvolve bases) or 35.8” (Jupiter bases)',
  '**Weight:** 196 lbs (Evvolve bases) or 180 lbs (Jupiter bases), without ballast',EVF,
  '**Base Colors:** Evvolve bases in Twilight, Cove, Dove, Sienna, or Raven, or '+EXT+'; Jupiter bases in Raven',
  '**Accessibility:** ADA compliant for wheelchairs and other mobility aids',
  '**Easy Cleaning:** The bases can be cleaned with bleach solutions and hospital-grade disinfectants without affecting the surface or color',
  S1000,'**Flammability Standards:** California Technical Bulletin 133 and ASTM E1537',GG,W10,USA],
 models=['**EV3696 – Evvolve Bases:** 36”×96”, 31.1” high, 196 lbs','**CY3696 – Jupiter Bases:** 36”×96”, 29.3” high, 180 lbs'],
 install=['**Ballasting:** Fill the bases on site with 400 lbs of dry sand, 200 lbs per base (not supplied), or order factory ballasting. Ballast or a bolt-down kit is required to validate the warranty.',
  '**Bolt-Down:** Optional bolt-down kit','**Assembly:** None required'],
 apps=apps('The Norix Double Pedestal Table suits dining areas and dayrooms that need one large table for a group, including a place for a wheelchair user.'),
 series=TBL5,
 mt='Norix Double Pedestal Table - EV3696 / CY3696 at Anchortex',
 md='Shop the Norix Double Pedestal table. A 36 x 96 inch laminate top on two Evvolve or Jupiter molded bases seats up to eight, with ADA wheelchair access.',
 notes=[NEWNOTE,SER_NOTE5,
  'Width: the Norix price list table, Tables Guide, and model numbers (EV3696 and CY3696) all say 36” × 96”. The spec sheet says 36” but gives 76.2 cm, which is 30”, and the price list ordering code says 30” × 96”. I used 36”.',
  'Proposed variants: Base (EV3696 - Evvolve Base, CY3696 - Jupiter Base), for two variants. The Norix list price is $3,525 for either base. At your usual 80% of list, it would be $2,820. Factory ballasting is $408 for both bases.',
  'Bolt-down: the price list shows a $250 bolt-down kit for the Evvolve bases and "NC" for the Jupiter bases, and the Norix web page offers the bolt-down kit only with the Evvolve bases. I wrote "optional bolt-down kit" without naming a base. Should I say it is for the Evvolve bases only?',
  'Game top: Norix does not list a game top for this table, so I left it out.',
  'Indoor use: unlike the other Norix tables, this spec sheet does not say "indoor use only," so I left that line out.',
  'Weights for the worksheet: 196 lbs (EV3696) and 180 lbs (CY3696). Heights are 31.1” and 29.3”.'])
