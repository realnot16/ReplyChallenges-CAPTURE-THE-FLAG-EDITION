table=[]
found=[]

def main():
    f = open("challenge.txt", "r")
    next(f)

    #read words
    words=[]

    w=False
    for x in f:
        if x=="\n":
            next(f)
            next(f)
            w=True
        if not w:
            x=x.split("\n")[0]
            x= x.split(" ")
            x.pop()
            table.append(x)
        if w:
            x = x.split("\n")[0]
            words.append(x)


    words.pop(0)
    # print(table)
    # print(words)
    

    for y,row in enumerate(table):
        for x,item in enumerate(row):
            #print("START SEARCH FOR "+str(table[y][x]))
            if not table[y][x]==0:
                for word in words:
                    
                    positions=[]
                    if word[0]==table[y][x]:
                        l=[y,x]
                        positions.append(l)
                        dir=0
                        change=False
                        move(word,1,y,x,positions,dir,change)

                        # print("DELETING FOLLOWING POSITIONS")
                        # print (positions)
                        # print("END FOR THE WORD "+word)

                        moveDiagonal(word,1,y,x,positions,dir)


    #TABELLA FINALE
    print("------------------")
    print(table)
    print("TOTAL WORDS "+str(len(words)))
    print("WORDS FOUND "+str(len(found)))
    # #PAROLE RESIDUE
    # print(defW)
    #CALCOLO IL CODICE FINALE
    res=""
    for x in table:
        for y in x:
            if not y==0:
                res+=str(y)
    print(res)
    print(found)


    words.sort()
    found.sort()

    if words ==found:
        print("AEEA")


def move(word,ind,y,x,positions,dir,change):

    if len(word)<ind:
        return    
    
    # if(word == "DOWNCAST"):
    #     print("RICORSIONE N"+str(ind)+" per la parola "+word+"  -----MI MUOVO DA QUI "+str(y)+" "+str(x)+" cercando "+word[ind])
    #     print(positions)

    movimenti=[]

    if (y+1)<len(table):
        if table[y+1][x]==word[ind]:
                movimenti.append([y+1,x,2])
    if (y-1)>0:
        if table[y-1][x]==word[ind]:
            movimenti.append([y-1,x,1])

    if (x+1)<len(table[y]):
        if table[y][x+1]==word[ind]:
            movimenti.append([y,x+1,3])
    if(x-1)>0:
        if table[y][x-1]==word[ind]:
            movimenti.append([y,x-1,4])
    
    for m in movimenti:
        dir2 = dir
        pos = positions.copy()
        change2 = change
        # if(word == "SQUEEZE"):
        #         print("movimento accettato, partenza da "+str(y)+"-"+str(x)+" --"+str(dir)+"  -"+str(m[2]))
        #         print(m)
        if(word[ind] == table[m[0]][m[1]]and [m[0],m[1]] not in pos):

            if(ind+1==len(word)):
                if change==False or dir2==m[2]:
                    pos.append([m[0],m[1]])
                    #print("ho trovato "+ word +" ind "+str(dir)+" --la parola è lunga "+str(len(word))+" sarann ocancellate "+str(len(pos))+" righe")

                    found.append(word)
                    for i,p in enumerate(pos):
                        for t in enumerate(pos[i:],i):
                            if p==t:
                                print("errore su parola "+word)
                                print(pos)
                                print(p)
                                
                        table[p[0]][p[1]]=0
            else:
                if dir2==0:
                    dir2=m[2]
                if dir2!=m[2] and not change2:
                    change2=True
                    dir2=m[2]
                if dir2==m[2]:   
                    pos.append([m[0],m[1]])
                    move(word,ind+1,m[0],m[1],pos,dir2,change2)





def moveDiagonal(word,ind,y,x,positions,dir):

    if len(word)<ind:
        return
    # if(word == "THRAHING"):
    #     print("RICORSIONE N"+str(ind)+" per la parola "+word+"  -----MI MUOVO DA QUI "+str(y)+" "+str(x)+" cercando "+word[ind])
    #     print(positions)

    movimenti=[]

    if (y+1)<len(table) and (x+1)<len(table[y]):
        if table[y+1][x+1]==word[ind]:
            movimenti.append([y+1,x+1,2])
    if (y-1)>0 and (x-1)>0:
        if table[y-1][x-1]==word[ind]:
            movimenti.append([y-1,x-1,4])

    if (x+1)<len(table[y]) and (y-1)>0:
        if table[y-1][x+1]==word[ind]:
            movimenti.append([y-1,x+1,1])
    if(x-1)>0 and (y+1)<len(table):
        if table[y+1][x-1]==word[ind]:
            movimenti.append([y+1,x-1,3])
    
    for m in movimenti:
        
        if(word[ind] == table[m[0]][m[1]]):
            # if(word == "THRAHING"):
            #     print("movimento accettato, partenza da "+str(y)+"-"+str(x)+" --"+str(dir)+"  -"+str(m[2]))
            #     print(m)
            dir2=dir
            pos = positions.copy()
            if(ind+1==len(word) and dir2==m[2]):
                pos.append([m[0],m[1]])
                #print("ho trovato "+ word +" ind "+str(dir)+" --la parola è lunga "+str(len(word))+" sarann ocancellate "+str(len(pos))+" righe")
                found.append(word)
                for i,p in enumerate(pos):
                    for t in enumerate(pos[i:],i):
                        if p==t:
                            print("errore su parola "+word)
                            print(pos)
                            print(p)
                    table[p[0]][p[1]]=0
            else:
                if dir2==0:
                    dir2=m[2]
                if dir2==m[2]:   
                    pos.append([m[0],m[1]])
                    moveDiagonal(word,ind+1,m[0],m[1],pos,dir2)

main()