import random
def play(word):
    attempt=0
    dashes="_"*len(word)
    print("_ "*len(word))
    dashes=list(dashes)
    res=""
    #print(dashes)
    temp=word.swapcase()
    temp2=word.upper()
    #print(temp)
    while temp2!=res:
        l=input("ENTER A LETTER...")
        if l in word or l in temp:
            if l in word:
                index=word.index(l)
            if l in temp:
                index=temp.index(l)
            for i in range(index,len(word)):
                if l==word[i] or l== temp[i]:
                    dashes[i]=l.upper()
            res="".join(dashes)
        else:
            attempt=attempt+1
            if attempt==1:
                print(" |======|======\n |\n |\n |\n |\n |\n/|\\")
            elif attempt==2:
                print(" |======|======\n |      O\n |\n |\n |\n |\n/|\\")
            elif attempt==3:
                print(" |======|======\n |      O\n |      |\n |      |\n |\n |\n/|\\")
            elif attempt==4:
                print(" |======|======\n |      O\n |     \|/\n |      |\n |\n |\n/|\\")
            elif attempt==5:
                print(" |======|======\n |      O\n |     \|/\n |      |\n |     / \\\n |\n/|\\")
                break
        print(res)
    if word.upper()==res:
        print("YOU WON!!!")
        print("========================")
        print("word is {}".format(word.upper()))
    else:
        print("YOU LOOSE!!!")
        print("========================")
        print("word is {}".format(word.upper()))
   # print(dashes)

fruits=["Apple","Bannana","Grapes","Orange","Straberry","Watermelon","Tomato"]
r_u_ready=input("ARE U READY TO PLAY!!!!!")
while r_u_ready=='yes':
    word=random.choice(fruits)
    print(word.upper())
    play(word)
    r_u_ready=input("ARE U READY TO PLAY!!!!!")
if r_u_ready!='yes':
    print("====================\nTHANK YOU!!!!")
