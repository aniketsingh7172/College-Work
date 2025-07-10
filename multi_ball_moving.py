from tkinter import*
import random
import time
t=Tk()
t.title('Multi ball Moving')
c=Canvas(t,width=1500,height=800)
c.pack()
class Ball:
    def __init__(self,color,size):
        self.ball=c.create_oval(10, 10, size, size, fill=color, outline=color)
        # self.ball = c.create_rectangle(10, 10, size, size, fill=color, outline=color)
        self.x=random.randrange(1,20)
        self.y=random.randrange(1,30)
    def anim(self):
        c.move(self.ball, self.x, self.y)
        pos = c.coords(self.ball)
        if pos[3] >= 800 or pos[1] <= 0:
            self.y = -self.y
        if pos[2] >= 1500 or pos[0] <= 0:
            self.x = -self.x

# s=random.randint(40,60)
balls=[]
c0=['red','blue','green','yellow','magenta','cyan','black']
for i in range(500):
    balls.append(Ball(c0[i%7],random.randrange(60,100)))
while True:
    for j in balls:
        j.anim()
    t.update()
    time.sleep(0.00000001)
