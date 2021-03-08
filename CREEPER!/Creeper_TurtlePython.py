#Creeper

#imports
import turtle
'''
import playsound
from playsound import PlaysoundException
from gtts import gTTS
'''
import time

#main turtle and screen
t = turtle
t.speed(0)
t.screensize(1300,1900)
screen = t.Screen()
t.hideturtle()

#progressbar form
ned_teller = turtle.Turtle()
ned_teller.hideturtle
ned_teller.penup()
ned_teller.goto(-200,205)
ned_teller.pendown()

for sidene in range(2):
    ned_teller.hideturtle
    ned_teller.fd(400)
    ned_teller.rt(90)
    ned_teller.fd(11)
    ned_teller.rt(90)

ned_teller.goto(-195,200)
ned_teller.color('blue')
ned_teller.pensize(11)

#progressbar skrift
t0 = turtle.Turtle()
t0.penup()
t0.hideturtle()

t0.goto(0,170)
arg = 'Installing TURTLES...'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

#creeperfunc
def creeper():
    t.fillcolor('lightgreen')
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)

    t.forward(25)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(25)
    t.left(90)

    for b in range(2):
        t.forward(300)
        t.left(90)
        t.forward(100)
        t.left(90)

    t.forward(25)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(75)
    t.left(90)

    for i in range(5):
        t.forward(10)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(50)
        t.right(90)
    t.left(90)

    t.forward(75)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(10)
    t.right(90)

    t.forward(25)
    t.left(90)
    t.forward(25)

    t.right(90)
    t.forward(31)
    t.end_fill()

    #Creeper Fjes
    t.color('lightgreen')
    t.forward(20)


    t.color('black')
    t.fillcolor('black')
    t.begin_fill()
    t.forward(25)
    t.left(90)

    for i in range(2):
        t.forward(15)
        t.right(90)

    for i in range(4):
        t.forward(25)
        t.left(90)

    t.right(180)
    t.forward(30)

    for i in range(4):
        t.forward(25)
        t.right(90)

    t.left(90)
    for i in range(2):
        t.forward(15)
        t.right(90)
    t.left(180)
    t.forward(25)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.end_fill()

#turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t8 = turtle.Turtle()
t9 = turtle.Turtle()
t10 = turtle.Turtle()
t11 = turtle.Turtle()
t12 = turtle.Turtle()
t13 = turtle.Turtle()
t14 = turtle.Turtle()
t15 = turtle.Turtle()
t16 = turtle.Turtle()
t17 = turtle.Turtle()
t18 = turtle.Turtle()
t19 = turtle.Turtle()

o2 = turtle.Turtle()
o3 = turtle.Turtle()
o4 = turtle.Turtle()
o5 = turtle.Turtle()
o6 = turtle.Turtle()
o7 = turtle.Turtle()
o8 = turtle.Turtle()
o9 = turtle.Turtle()
o10 = turtle.Turtle()
o11 = turtle.Turtle()
o12 = turtle.Turtle()
o13 = turtle.Turtle()
o14 = turtle.Turtle()
o15 = turtle.Turtle()
o16 = turtle.Turtle()
o17 = turtle.Turtle()
o18 = turtle.Turtle()
o19 = turtle.Turtle()

#progressbar skrift
t0.clear()
arg = 'Done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(50)
time.sleep(0.5)

t0.clear()
arg = 'Installing TURTLE Shapes...'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

#shape
t.addshape('rock.gif')
t.addshape('bomb.gif')
t.addshape('explosio.gif')
t.addshape('explosion.gif')

t0.shape('explosion.gif')


t1.shape('bomb.gif')
t2.shape('rock.gif')
t3.shape('explosio.gif')
t4.shape('rock.gif')
t5.shape('rock.gif')
t6.shape('explosio.gif')
t7.shape('bomb.gif')
t8.shape('rock.gif')
t9.shape('rock.gif')
t10.shape('bomb.gif')
t11.shape('rock.gif')
t12.shape('bomb.gif')
t13.shape('explosio.gif')
t14.shape('bomb.gif')
t15.shape('bomb.gif')
t16.shape('rock.gif')
t17.shape('bomb.gif')
t18.shape('rock.gif')
t19.shape('explosio.gif')

