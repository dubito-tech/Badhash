import string
import random
import math
import os


LevelOne = list(string.ascii_lowercase)
LevelTwo = list(string.ascii_letters)
LevelThree = list(string.ascii_lowercase + string.digits)
LevelFour = list(string.ascii_letters + string.digits)
LevelFive = list(string.ascii_letters + string.digits + string.punctuation)

def clear():
  os.system("clear")

def fileLen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def isPrime(n): 
    if n % 2 == 0 or n < 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def badHash(unhash): 
    customStuff = "åäöÅÄÖ" 
    badList = string.printable + customStuff
    values = {i:l for l,i in enumerate(badList, 1)} 
    primeCount = 0 
    for i in values:
      while True:
        primeCount += 1 
        if isPrime(primeCount): 
          break
      values[i] = primeCount
    output = 1 
    try:
        prodList = [values[letter] for letter in unhash]
        for number in prodList:
            output = output * number
        for i in range(0, len(unhash)):
            if i % len(unhash) == 0:
                output += values[unhash[i]]
            elif i % len(unhash) == 1:
                output *= values[unhash[i]]
            else:
                output -= values[unhash[i]]
    except KeyError or ValueError:
        return "Invalid Characters" 
    output = hex(output) 
    _, output = output.split("x")
    return output 

while True:
    print("Would you like to hash a word, or try to break a hash?")
    grandChoice = input("[hash/break] : ")
    if grandChoice.lower() == "hash":
        print("Enter string:")
        hashTheString = badHash(input(": "))
        print(hashTheString)
        print("\nPress enter to continue...")
        input(": ")
        clear()
    while grandChoice.lower() == "break":
        while True:
            print("Enter the BadHash you want to break")
            breakHash = input(": ")
            try:
              int(breakHash, 16)
              break
            except ValueError:
              print("Needs to be a hexidecimal")
        print("Do you want to use a list or random letters?")
        listOrRandom = input("[list/random] : ")
        if listOrRandom.lower() == "list":
            while True:
                print("\nType in the list's name, please include the file extension (.txt, .word, etc.)")
                fileName = input(": ")
                print("")
                try:
                    print("Please wait while we count the lines...")
                    totalLines = fileLen(fileName) + 1
                    print("Lines counted.")
                    with open(fileName, "r") as listText:
                        for i in range(1, totalLines):
                            trueText = listText.readline()
                            try:
                                trueText, junk = trueText.split("\n")
                            except ValueError:
                                pass
                            try:
                                breaker = badHash(trueText)
                                if breaker == breakHash:
                                    print(str(i) + ": " + trueText + " > " + breaker + " == " + breakHash)
                                    print("The hash is:", trueText)
                                    break
                                else:
                                    print(str(i) + ": " + trueText + " > " + breaker + " =/= " + breakHash)
                            except KeyError:
                                print("The entry contained letters that the cutoff hash does not support. SKIPPING")
                        else:
                            print("The list did not contain the correct string.")
                    break
                except FileNotFoundError:
                    print("\nThat file does not exist, please try again.")
                except KeyboardInterrupt:
                    print("You cancelled the process.")
                    break
            break
        elif listOrRandom.lower() == "random":
            while True:
                print("What level should the wordlist be?")
                print("Level 1: Only lowercase\nLevel 2: Full alphabet\nLevel 3: Lowercase and numbers\nLevel 4: Alphabet and numbers\nLevel 5: Alphabet, numbers and special characters. ")
                randChoiceOne = input("[1-5]: ")
                if randChoiceOne == "1":
                    activeList = LevelOne
                    break
                elif randChoiceOne == "2":
                    activeList = LevelTwo
                    break
                elif randChoiceOne == "3":
                    activeList = LevelThree
                    break
                elif randChoiceOne == "4":
                    activeList = LevelFour
                    break
                elif randChoiceOne == "5":
                    activeList = LevelFive
                    break
                else:
                    print("Choose a correct level.")
            while True:
                try:
                    print("What's the min length of the string?")
                    passMin = int(input(": ")) + 1
                    break
                except ValueError:
                    print("Print a number")
            while True:
                try:
                    print("What's the max length of the string?")
                    passMax = int(input(": ")) + 1
                    break
                except ValueError:
                    print("Print a number")
            print("\nThe process will start now, press CTRL+C to cancel.")
            input(": ")
            pastTries = []
            randAttempts = 1
            while True:
                try:
                    output = ""
                    exist = True
                    for i in range(1, random.randint(passMin, passMax)):
                        output += random.choice(activeList)
                    for thing in pastTries:
                        if output == thing:
                            exist = False
                            break
                    if exist == True:
                        outputHash = badHash(output)
                        if outputHash == breakHash:
                            print("SUCCESS! The hash is:", output)
                            break
                        else:
                            print(str(randAttempts) + ": " + output + " > " + outputHash + " =/= " + breakHash)
                            pastTries.append(output)
                            randAttempts += 1
                except KeyboardInterrupt:
                    print("\nYou cancelled the process.")
                    break
        else:
            print("Please enter a valid response [list/random]")
print("Thanks for using my program!")