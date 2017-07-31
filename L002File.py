#coding utf-8
def writeFile():
    f=open(r'C:\Python\Python36\workspace\1.txt','w')
    f.write("hello")
    f.write("lijingjing")
    f.write("good")
    f.close()
    print("write done,写完了")

#read file function
def readFile():
    r=open(r'C:\Python\Python36\workspace\1.txt',"r")
    r.read()
    print("read:"+r.readline())
    r.close()
writeFile()
readFile()
