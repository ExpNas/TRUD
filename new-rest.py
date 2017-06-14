import random
import re
valid_chars = " '-+"

class Serving:
    def __init__(self,name):
        self.name = name
        self.time=self.calc_time()
        
    def calc_time(self):
        return random.randint(0, 50)
    
    def to_print(self):
        print('{0}{1}{2}{3}minutes'.format(self.name, (31 - self.name.__len__())*'.', self.time, ((3 - int(len(str(self.time))))*' ')))
        
    def is_valid_name(self):
        for word in ''.join([w for w in list(self.name) if not w in valid_chars]).split():
            if not word.isalpha():
                return False
        return True


class Dish(Serving):
    pass
  
  
class Drink(Serving):
    def __init__(self,name):
        super().__init__(name)
        self.time = 5

    
def wwyl(item):
    dishes_string = input(f'What would you like to {data[item]}?(Use comma to separate) ')  
    dishes_list = re.split(',+', dishes_string)
    dishes_set = {dish.strip().title() for dish in dishes_list}
    try:
        my_class = eval(item)
    except NameError:
        my_class = type(item, (Dish,), {})
    
    # creating list of class Dishes
    dishes = [my_class(dish) for dish in dishes_set if (dish and my_class(dish).is_valid_name())]
     
    # printing list of class Dishes
    print('\n%s                     Time for cooking' % item)
    for dish in dishes:
        dish.to_print()
    print('\n')
            
    
data = {'Dish':'eat',
 #       'Drink':'drink',
 #       'Snack':'crunch',
        'Alcohol':'buzz',
 #       'Song':'sing',
 #       'Taxi':'go to'
        }
    
for item in data:
    wwyl(item)    
