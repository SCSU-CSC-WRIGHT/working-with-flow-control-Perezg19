import random
randnum = random.randint(1, 10)
attempts = 3
count = 1
while count <= attempts:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > randnum:
        print("Too high")
    elif guess < randnum:
        print("Too low")
    else:
        print("Correct")
        break
    count += 1
if count == attempts:
    print("Aannnd you're done.")
