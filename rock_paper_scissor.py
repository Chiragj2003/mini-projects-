import random 

i=j=0
print("press \n1 for rock \n2 for paper \n3 for scissor")

def rock_paper_scissor():
    while (i<5 and j<5):
        a= random.randint(0,2)
        b= int(input("enter your choice "))
        if (a==0 and b==0 ) or (a==1 and b==1 ) or (a==2 and b==2 ):
          print("tie")
        elif (a==0 and b==1 ) or (a==1 and b==2) or (a==2 and b==0):
          i+=1
          print("cpu wins")
        elif (a==0 and b==2 ) or (a==1 and b==0) or (a==2 and b==1):
            j+=1
            print("you wins")
        else:
            print("erroer")
        
   
rock_paper_scissor()
if i>j:
    print("cpu wins 5 round ")
else:
    print("you wins 5 round ")