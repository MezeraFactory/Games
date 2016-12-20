
import random
from tkinter import *

def stopProg(e):
    root.destroy()



computerNumber = random.randint(1,10)
root =  Tk()

button1=Button(root,text="Hello World click to close")
button1.pack()
button1.bind('<Button-1>',stopProg)

print('Welcome to guess a number between 1 and 10!')

try:
    guess=int(input(inputstring))
except:
    print("You didn't choose a number")
    exit(0)

while guess != computerNumber:
    if guess > computerNumber:
        guess = int(input("Too high. Choose again "))
    elif guess < computerNumber:
        guess = int(input("Too low. Choose again "))

print("You chose well.  Good job!")

















#y = random.randint(1,4)
#x = 1
#inputstring = 'Input your guess. You have ' + str(y) + ' tries.  '

#try:
#    guess=int(input(inputstring))
#except:
#    print("You didn't choose a number")
#    exit(0)


#while x < y:
#while guess != computerNumber:
#    if guess > computerNumber:
#        print("You're to high. you have ",y-x," guesses left.")
#       guess=int(input('Input your next guess '))
#    elif guess < computerNumber:
#        print("You're to low. you have ", y-x, " guesses left.")
#        guess = int(input('Input your next guess '))
#    else:
#        break
#    x=x+1

#if guess != computerNumber:
#    print("Nice Try!")
#    print("The computer chose ",computerNumber)
#else:
#    print("you guessed right!")
#    print("the number was ", computerNumber)






