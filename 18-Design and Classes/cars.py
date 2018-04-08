import datetime 

# Define the class
class Car(object):
    """
    represents color, x,y and direction.     
    """
    def __init__(car, color, location, dirtn):
        
            car.color = color
            car.location = location
            car.y = location[1]
            car.x = location[0]
            car.dirtn = dirtn
        
    def go(car,l):
        if car.dirtn == 'N':
            car.location.y =car.location.y+l
            return print(car)
        elif car.dirtn == 'S':
            car.location.y =car.location.y-l
            return print(car)
        elif car.dirtn == 'E':
            car.location.x =car.location.x+l
            return print(car)
        elif car.dirtn == 'W':
            car.location.x =car.location.x-l
            return print(car)
        else:
            return
    
    def turn_right(car):
        if car.dirtn =='N':
            car.dirtn = 'E'
        elif car.dirtn =='S':
            car.dirtn = 'W' 
        elif car.dirtn =='E':
            car.dirtn = 'S'
        elif car.dirtn =='W':
            car.dirtn = 'N'
        
        else:
            print ('Null')
    
    def turn_left(car):
        if car.dirtn =='N':
            car.dirtn = 'W'
        elif car.dirtn =='S':
            car.dirtn ='E' 
        elif car.dirtn =='E':
            car.dirtn = 'N'
        elif car.dirtn =='W':
            car.dirtn = 'S'
        
        else:
            print ('Null')
			
			
    def print_cars(car):
        print(str(car.color), 'the location of car is', str(car.location), 'and directed towards', str(car.dirtn))			