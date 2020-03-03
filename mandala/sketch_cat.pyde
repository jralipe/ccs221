#Nyancat by Maria Arlyn Fuerte
#BSCS1A

catx = 0
caty = 0
flag = True

def setup():
    size(900, 600)
    background(25, 25, 112)
    
def draw():
    global catx
    global caty
    global flag
    noStroke()
    background(25, 25, 112)
    
    
    fill(255, 0, 0) #RED
    rect(0, caty +150, 200, 20)
    fill(255, 165, 0) #ORANGE
    rect(0, caty +170, 200, 20)
    fill(255, 255, 0) #YELLOW
    rect(0, caty + 190, 200, 20)
    fill(0, 128, 0) #GREEN
    rect(0, caty +210, 200, 20)
    fill(0, 0, 255) #BLUE
    rect(0, caty +230, 200, 20)
    fill(75, 0, 130) #Violet
    rect(0, caty +250, 200, 20)
        
    
    if caty > 280:
        flag = False
    
    if caty > 200:
        catx +=1
        
    if catx > 250:
        caty -=1
   
    if caty < 50:
        catx -=1
        
    if catx < 30:
        caty +=1


    #Pikabody
    fill(160)
    rect(200, caty +135, 180, 150)
    fill(100)
    rect(215, caty +150, 150, 120)
    
    fill(160)
    rect(215, caty +150, 10, 10)
    rect(355, caty +150, 10, 10)
    rect(215, caty +260, 10, 10)
    
    #BELT
    fill(255)
    rect (240, caty+ 130, 30, 170)
    
    #Shadow
    fill(0)
    rect(190, caty +145, 10, 150) #left
    rect(380, caty +145, 10, 150) #right
    rect(200, caty +285, 180, 10) #bottom
    rect(210, caty +130, 160, 10) #top
    rect(200, caty +135, 10, 10) #left
    rect(370, caty +135, 10, 10) #right
    rect(190, caty +280, 20, 10)
    rect(180, caty +290, 10, 20)# backfeet left
    rect(180, caty +310, 30, 10)#backfeet bottom
    rect(210, caty +290, 10, 20) #backfeet right
    rect(230, caty +290, 10, 20)
    rect(240, caty +310, 20, 10)
    rect(260, caty +290, 10, 30)
    
    #backfeet
    fill(160)
    rect(190, caty +290, 20, 20)
    rect(240, caty +290, 20, 20)
    
    
    #head
    fill(0)
    rect(295, caty +220, 140, 40)
    rect(305, caty +210, 120, 15)
    rect(315, caty +205, 35, 8)
    rect(380, caty +205, 35, 8)
    rect(315, caty +197, 25, 8)
    rect(390, caty +197, 25, 8)
    rect(323, caty +189, 10, 8)
    rect(398, caty +189, 10, 8)
    rect(305, caty +255, 120, 15)
    rect(315, caty +270, 100, 20)
    rect(320, caty +290, 15, 10)
    rect(330, caty +300, 20, 10)
    rect(370, caty +290, 15, 10)
    rect(380, caty +300, 20, 10)
    fill(128)
    rect(330, caty +290, 20, 10)
    rect(380, caty +290, 20, 10)
    rect(315, caty +225, 110, 30)
    
    
    #eyes
    fill(20, 20, 20)
    rect(340, caty +230,20, 20)
    rect(380, caty +230, 20, 20)
    fill(235, 235, 235)
    rect(350, caty +240, 10, 10)
    rect(390, caty +240, 10, 10)
    
    #cheeks
    fill(250, 182, 193)
    circle(322, caty +248, 15)
    circle(418, caty +248, 15)
    
    #SWORD
    fill(50)
    rect(400, caty +290, 30, 20)
    rect(430, caty +280, 30, 40)
    fill(255)
    rect(460, caty +290, 90, 20)#BLADE
    #shadow
    fill(0)
    rect(390, caty +300, 10, 20)
    rect(400, caty+ 310, 40, 10)
    rect(430, caty +320, 40, 10)
    rect(460, caty +310, 90, 10)
    rect(550, caty +290, 10, 30)
    rect(460, caty +280, 90, 10)
    rect(420, caty +270, 50, 10)
    rect(410, caty +280, 20, 10)
    rect(540, caty +290, 10, 10)
