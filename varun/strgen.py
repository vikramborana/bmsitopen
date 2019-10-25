x = "a"
fil = open("f.txt","w")
fil.write(x)
f = open("f.txt","a")
g = open("f.txt","r")
f.write(x)
while(True):
    print(g.read())
    f.write(x)