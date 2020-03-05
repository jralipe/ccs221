#Jewel Josef Jasper C. Morales BSCS-1A
#nyancat

nyanx = 10
nyany = 10
flag = True
conway = None
pg = None
def setup():
    size(1080,720)
    background(1)
    frameRate(80) 





def draw():
    background(0,0,72)
    global nyanx
    global nyany
    global flag

    #stars
    fill(255,174,201)
    rect(500,520,20,100)#down
    rect(520,500,100,20)#right
    rect(500,400,20,100)#up
    rect(400,500,100,20)#left
    
    
    rect(100,100,10,50)#down
    rect(110,90,50,10)#right
    rect(100,40,10,50)#up
    rect(50,90,50,10)#left 
    
    rect(700,200,10,50)#down
    rect(710,190,50,10)#right
    rect(700,140,10,50)#up
    rect(650,190,50,10)#left 
    
    rect(400,300,10,50)#down
    rect(410,290,50,10)#right
    rect(400,240,10,50)#up
    rect(350,290,50,10)#left
    
    rect(100,600,10,50)#down
    rect(110,590,50,10)#right
    rect(100,540,10,50)#up
    rect(50,590,50,10)#left
    
    rect(900,100,10,50)#down
    rect(910,90,50,10)#right
    rect(900,40,10,50)#up
    rect(850,90,50,10)#left 
    
    rect(900,600,10,50)#down
    rect(910,590,50,10)#right
    rect(900,540,10,50)#up
    rect(850,590,50,10)#left
    
    
    #rainbow
    noStroke()
    fill(255,0,128)
    rect(nyanx+-800,nyany+100,1000,40,100) #40
    fill(255,128,64)
    rect(nyanx+-800,nyany+140,1000,40,100) #80
    fill(255,255,128)
    rect(nyanx+-800,nyany+180,1000,40,100) #135
    fill(108,255,146)
    rect(nyanx+-800,nyany+220,1000,40,100) #175
    fill(100,100,225)
    rect(nyanx+-800,nyany+260,1000,40,100) #215
    fill(128,0,128)
    rect(nyanx+-800,nyany+300,1000,40,100) #255
    
    
    #body
    stroke(75,75,75)
    fill(255,216,176)
    rect(nyanx+320,nyany+320,30,45,100) #limb1
    rect(nyanx+195,nyany+310,30,55,100) #limb2
    fill(255,255,255)
    rect(nyanx+320,nyany+315,30,30,50)
    fill(255,255,255)
    rect(nyanx+100,nyany+100,300,240,100)
    noStroke()
    fill(15,15,255)
    rect(nyanx+110,nyany+110,280,220,100)
    
    #backpack
    stroke(75,75,75)
    fill(0,251,125)
    rect(nyanx+320,nyany+95,30,230,100)
    rect(nyanx+130,nyany+20,215,100,100)
    fill(75,75,75)
    rect(nyanx+180,nyany+50,5,40)
    rect(nyanx+180,nyany+70,165,5,100)
    fill(0,251,125)
    rect(nyanx+250,nyany+90,30,240,100)
    
    
    
    #head
    fill(255,255,255)
    stroke(75,75,75)
    rect(nyanx+260,nyany+175,50,50,100)
    rect(nyanx+400,nyany+175,50,50,100)
    rect(nyanx+240,nyany+185,230,150,100)
    stroke(75,75,75)
    fill(255,216,176)
    rect(nyanx+260,nyany+195,220,140,100)
    
    #eyes
    noStroke()
    fill(0)
    ellipse(nyanx+320,nyany+245,10,10)
    ellipse(nyanx+450,nyany+245,10,10)
    
    #mouth
    rect(nyanx+360,nyany+295,50,1)
    
    #limbs
    stroke(75,75,75)
    fill(255,216,176)
    rect(nyanx+260,nyany+325,30,50,100)
    rect(nyanx+135,nyany+315,30,55,100)
    fill(255,255,255)
    rect(nyanx+260,nyany+315,30,40,50)
    rect(nyanx+135,nyany+315,30,30,50)
    
    #animation
    if flag:
            nyanx +=1

    if nyanx > 600:
            flag = False

    if nyanx >550:
            nyany +=1

    if nyany > 300:
            nyanx -=1

    if nyanx < 60:
            nyany -=1

    if nyany < 100:
            nyanx +=1
