import json,sys
GD='/tmp/claude-0/-home-claude/cfa6e804-8b87-569e-b391-80a01c05d6c7/scratchpad/gd'
exec(open(f'{GD}/build.py').read().split("RIOT=")[0].replace("D=sys.argv[1]",""))
exec(open(f'{GD}/paced.py').read())
BH='https://www.anchortex.com/collections/bh-behavioral-healthcare-furniture'
NX='https://www.anchortex.com/collections/norix-furniture'
A='https://www.anchortex.com/products/'
SERIES=[
('h3','[H2] About Norix Prodigy Bedroom Furniture Series'),
('p','The Norix Prodigy Bedroom Furniture Series offers coordinated furniture for behavioral healthcare facilities, psychiatric hospitals, residential treatment centers, and other demanding institutional environments. The collection includes beds, nightstands, desks, wardrobes, and storage furniture that combine safety-conscious design with a residential appearance.'),
('p','Common characteristics of the Prodigy Series include:'),
('b1','**Safety-Conscious Design:** Model-specific features designed to help reduce ligature risks, tampering, and opportunities for contraband concealment'),
('b1','**Durable Construction:** Reinforced polymer materials for strength and impact resistance'),
('b1','**Easy Cleaning:** Nonporous surfaces designed for routine cleaning and maintenance'),
('b1','**TruGrain™ Wood-Grain Finish:** Proprietary Norix technology that replicates the appearance and texture of natural wood, creating a less institutional environment'),
('b1','**Recycled Materials:** Recyclable polymer materials incorporating recycled content'),
('h3','[H2] About Norix Furniture'),
('p',f'Norix manufactures durable furniture for demanding environments, including behavioral healthcare facilities, psychiatric hospitals, correctional institutions, and residential treatment centers. Explore the full line of [Norix Furniture]({NX}) at Anchortex.'),
]
def apps(intro):
    return [
('h3','[H2] Applications'),
('p',intro),
('p','Typical applications include:'),
('b1','Behavioral healthcare facilities and psychiatric hospitals'),
('b1','Inpatient psychiatric units'),
('b1','Residential mental health treatment centers'),
('b1','Correctional and detention facilities with appropriate security requirements'),
('b1','Other supervised residential and institutional settings'),
('p',f"Explore Anchortex's [Behavioral Health Furniture]({BH}) collection for additional institutional furniture options."),
]
def meta(t,d): return [('h2','Meta Title and Description'),('p',f"**Meta title ({len(t)} characters):** {t}"),('p',f"**Meta description ({len(d)} characters):** {d}")]
MARKS=['Recommended H1','Revised Product Description','Construction:','Installation and Options','Available Models and Options','[H2] Applications','[H2] About Norix Prodigy','Meta Title and Description','Notes and Questions']
