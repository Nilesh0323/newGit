from PIL import Image

from fpdf import FPDF

img=Image.open("file/bg.png")
sizeOfSheet=img.width
gap,_=0,0
allowedchar='qwertyuiopasdfghjklzxcvbnm(),.?;1234567890'

def Write(char):
    if char=='\n':
        pass
    else:
        global gap,_
        char.lower()
        try:
            cases=Image.open("file/"+char+".png")
            print("cases working")
        except:
            cases=Image.open("file/q.png")
        img.paste(cases,(gap,_))
        size=cases.width
        gap+=size
        del cases

def Letters(word):
    print(word)
    global gap,_
    if gap > sizeOfSheet-95*(len(word)):
        gap=0
        _+=200
    for letter in word:
        print(letter)
        if letter in allowedchar:
            if letter.islower():
                pass
            elif letter.isupper():
                letter.lower()
                letter+='Upper'
            elif letter=='.':
                letter="fullstop"
            elif letter==',':
                letter="comma"

            elif letter==':':
                letter="colon"
            elif letter=='!':
                letter="exclamation"
            elif letter=='?':
                letter="question"

            elif letter=='(':
                letter="bracketclose"
            elif letter==')':
                letter="bracketclose"

            Write(letter)


def Word(Input):
    print(Input)
    wordlist=Input.split(' ')
    print("kis")
    print(wordlist)
    for i in wordlist:
        Letters(i)
        Write('space')




if __name__=='__main__':

    try:
        with open("file/black.txt",'r') as file:
            print("nilesh")
            data=file.read().replace('\n','')
            l=len(data)
            nn=len(data)//600
            print(nn)
            print(l)
            chunks,chunk_size=len(data),len(data)//nn+1
            p=[data[i:i+chunk_size] for i in  range(0,chunks,chunk_size)]
            print(p)
            print(len(p))
            print("before for")
            exit

            for i in range(0,len(p)):
                Word(p[i])
                Write('\n')
                img.save("file/%doutt.png"%i)
                img1=Image.open("file/bg.png")
                img=img1
                gap,_=0,0
    except ValueError as E:
        print("{}\nTry again",format(E))
    imageList=[]
    for i in range(0,len(p)):
        imageList.append("file/%doutt.png"%i)

    cover=Image.open(imageList[0])
    width,height=cover.size
    pdf=FPDF(unit="pt",format=[width,height])
    for i in range(0,len(imageList)):
        pdf.add_page()
        pdf.image(imageList[i],0,0)
    pdf.output("file/neww_2.pdf","F")





