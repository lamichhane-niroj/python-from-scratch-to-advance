#qn 1
with open('poem.txt','r') as f:
    txt =  f.read()

if 'twinkle' in txt:
    print("present")
else:
    print("not present")


#qn 2
score = 120
f = open('highscore.txt','r')
highscore = f.read()
highscore = int(highscore)
f.close()

if score>highscore:
    f = open('highscore.txt','w')
    f.write(str(score))
    f.close()


#qn 3
f = open('sample.txt','r')
txt =  f.read()
f.close()

newtxt = txt.replace("fool", "####")
f = open('sample.txt','w')
f.write(newtxt)
f.close()

