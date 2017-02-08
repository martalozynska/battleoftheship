def read_field(filename):
    '''
    (str) -> (data)
    Reads data from file

    '''
    field = []
    data = {}
    letters = {}
    new_field = []
    file = open(filename,'r')
    rows = file.readlines()
    for row in rows:
        row = row.replace('\n', '')
        new_field.append(row)
    for i in new_field:
        new = list(i)
        field.append(new)
    for x in range(1,11):
        for y in range(1,11):
            data[(x,y)] = field[y-1][x-1]
    return data



def has_ship(field,coord):
    '''
    (data, tuple) -> (bool)
    
    Checks if the cell contains ship or not

    '''
    let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    coord = (let.index(coord[0]) + 1,coord[1])
    res = field1[coord]
    if res == '*':
        return True
    return False

field1 = read_field("field.txt")
has_ship(field1, ('C',7)) 


def get_left(coord):
    if coord[0] == "A":
        return None
    let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    coord = (let[let.index(coord[0]) - 1], coord[1])
    
    return coord 


def get_right(coord):
    let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if coord[0] == "J":
        return None
    coord = (let[let.index(coord[0]) + 1], coord[1])
    return coord

def get_up(coord):
    if coord[1] == 1:
        return None
    coord = (coord[0], coord[1] - 1)
    return coord

def get_down(coord):
    coord = (coord[0], coord[1] + 1)
    if coord[1] == 10:
        return None
        
    return coord
 
print(get_left(('C',7)))
#print(get_right(('C',1)))
#print(get_up(('C',1)))
#print(get_down(('C',1)))

get_left(('C',7))
get_right(('C',7))
get_up(('C',7))
get_down(('C',7))

def ship_size(data, coord):
    '''
    (data, tuple) -> (bool) 
    Determines the size of the ship 

    '''
    
    size = 0 
    if has_ship(data, coord):
        size = 1
    move_coord = [get_right, get_left, get_up, get_down]
    coord1 = coord          
    for func in move_coord: 
        coord = coord1
        while has_ship(data,func(coord)) == True:
            coord = func(coord)
            size += 1
    return size


ship_size(field1,('C',7))    

def field_to_str(data):
 
    '''
    (data) -> (str) 
    '''
    let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    res = ''
    for num in range(1,11):
        for char in range(1,11):
            tup1 = (char, num)
            res += data[tup1]
        res += '\n'
    return res
    
    file.close()
    
    
field_to_str(field1)