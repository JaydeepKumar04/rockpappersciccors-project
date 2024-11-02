import random
sc='''
_ _ _/￣￣￣￣)_ _ _
           _ _ _ _ _)_
          _ _ _ _ _ _ _) 
          _ _ _)
￣￣\_ _ _ _ )  '''
ro='''
    /￣￣￣)
￣￣   ￣_￣)
       _ _ _) 
        _ _)
￣￣\_ _ _)'''
pp='''
_ _ _/￣￣￣ )_ _ _
         _ _ _ _ _ _)_  
       _ _ _ _ _ _ _ _) 
        _ _ _ _ _ _ )
￣￣\_ _ _ _ _ _ )'''
game_images=[ro,pp,sc]
usrc=int(input())
if usrc>=3 or usrc<0:
    print("enter valid choice")
else:
    print(game_images[usrc])
    if usrc==0:
        print("u choosen rock")
    elif usrc==1:
         print("u choosen papper")
    elif usrc==2:
         print("u choosen scissors")
    cmpc=random.randint(0,2)
    print(cmpc)
    if cmpc==0:
        print("computer choosen rock")
    elif cmpc==1:
         print("computer choosen papper")
    elif cmpc==2:
         print("computer choosen scissors")
    print(game_images[cmpc])
    if cmpc==usrc:
        print("\nits a draw")
    elif cmpc==2 and usrc==0:
        print("\nu won")
    elif cmpc==0 and usrc==2:
        print("\nu loose")
    elif cmpc>usrc:
        print("\nu loose")
    elif cmpc<usrc:
        print("\nu won")

