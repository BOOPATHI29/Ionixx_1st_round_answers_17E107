"""

3. Design an algorithm which helps a man to travel from A-D with minimum cost and time.
Given route points (consider travel by bus for example). below are the route points the
country supports
A - B (Cost 50, KM - 100)
B - C (Cost 100, KM - 50)
A - C (Cost 75 , KM- 150)
C - D (Cost 50 , KM - 100)
A - D (Cost 150, KM-150)

"""



def min_cost_recursive(cost,s,d): #s -> source and d -> destination cost => matrix 
    
    if s==d: #if source is same as distination  eg : A -> A , B-> B ..    
        return cost[s][s] # if condition is true means, it executes
    
    minn=cost[s][d] #direct ticket from source to destination . minn gets initialized and starts to compare interal paths (A->C->D , A->B->C->D , etc)
    
    for i in range(s+1,d): #This loop finds minimum with every intermediate nodes s=1,d=3.
        c=min_cost_recursive(cost,s,i)+min_cost_recursive(cost,i,d) # recursive function inorder to get if there is a minimum cost than minn
        
        if c<minn: # if there is a minimum cost then it updates the minn
            minn=c # minimum cost updated in  minn
            
    return minn # returning the values
    
#-------------------------------------------------------------------------------------------------------------------------------#
#Here is the main program

inf=9999 #some range integer bcz it says there is no values .
        # if we add it , it gives more than minimum number so that we can came to know , the path doesn't .
        
n=4 # 4 stations (A,B,C,D)


cost=[[0,50,75,150],[inf,inf,100,inf],[inf,inf,inf,50],[inf,inf,inf,0]] #matrix representation of given data in Question


print("The Minimum cost to reach station A -> D is",min_cost_recursive(cost,0,n-1))  # printing the retrun result
