"""

1. To create a chat like environment, and can keep a character/word to end the chat. At the end
of the chat, the application should be able to answer 3 types of questions.
Eg.
A : Ping
B : Pong
A : Ping
B : quit
Here, quit is the key to end the conversation. After that, 3 questions to popup / analysis
report answering all 3 qns below
1. To know the number of repetition of a character
2. To know the number of repetition of a word
3. To know the length of conversation
Appropriate answers need to be displayed on choosing

"""

l=[]  # to append the input ( so we can find the no. of repitition  words ) 
l1=[] # to append the characters that u have entered as a word
le=0 # to know the length of conversation
while (1): #to get the input continously
    
    s=input() # input
    le+=1 # length of conversation
    
    if s!="quit":
       
        l.append(s) # to append the input if not quit
        
    else:
        
        l.append(s)  # to append the input if quit
        break # if the input is quit ->  while loop ends 
for i in l:
    for j in i:
        l1.append(j) # to append the characters 
f={} # to count the characters using Hashing technique
for i in l:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
f1={}  # to count the words using Hashing technique
for i in l1:
    if i in f1:
        f1[i]+=1
    else:
        f1[i]=1
    

print("Enter \n1. The number of repetition of a character \n2. The number of repetition of a word \n3. The length of conversation")
n1=int(input()) 
if n1==1:
    print("The number of repetition of a character - ",f) # gives count of character
elif n1==2:
    print("The number of repetition of a word - ",f1) # gives count of word
elif n1==3:
    print("The length of conversation - ",le) # gives the length of conversation

