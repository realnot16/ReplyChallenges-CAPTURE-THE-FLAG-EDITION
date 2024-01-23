import re


table=[]

def main():
    f = open("map.txt", "r")

    #read map
    for x in f:
        x=x.split("\n")[0]
        table.append(x)

    print(table)

    round()



def round():
    table2= table.copy()
    for y in range(0,len(table)):
            for x in range(0,len(table[y])):
                l=[y,x]
                c=countBlackHoles(y,x)
                print(str(l)+" "+table[y][x]+" -- "+str(c))
                if not(c==3 or c==2):
                    table2[y][x]=re.sub("&",".",table2[y][x],1)
                elif c>=3 and isPortal(y,x):
                    print("PORTAL "+str(y)+"  "+str(x))
                elif c>=3:
                    table2[y][x]=re.sub(".","&",table2[y][x],1)
                


def countBlackHoles(y,x):
    c=0
    for i in range(y-1,y+2):
        if i>0 and i<len(table):
            for j in range(x-1,x+2):
                if j>0 and j<len(table[i]):
                    #print("CHECK HOLES "+str(i)+" - "+str(j)+"-----"+str(x)+" - "+str(y)+" ------- "+str(table[i][j]))
                    if (y!=i or x!=j):
                        if table[i][j]=="&":
                            c+=1
    return c

def isPortal(y,x):
    return re.search("[a-z]",table[y][x])
main()