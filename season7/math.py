from random import randint
score = 0
while True:
    num1 = randint(1, 30)
    num2 = randint(1,30)
    false_result = randint(-3,3)
    sum = num1 + num2+ false_result
    print("{} + {} = {}".format(num1,num2,sum))

    answer = input("F or T ? ").lower()

    if false_result == 0:
        if answer =="t":
            score +=1
            print("Your score: {}".format(score))
        if answer =="f":
            print("Game over")
            break

    if  false_result != 0:
        if answer =="t":
            print("Game over")
            break
        if answer =="f":
            score +=1
            print("Your score: {}".format(score))
    
