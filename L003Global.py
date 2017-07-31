
def changeNum(x):
    y=50
    print("y:%d"%y,"x:",x)
    x=20
    y=20
    print("y change to %d"%y,"x change to",x)

global y
x=50
changeNum(x)
print("x still is",x)

assert 2==1,"2!=1"
