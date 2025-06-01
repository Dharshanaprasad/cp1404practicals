# A menu-based program to work with scores

def main():
    score = get_valid_score()
    choice = ""
    while choice.upper() != "Q":
        print("\nMenu:\n(G)et score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input("Choose an option: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print("Result:", get_score_result(score))
        elif choice == "S":
            print("*" * int(score))
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid choice")

def get_valid_score():
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Try again.")
        score = float(input("Enter a valid score (0-100): "))
    return score

def get_score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
