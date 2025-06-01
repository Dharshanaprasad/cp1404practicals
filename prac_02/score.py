# This program asks for a score and prints the result

import random

def main():
    score = float(input("Enter your score (0-100): "))
    result = get_score_result(score)
    print("Result:", result)

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} -", get_score_result(random_score))

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
