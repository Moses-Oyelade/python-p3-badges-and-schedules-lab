def badge_maker(name):
    return f"Hello, my name is {name}."
print(badge_maker("Moses"))



names = ["Moses", "Jide", "Alfred"]

def batch_badge_creator(names):
    def badge(name):
        return f"Hello, my name is {name}."
        
    badges = [badge(name) for name in names]
    return badges
    
print(batch_badge_creator(names))
   
   

def assign_rooms(names):
    
    def badge_room(name):
        index = names.index(name)
        return f"Hello, {name}! You'll be assigned to room {index + 1}!"
    return [badge_room(name) for name in names]
    
print(assign_rooms(names))      
    
    

def printer(names):
    for name in batch_badge_creator(names):
        print(name)
        
    for name in assign_rooms(names):
        print(name)
    
    
print(printer(names))
