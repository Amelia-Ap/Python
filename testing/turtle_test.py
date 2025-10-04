import turtle

for k in range(20,4,-2):
    print(k)

t = turtle.Turtle()
t.color("blue")
Tupel=(1,2,3)
Tupel2=(1,2,3)

print(Tupel, Tupel2)

# Draw a regular polygon with a specific sidelength and amount of edges and
def polygon(sidelength, amount_of_edges):
    for i in range(amount_of_edges):
        t.forward(sidelength)
        t.right(180-180*(amount_of_edges-2)/amount_of_edges)

polygon(40, 3)
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