score = int(input("Enter the score:"))
if score > 100 or score < 0: 
    print("The score is not valid")
elif score <40:
    print("you are failed")
elif score >=50 and score <=59:
    print("Congratulations, you are 2nd class pass")
elif score >=60 and score <=90:
    print("you are excellent")
else:
    print("Sorry, you are awesome")