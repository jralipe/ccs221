#movements//belong to origin is 0
catX=0
catY=0 
#movements//belong to origin is 0
catheadX=0
catheadY=0
#movements//belong to origin is 0
rgbX = 0
rgbY = 0

#bolean
flag=True

def setup():

    size(1366,768)
    frameRate(80)
    
    
def draw():
    background(0,0,0)
    moveX = mouseX-500
    moveY = mouseY
    starbg();
    rainbow(moveX,moveY);
    catlimbs(moveX,moveY);
    catfeet(moveX,moveY);
    catbody(moveX,moveY);
    cathead(moveX,moveY);
    catface(moveX,moveY);
    rgbfunction(moveX,moveY);
    headfunction(moveX,moveY);
    function(moveX,moveY);
    
def starbg():
    fill(255)
    rect(random(width+50),random(height+50),50,50)
    rect(random(width+402),random(height+410),50,50)
    rect(random(width+50),random(height+500),50,50)
    rect(random(width+610),random(height+40),50,50)
    rect(random(width+170),random(height+70),50,50)
    rect(random(width+800),random(height+580),50,50)
    rect(random(width+760),random(height+520),50,50)
    rect(random(width+30),random(height+300),50,50)
    rect(random(width+800),random(height+300),50,50)
    rect(random(width+1300),random(height+300),50,50)
    rect(random(width+1200),random(height+510),50,50)
    rect(random(width+1120),random(height+120),50,50)
    
def rainbow(moveX, moveY):

    drawPointX = moveX -1000-100-50
    drawPointY = moveY-50-50
    yModifier = 0

    noStroke()
    for i in range(6):
        if i == 0:
            fill(237,28,36)
        elif i == 1:
            fill(255,127,39)
        elif i == 2:
            fill(255,242,0)
        elif i == 3:
            fill(0,255,30)
        elif i == 4:
            fill(0,0,255)
        elif i == 5:
            fill(128,0,125)

                    

        rect(drawPointX,rgbY+drawPointY+yModifier,60,25)
        rect(drawPointX+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60,rgbY+drawPointY+yModifier,60,25)
        rect(drawPointX+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60,rgbY+drawPointY+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbX+drawPointY-12.5+yModifier,60,25)
        rect(drawPointX+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60+60,rgbY+drawPointY-12.5+yModifier,60,25)
            
        yModifier += 25
            
    
     

def catlimbs(moveX, moveY):
    drawPointX = moveX+60+60+60+60+60+60
    drawPointY = moveY-25-15
        
    rectMode(CENTER)
    fill(0,0,0)
    rect(catX+drawPointX,catY+drawPointY,25*1.5,15*2)
    rect(catX+drawPointX+15,catY+drawPointY+7.5,25*1.5,15*2)
    rect(catX+drawPointX+15+15,catY+drawPointY+7.5+7.5,25*1.5,15*2)
    rect(catX+drawPointX+15+15+15,catY+drawPointY+7.5+7.5+7.5,25*1.5,15*2)

    fill(159,158,158)
    rect(catX+drawPointX,catY+drawPointY,20,15)
    rect(catX+drawPointX+15,catY+drawPointY+7.5,20,15)
    rect(catX+drawPointX+15+15,catY+drawPointY+7.5+7.5,20,15)
    rect(catX+drawPointX+15+15+15,catY+drawPointY+7.5+7.5+7.5,20,15)
    
    rectMode(CORNER)

def catfeet(moveX,moveY):
    drawPointX = moveX+60+60+60+60+60+60+60
    drawPointY = moveY+25+5
    #backfeet
    rectMode(CENTER)
    #1
    fill(0,0,0)
    rect(catX+drawPointX,catY+drawPointY,30,15+15)
    fill(159,158,158)
    rect(catX+drawPointX,catY+drawPointY,20,15*1.5)
    #2
    fill(0,0,0)
    rect(catX+drawPointX+8*6,catY+drawPointY,30,15+15)
    fill(159,158,158)
    rect(catX+drawPointX+8*6,catY+drawPointY,20,15*1.5)
    #front feet
    #1
    fill(0,0,0)
    rect(catX+drawPointX+8*18,catY+drawPointY,30,15+15)
    fill(159,158,158)
    rect(catX+drawPointX+8*18,catY+drawPointY,20,15*1.5)

    #2
    fill(0,0,0)
    rect(catX+drawPointX+8*24,catY+drawPointY,30,15+15)
    fill(159,158,158)
    rect(catX+drawPointX+8*24,catY+drawPointY,20,15*1.5)

def catbody(moveX,moveY):
    drawPointX = moveX+60+60+60+60+(60+60+60+60+30)
    drawPointY = moveY-25-25
    
    rectMode(CENTER)
    fill(0,0,0)
    rect(drawPointX,catY+drawPointY,180+20,130)
    rect(drawPointX,catY+drawPointY,180,130+20)
    rect(drawPointX,catY+drawPointY,180-20,130+20+20)
    fill(234,209,134)
    rect(drawPointX,catY+drawPointY,180,130)
    rect(drawPointX,catY+drawPointY,180-20,130+20)
    
    fill(255,108,255)
    rect(drawPointX,catY+drawPointY,180-20-20,130-20)
    rect(drawPointX,catY+drawPointY,180-20,130-20-20)
    rect(drawPointX,catY+drawPointY,180-20-20-20,130)
    
    fill(255,0,128)
    rect(drawPointX-40,catY+drawPointY-40,15,15)
    rect(drawPointX,catY+drawPointY-50,15,15)
    rect(drawPointX+40,catY+drawPointY-35,15,15)
    rect(drawPointX-35,catY+drawPointY-15,15,15)
    rect(drawPointX-50,catY+drawPointY+40,15,15)
    rect(drawPointX-60,catY+drawPointY+15,15,15)
    rect(drawPointX-20,catY+drawPointY+40,15,15)
    rect(drawPointX-15,catY+drawPointY+10,15,15)
    
