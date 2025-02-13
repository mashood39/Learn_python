import turtle as t
import colorsys
t.bgcolor('black')
t.speed(0)
t.tracer(100)      
t.pensize(1)       
h = 0.5 
for i in range(250):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.004  
    t.fillcolor(c)
    t.begin_fill()
    t.forward(i)    
    t.left(100)     
    t.circle(30)    
    for j in range(2):
        t.forward(i * j)  
        t.right(109)     
    t.end_fill()  
t.done()  
