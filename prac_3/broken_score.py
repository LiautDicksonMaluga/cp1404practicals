"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = get_user_score()
    result = return_score_result(score)
    print(result)


def return_score_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        if score > 90:
            return "Excellent"
        if score > 50:
            return "Passable"
        if score < 50:
            return "Bad"


def get_user_score():
    score = float(input("Enter score: "))
    return score


main()