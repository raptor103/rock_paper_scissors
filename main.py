import random


class Player:
    def __init__(self):
        self.choices = ["rock", "paper", "scizors"]

    def get_choice(self):
        return random.choice(self.choices)


def evalute_winner(choice1, choice2):
    matrix = {"rock": ["rock", "scizors"],
                "scizors": ["scizors", "paper"],
               "paper": ["paper", "rock"]}
    if choice1 == choice2:
        return "draw"
    else:
        for k, v in matrix.items():
            if choice1 in v and choice2 in v:
                return k


if __name__ == "__main__":
    P1_choice = Player().get_choice()
    P2_choice = Player().get_choice()
    evaluation = evalute_winner(P1_choice, P2_choice)

    print(P1_choice)
    print(P2_choice)
    print(evaluation)

    if evaluation == "draw":
        print("Nobody wins")
    elif evaluation == P1_choice:
        print("P1 wins")
    else:
        print("P2 wins")