o2.shape('rock.gif')
o3.shape('explosio.gif')
o4.shape('rock.gif')
o5.shape('rock.gif')
o6.shape('explosio.gif')
o7.shape('bomb.gif')
o8.shape('rock.gif')
o9.shape('rock.gif')
o10.shape('bomb.gif')
o11.shape('rock.gif')
o12.shape('bomb.gif')
o13.shape('explosio.gif')
o14.shape('bomb.gif')
o15.shape('bomb.gif')
o16.shape('rock.gif')
o17.shape('bomb.gif')
o18.shape('rock.gif')
o19.shape('explosio.gif')

#progressbar skrift
t0.clear()
arg = 'Done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(50)
time.sleep(0.5)

t0.clear()
arg = 'Hiding TURTLES...'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

#hideturtle
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
t5.hideturtle()
t6.hideturtle()
t7.hideturtle()
t8.hideturtle()
t9.hideturtle()
t10.hideturtle()
t11.hideturtle()
t12.hideturtle()
t13.hideturtle()
t14.hideturtle()
t15.hideturtle()
t16.hideturtle()
t17.hideturtle()
t18.hideturtle()
t19.hideturtle()

o2.hideturtle()
o3.hideturtle()
o4.hideturtle()
o5.hideturtle()
o6.hideturtle()
o7.hideturtle()
o8.hideturtle()
o9.hideturtle()
o10.hideturtle()
o11.hideturtle()
o12.hideturtle()
o13.hideturtle()
o14.hideturtle()
o15.hideturtle()
o16.hideturtle()
o17.hideturtle()
o18.hideturtle()
o19.hideturtle()

#progressbar skrift
t0.clear()
arg = 'Done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(50)
time.sleep(0.5)

t0.clear()
arg = 'Penning up TURTLES...'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

#penup
t1.penup()
t2.penup()
t3.penup()
t4.penup()
t5.penup()
t6.penup()
t7.penup()
t8.penup()
t9.penup()
t10.penup()
t11.penup()
t12.penup()
t13.penup()
t14.penup()
t15.penup()
t16.penup()
t17.penup()
t18.penup()
t19.penup()

o2.penup()
o3.penup()
o4.penup()
o5.penup()
o6.penup()
o7.penup()
o8.penup()
o9.penup()
o10.penup()
o11.penup()
o12.penup()
o13.penup()
o14.penup()
o15.penup()
o16.penup()
o17.penup()
o18.penup()
o19.penup()

#progressbar skrift
t0.clear()
arg = 'Done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(50)
time.sleep(0.5)

t0.clear()
arg = 'Positioning TURTLES...'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

#goto
t1.goto(00,-20)
t2.goto(00,-20)
t3.goto(00,-20)
t4.goto(00,-20)
t5.goto(00,-20)
t6.goto(00,-20)
t7.goto(00,-20)
t8.goto(00,-20)
t9.goto(00,-20)
t10.goto(00,-20)
t11.goto(00,-20)
t12.goto(00,-20)
t13.goto(00,-20)
t14.goto(00,-20)
t15.goto(00,-20)
t16.goto(00,-20)
t17.goto(00,-20)
t18.goto(00,-20)
t19.goto(00,-20)

#progressbar skrift
t0.clear()
arg = 'Halfway done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(25)

#goto
o2.goto(0,60)
o3.goto(0,60)
o4.goto(0,60)
o5.goto(0,60)
o6.goto(0,60)
o7.goto(00,60)
o8.goto(00,60)
o9.goto(00,60)
o10.goto(00,60)
o11.goto(00,60)
o12.goto(00,60)
o13.goto(00,60)
o14.goto(00,60)
o15.goto(00,60)
o16.goto(00,60)
o17.goto(00,60)
o18.goto(00,60)
o19.goto(00,60)

#progressbar skrift
t0.clear()
arg = 'Done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(25)
time.sleep(0.5)

t0.clear()
arg = 'Speeding up TURTLES...'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

#speed
t.speed(0)
t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)
t5.speed(0)
t6.speed(0)
t7.speed(0)
t8.speed(0)
t9.speed(0)
t10.speed(0)
t11.speed(0)
t12.speed(0)
t13.speed(0)
t14.speed(0)
t15.speed(0)
t16.speed(0)
t17.speed(0)
t18.speed(0)
t19.speed(0)

o2.speed(0)
o3.speed(0)
o4.speed(0)
o5.speed(0)
o6.speed(0)
o7.speed(0)
o8.speed(0)
o9.speed(0)
o10.speed(0)
o11.speed(0)
o12.speed(0)
o13.speed(0)
o14.speed(0)
o15.speed(0)
o16.speed(0)
o17.speed(0)
o18.speed(0)
o19.speed(0)

#progressbar skrift
t0.clear()
arg = 'Done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(50)
time.sleep(0.5)

