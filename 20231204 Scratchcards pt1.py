### PART ONE ###

def score(winnings: list[int], numbers: list[int]) -> int:
    count = 0

    for num in numbers:
        if num in winnings:
            count += 1

    return int(2**(count-1))


def load_file(file="20231204_data.txt"):
    total = 0
    
    with open(file) as data:
        for line in data:
            card_header, card_data = line.split(": ")
            
            card_id = int(card_header[4::])

            winnings, numbers = [[int(n) for n in nums.split(" ") if n != ""] for nums in card_data.split(" | ")]

            #winnings = [int(n) for n in winnings.split(" ")]
            #numbers = [int(n) for n in numbers.split(" ")]

            total += score(winnings, numbers)
        
    # return winnings, numbers
    return total


print(load_file())
