### PART TWO ###

def check_schematic(schematic: dict, WIDTH: int, HEIGHT: int):
    
    ###
    
    def get_gear(x: int, y: int) -> list:
        adjacent_parts = []
        visited = []
        for row in range(-1,2):
            for col in range(-1,2):
                if row == col and col == 0:
                    continue

                check_x = x + col
                check_y = y + row
                
                if check_x < 0 or check_x > WIDTH:
                    continue
                if check_y < 0 or check_y > HEIGHT:
                    continue


                # Number can be fully on top or below a gear
                # 123
                # .*.
                # ...
                # NOT a gear as 123 is one whole number

                # Check surrounding symbol exists
                coord = (check_x, check_y)
                symbol = schematic.get(coord, False)

                # If number add to visited
                if symbol and symbol.isnumeric():
                    visited.append(coord)

                    # If previous was a number ignore
                    previous = (check_x-1,check_y)
                    if previous not in visited:
                        adjacent_parts.append(coord)
                
        return adjacent_parts if len(adjacent_parts) > 1 else []


    def is_numeric(x: int, y: int) -> bool:
        symbol = schematic.get((x,y), False)
        return symbol.isnumeric() if symbol else symbol


    def get_number(x: int, y: int) -> int:
        """ Assumes x,y is numeric """
        number = schematic[(x,y)]

        # Eval left
        i = 1
        while is_numeric(x-i, y):
            #number += 10*schematic[(x-i,y)]
            number = schematic[(x-i,y)] + number
            i += 1

        # Eval right
        i = 1
        while is_numeric(x+i, y):
            # number *= 10
            # number += schematic[(x-i,y)]
            number += schematic[(x+i,y)]
            i += 1

        return int(number)
        
    
    ###

    total = 0
        
    for coord, symbol in schematic.items():
        # If symbol ignore
        if "*" not in symbol:
            continue
        
        x,y = coord
        ratio = 1

        parts_list = get_gear(x,y)
        
        if len(parts_list) != 2:
            continue

        for part in parts_list:
            # px, py = part

            # ratio *= get_number(px, py)
            p = get_number(*part)
            ratio *= p

        total += ratio

    return total


def load_file(file="20231203_data.txt"):
    schematic = {}
    with open(file) as data:
        h = 0
        w = 0
        # Process Schematic
        
        for y, line in enumerate(data):
            h += 1
            for x, char in enumerate(line):
                if "." in char or "\n" in char:
                    continue
                schematic[(x,y)] = char

            if w == 0:
                w = len(line)

        HEIGHT = h-1
        WIDTH = w

        # Check is Part
    return check_schematic(schematic, WIDTH, HEIGHT)


print(load_file()) #"20231203_test.txt"
