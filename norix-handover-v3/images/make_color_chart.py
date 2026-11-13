from PIL import Image, ImageDraw, ImageFont
C=[("Aqua","#4d9b92"),("Black","#000000"),("Blue Gray","#9eb4bf"),("Brown","#7f5e1d"),("Burgundy","#80474e"),("Canvas","#e0dbc7"),
   ("Claylight","#b7856e"),("Gray","#7f7f7f"),("Green","#209300"),("Indigo","#77579b"),("Midnight Blue","#4d627f"),("Moss","#777658"),
   ("Overcast","#667690"),("Sand","#d1cc92"),("Seagrass","#8a9b7a"),("Slate Blue","#3942ef"),("Stone Gray","#d3d1cb"),("Tide","#86a9ad")]
S=2  # draw at 2x then downscale for smooth edges
cols,rows=6,3
sq=200*S; gapx=60*S; m=60*S; txt=56*S; rowgap=36*S
W=m*2+cols*sq+(cols-1)*gapx; H=m*2+rows*(sq+txt)+(rows-1)*rowgap
im=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(im)
f=ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",30*S)
for k,(n,h) in enumerate(C):
    r,c=divmod(k,cols); x=m+c*(sq+gapx); y=m+r*(sq+txt+rowgap)
    d.rounded_rectangle([x,y,x+sq,y+sq],radius=14*S,fill="white",outline="#b3b3b3",width=4*S)
    p=14*S; d.rectangle([x+p,y+p,x+sq-p,y+sq-p],fill=h)
    tw=d.textlength(n,font=f); d.text((x+(sq-tw)/2,y+sq+14*S),n,fill="#333333",font=f)
im=im.resize((W//S,H//S),Image.LANCZOS)
out="/home/user/claude/norix-handover-v3/images/Cortech-Endurance-18-Color-Chart.jpg"
im.save(out,quality=92); print(im.size)
