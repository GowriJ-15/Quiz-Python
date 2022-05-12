from datetime import datetime
import time
fin=open("answer.txt","a") #file to store time,score
fout=open("quizqns.txt","r") #file with questions 
data=fout.readlines() #reading file line-wise
#print(data)
print('Hi welcome to Quiz')
name=input("Enter your name")
score=0
for row in data:
    Q=row.split('ans') #splitting each line using 'ans'
    print("Question")
    print(Q[0])
    print('options :')
    print(Q[1])
    inp=input("Enter your answer-1,2,3,4 or pass")
    print(Q[2])
    if inp.isalpha():   #if user passes the qn
        continue
    elif int(inp)==int(Q[2]): #if ans is correct 
        score=score+10
    else:                     #if ans is wrong 
        score=score-5
    op=input("Do you want to continue?y/n")
    if op=="n" or op=="N":
        break
        
print("Score is:",score)       
l=[name,"\t",str(score),"\t"]
fin.writelines(l)
fin.write("\t")
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
fin.write(f"{date}")  #timestamp
fin.write("\n")
fout.close()
fin.close()
    
    
    
    
    
