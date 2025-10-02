import turtle

for k in range(20,4,-2):
    print(k)

t = turtle.Turtle()
t.color("green")
Tupel=(1,2,3)
Tupel2=(1,2,3)

print(Tupel, Tupel2)
def polygon(k):
    for i in range(k):
        t.forward(50)
        t.right(180-180*(k-2)/k)

polygon(5)
turtle.done()

'''
polygon(4)
t.left(45)
t.forward(50)
t.right(45)
t.forward(50)
t.right(135)
t.forward(50)
t.left(45)
t.forward(50)
t.left(135)
t.forward(50)
t.left(45)
t.forward(50)
'''