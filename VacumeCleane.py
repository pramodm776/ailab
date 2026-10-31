# 1. Design and implement a simple reflex agent for the Vacuum Cleaner world and analyze its rational behavior in a given environment.
# environ ment

room = {
    'A':'Dirty',
    'B':'Dirty'
}

position = 'A';

def vacume_cleaner(position, room):
    if room[position] == 'Dirty':
        print("room", position, "is Dirty. Cleaning....." )
        
        room[position] = 'Clean';
    
    elif position == 'A':
        
        print("Room A is clean. Moving to the Right")
        position = 'B' 
        
    elif position == 'B':
        print("Room B is Clean. Moving to the Left")
        position == 'A'   
        
        
    return position




for i in range(5):
    
    print("\nSteps", i+1)
    
    position = vacume_cleaner(position, room)
    
    print("Current Environment", room)
    print("Current Room", position)
    
    
print("\nFinal Environment", room)
    
    

