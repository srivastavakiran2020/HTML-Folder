import random

# set up the game variables
secret = random.randint(1, 50)
attempts = 5

print("Guess a number between 1 to 50.")
print("You have", attempts, "attempts.")
guess = int(input("Enter your number(1 to 50 only!):- "))
while guess == secret:

    if guess == secret:
       print("You are correct! The number was:- " + secret)
else:
    print("You were wrong! The number was actually:- ", secret, "! -1 attempt. ")
    print("Hints: Temperatures of the Earth like: 🧊 absolute zero, 🥶 bitter cold, 🥵 heatwave, 🔥 very hot.")
