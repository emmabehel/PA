import random 
import tabulate
import timeit

def one_dimension(steps):
    x = 0
    counter = 0
    
    for i in range(steps):
        
        direction=random.choice(["left","right"])
        if direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
            
        if x == 0:
            counter += 1
            break
    return counter
      
def two_dimension(steps):
    x = 0
    y= 0
    counter_2d = 0
    
    for i in range(steps):
        
        direction = random.choice(["left", "right", "up", "down"])
        if direction == "left":
            x -= 1
        if direction == "right":
            x += 1
        if direction == "up":
            y += 1
        elif direction == "down":
            y -= 1
        
        if x == 0 and y == 0:
            counter_2d += 1
            break
    return counter_2d


def three_dimension(steps):
    x = 0
    y = 0
    z = 0
    counter_3d = 0
    
    for i in range(steps):
        
        direction = random.choice(["left", "right", "up", "down", "in", "out"])
        if direction == "left":
            x -= 1
        if direction == "right":
            x += 1
        if direction == "up":
            y += 1
        if direction == "down":
            y -= 1
        if direction == "in":
            z += 1
        elif direction == "down":
            z -= 1
        
        if x == 0 and y == 0 and z == 0:
            counter_3d += 1
            break
    return counter_3d


def main():
    steps = [20, 200, 2000, 20000, 200000, 2000000]
    
    table = []
    time_table = []
       
    for i in steps:
        one_dimension_100 = 0
        two_dimension_100 = 0
        three_dimension_100 = 0
        
        for j in range(100):
            one_dimension_result = one_dimension(i)
            two_dimension_result = two_dimension(i)
            three_dimension_result = three_dimension(i)
            
            if  one_dimension_result == 1:
                one_dimension_100 += 1
            if  two_dimension_result == 1:
                two_dimension_100 += 1
            if  three_dimension_result == 1:
                three_dimension_100 += 1
        
    
    
        table.append([f'{i} steps', f'1D: {one_dimension_100}%', f'2D: {two_dimension_100}%', f'3D: {three_dimension_100}%'])
        three_dimension_time = timeit.timeit(lambda: three_dimension(i), number = 100)
        time_table.append([f'{i} steps {three_dimension_time} seconds'])

    headers = ["Number of steps", "1D", "2D", "3D"]
    headers_time = ["Number of Steps", '3D']
    table_percentage = tabulate.tabulate(table, headers, tablefmt="grid")    
    time_table_seconds = tabulate.tabulate(time_table, headers_time, tablefmt = "grid")
        
        
    print(table_percentage)
    print(time_table_seconds)


    

        
main()