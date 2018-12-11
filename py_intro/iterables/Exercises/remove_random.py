import random

#%%
def remove_random(somelist):
    #print(somelist)
    #print(len(somelist))
    removeValue = random.choice(somelist)
    somelist.remove(removeValue)
    return(removeValue)

def main():
    colors = ['red','blue','green','orange']
    #Your code here
    removedColor = remove_random(colors)
    print("The removed color was: ",removedColor)
    print("The remaining colors are: ",colors)

#%%
    
main()
