import pygame,random,sys
a,tr=(pygame.image.load(f'{i}.webp') for i in ["auto","truck"])
tl=pygame.transform.scale(pygame.image.load("tło.webp"),(400,600))
pygame.init();e,c,g,pr,s=pygame.display.set_mode((400,600)),pygame.time.Clock(),a.get_rect(center=(200, 500)),[],0
def dp():pr.append(tr.get_rect(center=(random.choice([80, 150, 240, 320]),-50)))
dp()
while 1:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:pygame.quit();sys.exit()
    k=pygame.key.get_pressed();g.x+=(k[pygame.K_RIGHT]-k[pygame.K_LEFT])*5
    for p in pr:
        p.y+=5+s//10
        if p.colliderect(g):pr=[];dp();s=0
        if p.y>600:pr.remove(p);s+=1
    if pr[-1].y>150:dp()
    e.blit(tl,(0,0));e.blit(a,g)
    for p in pr:e.blit(tr,p)
    e.blit(pygame.font.SysFont("",36).render(f"Punkty: {s}",1,([0]*3)),(10,10));pygame.display.flip();c.tick(60)