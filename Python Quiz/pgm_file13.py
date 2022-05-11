from datetime import datetime
import time
fin=open("answer.txt","a")
fout=open("quizqns.txt","r")
data=fout.readlines()
#print(data)
print('Hi welcome to Quiz')
name=input("Enter your name")
score=0
for row in data:
    Q=row.split('ans')
    print("Question")
    print(Q[0])
    print('options :')
    print(Q[1])
    inp=input("Enter your answer-1,2,3,4 or pass")
    print(Q[2])
    if inp.isalpha():
        continue
    elif int(inp)==int(Q[2]):
        score=score+10
    else:
        score=score-5
    op=input("Do you want to continue?y/n")
    if op=="n" or op=="N":
        break
        
print("Score is:",score)       
l=[name,"\t",str(score),"\t"]
fin.writelines(l)
fin.write("\t")
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
fin.write(f"{date}")
fin.write("\n")
fout.close()
fin.close()
    
    
    
    
    