t0.clear()
arg = 'Installing angles TURTLES...'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

#vinkel

t1.lt(-110)
t2.lt(-30)

t4.lt(30)
t5.lt(70)
t6.lt(30)

t8.lt(-30)
t9.lt(-70)

t10.lt(160)
t11.lt(10)
t12.lt(180)
t13.lt(190)
t14.lt(-120)
t15.lt(-400)
t16.lt(360)
t17.lt(195)
t18.lt(355)
t19.lt(270)

o2.lt(-30)

o4.lt(30)
o5.lt(70)
o6.lt(30)

o8.lt(-30)
o9.lt(-70)

o10.lt(160)
o11.lt(10)
o12.lt(180)
o13.lt(190)
o14.lt(-120)
o15.lt(-400)
o16.lt(360)
o17.lt(195)
o18.lt(355)
o19.lt(0)


#progressbar skrift
t0.clear()
arg = 'Done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(50)
time.sleep(0.5)

t0.clear()
arg = 'Making Creeper..'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

#creeper maskin
t.goto(-50,0)
creeper()

#main turtle transform
t.shape('rock.gif')
t.penup()
t.goto(100,-20)
t.lt(110)

#progressbar skrift
t0.clear()
arg = 'Done.'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))

ned_teller.fd(50)
time.sleep(0.5)

#CoutDown prep
t0.clear()
ned_teller.clear()
ned_teller.hideturtle()


time.sleep(1)
ned_teller.penup()
ned_teller.goto(0,200)

arg = 'CountDown'
t0.write(arg,move = False, align = 'center', font = ('Arial', 11, 'normal'))


#CoutDown

ned_teller.color('green')
arg = '3'
ned_teller.write(arg,move = False, align = 'center', font = ('Arial', 45, 'normal'))

time.sleep(1)
ned_teller.clear()

ned_teller.color('blue')
arg = '2'
ned_teller.write(arg,move = False, align = 'center', font = ('Arial', 45, 'normal'))

time.sleep(1)
ned_teller.clear()

ned_teller.color('red')
arg = '1'
ned_teller.write(arg,move = False, align = 'center', font = ('Arial', 45, 'normal'))

time.sleep(1)
ned_teller.clear()

#Action prep
t0.clear() 
t0.goto(0,-20)

t.clear() #clearing creeper

t0.speed(2)
#bevegelse
for i in range(50):
    if i < 7:
        t0.fd(5)
        t0.bk(10)
        t0.fd(5)

    t.fd(20)
    t1.fd(-20)
    t2.fd(-20)
    t3.fd(-20)
    t4.fd(-20)
    t5.fd(-20)
    t6.fd(20)
    t7.fd(20)
    t8.fd(20)
    t9.fd(20)
    t10.fd(20)
    t11.fd(20)
    t12.fd(20)
    t13.fd(20)
    t14.fd(20)
    t15.fd(20)
    t16.fd(20)
    t17.fd(20)
    t18.fd(20)
    t19.fd(20)


    o2.fd(20)
    o3.fd(20)
    o4.fd(20)
    o5.fd(20)
    o6.fd(20)
    o7.fd(20)
    o8.fd(20)
    o9.fd(20)
    o10.fd(20)
    o11.fd(20)
    o12.fd(20)
    o13.fd(20)
    o14.fd(20)
    o15.fd(20)
    o16.fd(20)
    o17.fd(20)
    o18.fd(20)
    o19.fd(20)

    
    #showturtle
    if i < 1: 
        t0.showturtle()
        t.showturtle()
        t1.showturtle()
        t2.showturtle()
        t3.showturtle()
        t4.showturtle()
        t5.showturtle()
        t6.showturtle()
        t7.showturtle()
        t8.showturtle()
        t9.showturtle()
        t10.showturtle()
        t11.showturtle()
        t12.showturtle()
        t13.showturtle()
        t14.showturtle()
        t15.showturtle()
        t16.showturtle()
        t17.showturtle()
        t18.showturtle()
        t19.showturtle()

        o2.showturtle()
        o3.showturtle()
        o4.showturtle()
        o5.showturtle()
        o6.showturtle()
        o7.showturtle()
        o8.showturtle()
        o9.showturtle()
        o10.showturtle()
        o11.showturtle()
        o12.showturtle()
        o13.showturtle()
        o14.showturtle()
        o15.showturtle()
        o16.showturtle()
        o17.showturtle()
        o18.showturtle()
        o19.showturtle()

t.done()
