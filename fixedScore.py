__author__ = 'Mitch Hardy'


def main():#Calculate score and provide assessment to user

    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid Option")
        score = float(input("Enter score: "))
    if score >= 0 and score < 50:
        print("Bad")
    elif score >= 50 and score < 90:
        print ("passable")
    elif score >= 90:
        print("Excellent")



main()