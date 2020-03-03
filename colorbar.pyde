#Color Random Bars

def setup():
    size(1280, 720)
    ml = 55
    mt = 55
    rectMode(CENTER);
    for i in range (8):
        rect(ml, mt, 20, 200);
        ml=ml+100
        fill(random(450), random(250), random(450))
