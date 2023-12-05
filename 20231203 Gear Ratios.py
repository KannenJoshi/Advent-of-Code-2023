### PART ONE ###

def check_schematic(schematic: dict, WIDTH: int, HEIGHT: int):
    
    ###
    
    def is_part(x: int, y: int) -> bool:
        for row in range(-1,2):
            for col in range(-1,2):
                if row == col and col == 0:
                    continue
                
                check_x = x + col
                check_y = y + row
                
                if check_x < 0 or check_x >= WIDTH:
                    continue
                if check_y < 0 or check_y >= HEIGHT:
                    continue

                symbol = schematic.get((check_x, check_y), False)
                if symbol and not symbol.isnumeric():
                    return True
        return False


    def is_numeric(x: int, y: int) -> bool:
        symbol = schematic.get((x,y), False)
        return symbol.isnumeric() if symbol else symbol
    
    ###
    
    valid = False
    number = 0
    total = 0
    
    for coord, symbol in schematic.items():
        # If symbol ignore
        if not symbol.isnumeric():
            continue
        
        x,y = coord
        number = 10*number + int(symbol)

        # If the current digit is a part
        if is_part(x,y):
            valid = True

        # If next is not a number
        if not is_numeric(x+1,y):
            # If was a part then add
            if valid:
                total += number
            # Reset
            number = 0
            valid = False

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


print(load_file())
