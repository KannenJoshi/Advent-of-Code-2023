### PART TWO ###

def process_card(data):
    card_header, card_data = data.split(": ")
    card_id = int(card_header[4::])
    winnings, numbers = [[int(n) for n in nums.split(" ") if n != ""] for nums in card_data.split(" | ")]
    return [card_id, winnings, numbers]


def score(card_id: int, winnings: list[int], numbers: list[int]) -> list[int]:
    count = 0

    for num in numbers:
        if num in winnings:
            count += 1

    return [card_id+i for i in range(1,count+1)]


def load_file(file="20231204_data.txt"):
    cards = []
    scores = {}

    with open(file) as data:
        for line in data:
            card = process_card(line)
            cards.append(card[0])
            scores[card[0]] = list(score(*card))

    pointer = 0

    while pointer < len(cards):
        # cid, wins, nums = cards[pointer]

        card = cards[pointer]
        cards.extend(scores[card])

        pointer += 1
        
    # return winnings, numbers
    return len(cards)


print(load_file())
