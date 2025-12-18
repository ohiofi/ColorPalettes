import turtle,math
import colorPalettes

screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.tracer(0)
t = turtle.Turtle()

def makeTri(mycolor, size):
  t.color(mycolor)
  t.begin_fill()
  t.forward(size)
  t.lt(180-45)
  t.forward(math.sqrt(size**2+size**2))
  t.lt(180-45)
  t.forward(size)
  t.lt(90)
  t.end_fill()

def makeTriPanel(c1,c2,reps,stripeSize):
  t.pd()
  for i in range(reps,0,-1):
    if i%2==1:
      makeTri(c1,stripeSize*i)
    else:
      makeTri(c2,stripeSize*i)
  t.pu()

def makeQuarterPanel(c1,c2,width,numStripes):
  stripeSize = width / (numStripes/2)
  #t.setheading(0)
  makeTriPanel(c1,c2,numStripes,stripeSize)
  t.forward(stripeSize*numStripes)
  t.lt(90)
  t.forward(stripeSize*numStripes)
  t.lt(90)
  makeTriPanel(c2,c1,numStripes,stripeSize)
  t.forward(stripeSize*numStripes)
  t.lt(90)
  t.forward(stripeSize*numStripes)
  t.lt(90)


def makeFullPanel(c1,c2,width,numStripes,isInverted):
  t.setheading(0)
  t.pu()
  t.forward(width/2)
  t.lt(90)
  t.forward(width/2)
  t.rt(90)
  t.pd()
  width = width/4
  for i in range(4):
    t.setheading(90*i)
    if isInverted:
      t.fd(width*2)
      t.lt(90)
      if i%2==1:
        makeQuarterPanel(c1,c2,width,numStripes)
      else:
        makeQuarterPanel(c2,c1,width,numStripes)
      t.lt(-90)
      t.fd(-width*2)
    else:
      makeQuarterPanel(c1,c2,width,numStripes)
  # t.pu()
  # t.forward(width/2)
  # t.lt(90)
  # t.forward(width/2)
  # t.rt(90)
  # t.pd()

def jump(x,y,gridsize):
  t.setheading(0)
  t.pu()
  t.goto(x-gridsize/2,y-gridsize/2)
  t.pd()


def main(colorscheme = 4):
  gridsize=40
  for row in range(-600//gridsize,600//gridsize):
    for col in range(-1200//gridsize,1200//gridsize):
      jump(col*gridsize,row*gridsize,gridsize)
      cnum = int(math.sqrt((row)**2 + (col)**2))%10
      makeFullPanel(
        colorPalettes.cp[colorscheme]["colors"][cnum],
        colorPalettes.cp[colorscheme]["colors"][(cnum+1)%10],
        ((row*col)%3+2)*gridsize,
        5,
        (row+col)%2==1
      )
      screen.update()
# jump(0,0)
# for i in range(4):
#   t.forward(gridsize)
#   t.lt(90)
  
#makeFullPanel("red","blue",100,8,True)
for i in range(20):
  main(i)
  screen.update()
turtle.mainloop()
