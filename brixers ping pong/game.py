from pygame import*
w = 700
h = 500
win = display.set_mode((w,h))
color = (255,10,75)
win.fill(color)
while True:
   
    for e in event.get():
        if e.type==QUIT:
            exit()




    display.update()