def cathead(moveX,moveY):
    drawPointX = moveX+60+60+60+60+(60+60+60+60+60+60)
    drawPointY = moveY-10
    
    #faceoutline
    rectMode(CENTER)
    fill(0,0,0)
    #fill(159,158,158)
    rect(catheadX+drawPointX,catheadY+drawPointY,100,90)
    rect(catheadX+drawPointX,catheadY+drawPointY,100+20,90-25)
    rect(catheadX+drawPointX,catheadY+drawPointY,100+20+20,90-20-20)
    #earsoutline
    #1
    rect(catheadX+drawPointX-30-10,catheadY+drawPointY-40,40,30)
    rect(catheadX+drawPointX-30-10-5,catheadY+drawPointY-40,40-5,30+20)
    rect(catheadX+drawPointX-30-10-5,catheadY+drawPointY-40,40-10-10,30+20+20)
    #2
    rect(catheadX+drawPointX-30+75-5,catheadY+drawPointY-40,40,30)
    rect(catheadX+drawPointX-30+75,catheadY+drawPointY-40,40-5,30+20)
    rect(catheadX+drawPointX-30+75,catheadY+drawPointY-40,40-10-10,30+20+20)
    

    #skinoutline
    fill(159,158,158)
    rect(catheadX+drawPointX,catheadY+drawPointY,100-15,90-15)
    rect(catheadX+drawPointX,catheadY+drawPointY,100+20-15,90-25-15)
    rect(catheadX+drawPointX,catheadY+drawPointY,100+20+20-15,90-20-20-15)
    #earsoutline
    #1
    rect(catheadX+drawPointX-30-10,catheadY+drawPointY-40,40-15,30-15)
    rect(catheadX+drawPointX-30-10-5,catheadY+drawPointY-40,40-5-15,30+20-15)
    rect(catheadX+drawPointX-30-10-5,catheadY+drawPointY-40,40-10-10-15,30+20+20-15)
    #2
    rect(catheadX+drawPointX-30+75-5,catheadY+drawPointY-40,40-15,30-15)
    rect(catheadX+drawPointX-30+75,catheadY+drawPointY-40,40-5-15,30+20-15)
    rect(catheadX+drawPointX-30+75,catheadY+drawPointY-40,40-10-10-15,30+20+20-15)
    
    rectMode(CORNER)
    
def catface(moveX,moveY):
    drawPointX = moveX+60+60+60+60+(60+60+60+60+60+40)
    drawPointY = moveY-17.5
    
    
    #eyes
    rectMode(CENTER)
    fill(0,0,0)
    rect(catheadX+drawPointX,catheadY+drawPointY,15,17.5)
    rect(catheadX+drawPointX+55,catheadY+drawPointY,15,17.5)
    
    fill(255,255,255)
    rect(catheadX+drawPointX-5,catheadY+drawPointY-5,7.5,7.5)
    rect(catheadX+drawPointX+50,catheadY+drawPointY-5,7.5,7.5)
    
    #nose
    fill(0,0,0)
    rect(catheadX+drawPointX+35,catheadY+drawPointY+5,7.5,7.5)
    
    #mouth
    fill(0,0,0)
    rect(catheadX+drawPointX+27.5,catheadY+drawPointY+30,50,10)
    rect(catheadX+drawPointX+5,catheadY+drawPointY+24.5,6.5,20)
    rect(catheadX+drawPointX+5+22.5,catheadY+drawPointY+24.5,7.5,20)
    rect(catheadX+drawPointX+5+45,catheadY+drawPointY+24.5,7.5,20)
    
    #cheeksblush
    fill(255,192,203)
    rect(catheadX+drawPointX-20,catheadY+drawPointY+18.5,20,20)
    rect(catheadX+drawPointX+72.5,catheadY+drawPointY+18.5,20,20)
    
def rgbfunction(moveX,moveY):
    frameRate(60)
    global rgbX
    global rgbY
    global flag
    
    if flag:
        rgbX += 1
    if rgbX>2:
        flag = False
    if rgbX>2:
        rgbY += 1
    if rgbY>2:
        rgbX -= 1
    if rgbX<2:
        rgbY -= 1
    if rgbY<2:
        rgbX += 1

def function(moveX,moveY):
    global catX
    global catY
    global flag

    if flag:
        catX += 1
    if catX>3:
        flag = False
    if catX>3:
        catY += 1
    if catY>3:
        catX -= 1
    if catX<3:
        catY -= 1
    if catY<3:
        catX += 1
        
def headfunction(moveX,moveY):    
    global catheadX
    global catheadY
    global flag

    if flag:
        catheadX += 1
    if catheadX>5:
        flag = False
    if catheadX>5:
        catheadY += 1
    if catheadY>5:
        catheadX -= 1
    if catheadX<5:
        catheadY -= 1
    if catheadY<5:
        catheadX += 1
        
