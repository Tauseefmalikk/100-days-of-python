enemies=1
def increase_enemies():
    enemies=2
    print(f"enemies inside function:{enemies}")

increase_enemies()
print(f"enemies inside function:{enemies}")
 
    
#local scope

def player():
    player=2
    print(player) 
player()
    
    
#global scope
player=4
def coach():
    coach=2
    print(player)
coach()

