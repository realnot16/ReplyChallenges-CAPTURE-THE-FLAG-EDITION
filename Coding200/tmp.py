 for word in words:
        l=[]
        for y,row in enumerate(table):
            # print("LE MIE RIGHE ")
            # print(y)
            # print(row)
            # print("--------")
            for x,column in enumerate(table):
                #check for first word[letter]
                if word[0]==table[y][x]:
                    #print("trovata lettera "+word[0]+" della parola: "+word +" alla posizione "+str(y)+" "+str(x))
                    l=[y,x]



                    br=True
                    tr=True
                    tl=True
                    bl=True
                    down=True
                    up=True
                    right=True
                    left=True

                #     for i,letter in enumerate(word[1:],1):
                #         #VERTICAL SEARCH
                #         #down
                #         if(y+i)<len(table) and down:
                #             if not letter==table[y+i][x]:
                #                 down=False
                #         else:
                #             down=False                        
                #         #up
                #         if(y-i)>0 and up:
                #             if not letter==table[y-i][x]:
                #                 up=False
                #         else:
                #             up=False  
                #         #HORIZONTAL SEARCH
                #         #right
                #         if(x+i)<len(table[y]) and right:
                #             if not letter==table[y][x+i]:
                #                 right=False
                #         else:
                #             right=False        
                #         #left
                #         if(x-i)>0 and left:
                #             if not letter==table[y][x-i]:
                #                 left=False
                #         else:
                #             left=False                         

                #         #DIAGONAL SEARCH
                #         #bot-left
                #         if(y+i)<len(table) and (x-i)>0 and bl:
                #             if not letter==table[y+i][x-i]:
                #                 bl=False
                #         else:
                #             bl=False
                        
                #         #bot-right
                #         if(y+i)<len(table) and (x+i)<len(table[y]) and br:
                #             if not letter==table[y+i][x+i]:
                #                 br=False
                #         else:
                #             br=False

                #         #top-right
                #         if(y-i)>0 and (x+i)<len(table[y]) and tr:
                #             if not letter==table[y-i][x+i]:
                #                 tr=False
                #         else:
                #             tr=False
                        
                #         #top-left
                #         if(y-i)>0 and (x-i)>0 and tl:
                #             if not letter==table[y-i][x-i]:
                #                 tl=False
                #         else:
                #             tl=False

                #         if not (br or tr or tl or bl or up or down or left or right):
                #             break

                #     #FIX TABLE WITH 0 FOR VERTICAL AND HORIZONTAL
                #     if up:
                #         for k,w in enumerate(fixedW):
                #             if w==word:
                #                 fixedW.pop(k)
                #                 break

                #         for i,word in enumerate(word):
                #             table[l[0]-i][l[1]]=0
                #         break
                #     if down:
                #         for k,w in enumerate(fixedW):
                #             if w==word:
                #                 fixedW.pop(k)
                #                 break

                #         for i,word in enumerate(word):
                #             table[l[0]+i][l[1]]=0
                #         break
                #     if right:
                #         for k,w in enumerate(fixedW):
                #             if w==word:
                #                 fixedW.pop(k)
                #                 break

                #         for i,word in enumerate(word):
                #             table[l[0]][l[1]+i]=0
                #         break
                #     if left:
                #         for k,w in enumerate(fixedW):
                #             if w==word:
                #                 fixedW.pop(k)
                #                 break

                #         for i,word in enumerate(word):
                #             table[l[0]][l[1]-i]=0
                #         break
                # #FIX TABLE WITH 0 FOR DIAGONAL     
                #     if bl:
                #         for i,word in enumerate(word):
                #             table[l[0]+i][l[1]-i]=0
                #         for k,w in enumerate(fixedW):
                #             if w==word:
                #                 fixedW.pop(k)
                #                 break
                #         break

                #     if br:
                #         for k,w in enumerate(fixedW):
                #             if w==word:
                #                 fixedW.pop(k)
                #                 break

                #         for i,word in enumerate(word):
                #             table[l[0]+i][l[1]+i]=0
                #         break

                #     if tl:
                #         for k,w in enumerate(fixedW):
                #             if w==word:
                #                 fixedW.pop(k)
                #                 break

                #         for i,word in enumerate(word):
                #             table[l[0]-i][l[1]-i]=0
                #         break

                #     if tr:
                #         for k,w in enumerate(fixedW):
                #             if w==word:
                #                 fixedW.pop(k)
                #                 break
                #         for i,word in enumerate(word):
                #             table[l[0]-i][l[1]+i]=0
                #         break

    # print(table)
    #print(fixedW)