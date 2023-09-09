import pygame as p
h,v,m=10,10,1
x_change,y_change=h+m,0
class smt(p.sprite.Sprite):
 def __init__(self,x,y):
  super().__init__()
  self.image=p.Surface([h,v])
  self.rect,self.rect.x,self.rect.y=self.image.get_rect(),x,y
p.init()
s,spl,ssm=p.display.set_mode([500,500]),p.sprite.Group(),[]
for i in range(15):
 x,y=250-(h+m)*i,30
 sm=smt(x,y)
 ssm.append(sm)
 spl.add(sm)
t=p.time.Clock()
while True:
 for event in p.event.get():
  if event.type==p.KEYDOWN:
   if event.key==p.K_LEFT:
    x_change,y_change=(h+m)*-1,0
   if event.key==p.K_RIGHT:
    x_change,y_change=(h+m),0
   if event.key==p.K_UP:
    x_change,y_change=0,(v+m)*-1
   if event.key==p.K_DOWN:
    x_change,y_change=0,(v+m)
 osm=ssm.pop()
 spl.remove(osm)
 x,y=ssm[0].rect.x+x_change,ssm[0].rect.y+y_change
 sm=smt(x,y)
 ssm.insert(0,sm)
 spl.add(sm)
 s.fill((50,50,50))
 spl.draw(s)
 p.display.flip()
 t.tick(5)
p.quit()


