from turtle import *
n = int(input("So canh ma ban muon:"))
shape ("turtle")
for i in range(n):
    forward(200)
    right(180-((n-2)*(180/n)))
mainloop()