### PART ONE ###
"""
def parse_round(game_data: str) -> list[dict[str: int]]:
    data = {"blue": 0, "red": 0, "green": 0}
    game = game_data.split(", ")

    for dice in game:
        for colour in data:
            if colour in dice:
                data[colour] = int(dice.replace(colour, ""))
                break

    return data


def parse_game(game_data: str) -> list[dict[str: int]]:
    data = {"blue": 0, "red": 0, "green": 0, "min_dice": 0}
    games = game_data.split("; ")

    for game in games:
        round_data = parse_round(game)
        for colour, quantity in round_data.items():
            data[colour] += quantity

        data["min_dice"] = max(data["min_dice"], sum([v for k,v in data.items() if k != "min_dice"]))
    print("pg", data)
    return data


def validate_game(game_data: str,
                  red: int = 12,
                  green: int = 13,
                  blue: int = 14) -> int:
    header, data = game_data.split(": ")
    game_id = int(header[4::])

    dice = parse_game(data)
    total_dice = sum(dice.values())

    valid = False
    total = red+blue+green

    if red > dice["red"] and blue > dice["blue"] and green > dice["green"] and total > total_dice:
        valid = True
    
    return game_id if valid else 0
"""

def validate_dice(dice: str, colour: str):
    if colour in dice:
        number = int(dice.replace(colour,""))
        return number
    return 0


def validate_game(game_data: str,
                  red: int = 12,
                  green: int = 13,
                  blue: int = 14) -> int:
    min_dice = {"red": 0, "green": 0, "blue": 0}
    
    header, data = game_data.split(": ")
    game_id = int(header[4::])

    rounds = data.split("; ")
    
    for play in rounds:
        dice = play.split(", ")
        for colour in dice:
            r = validate_dice(colour, "red")
            g = validate_dice(colour, "green")
            b = validate_dice(colour, "blue")

            min_dice["red"] = max(r, min_dice["red"])
            min_dice["green"] = max(g, min_dice["green"])
            min_dice["blue"] = max(b, min_dice["blue"])
            
            # print(r,g,b)
            # if not(r and b and g):
            #     return 0
            # if r > red or b > blue or g > green:
            #     return 0
            
    ### PART ONE ###
    # return game_id

    ### PART TWO ###
    prod = 1
    for v in min_dice.values():
        prod *= v
    return prod
    


def load_file(file="20231202_data.txt"):
    with open(file) as data:
        # return sum([validate_game(game) for game in data])
        
        total = 0
        for game in data:
            score = validate_game(game)
            print(game)
            print(score)
            print()
            total += score
        return total
