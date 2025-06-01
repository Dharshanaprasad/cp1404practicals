# score.py
# This program takes a user's score and provides a rating based on it.

score = float(input("Enter your score: "))
if score < 0 or score > 100:
    print("Invalid score entered.")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")