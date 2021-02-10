import random, sys, time
from getkey import getkey

#colours
reset = "\033[0m"
dim = "\033[2m"
underline = "\033[4m"
blue = "\033[1;34m"
red = "\033[1;91m"
green = "\033[1;32m"


#just all of the different passages
strings = [
  "Save your favorite articles to read offline, sync your reading lists across devices and customize your reading experience with the official Wikipedia app.",

  "The Waterloo Bay massacre was a clash between European settlers and Aboriginal Australians that took place on the cliffs of Waterloo Bay near Elliston, South Australia, in late May 1849.",

  "In computing, a printer is a peripheral device which makes a persistent representation of graphics or text, usually on paper. While most output is human-readable, bar code printers are an example of an expanded use for printers.",

  "The first commercial printers generally used mechanisms from electric typewriters and Teletype machines. The demand for higher speed led to the development of new systems specifically for computer use.",

  "In a speed typing contest contestants compete to attain the highest accurate typing speeds. These contests have been common in North America since the 1930s and were used to test the relative efficiency of typing with the Dvorak and QWERTY keyboard layouts.",

  "A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming. Modern computers have the ability to follow generalized sets of operations, called programs.",

  "Since the first dinosaur fossils were recognized in the early 19th century, mounted fossil dinosaur skeletons have been major attractions at museums around the world, and dinosaurs have become an enduring part of world culture.",

  "A book is a medium for recording information in the form of writing or images, typically composed of many pages bound together and protected by a cover.",

  "A touch typist will know their location on the keyboard through muscle memory, the term is often used to refer to a specific form of touch typing that involves placing the eight fingers in a horizontal row along the middle of the keyboard and having them reach for specific other keys.",
 ]

def write(text):
  sys.stdout.write(text)
def clear():
  sys.stdout.write("\033[2J\033[H")



def countdown(num, text):
  for i in range(num, 0, -1):
    clear()
    print(reset + "String is: " + red + underline + text + reset)
    print(str(i))
    time.sleep(1)



ready = input(underline + green + "Welcome to CodingCactus's typing speed test!!\n\n" + reset +  "You enter every letter individually, if you get a letter wrong, you must enter it until it is correct.\nIt will all become clear.\n\nAre you ready? (Press Enter)")

tries = 0
totalwpm = 0
bestWPM = 0

totalAccuracy = 0

play = "y"

while play == "y":
  #chooses the random passage
  string = random.choice(strings)

  countdown(3, string)
  

  complete = False
  currentLetter = 0
  wrong = 0
  time1 = time.time()
  while not complete:
    if currentLetter > 0:
      #if the letter isn't the first one in the string, then dim all the letters before the current one
      doneString = reset + dim + string[:currentLetter]
    #underline the current letter
    current = underline + blue + string[currentLetter]
    #reset the colour for all the ones after the current letter
    afterCurrent = reset + string[currentLetter+1:]
    
    clear()
    if currentLetter == 0:
      print(current + afterCurrent)
    else:
      print(doneString + current + afterCurrent)
    
    #detects what key is pressed
    inputChar = getkey()
    while inputChar != string[currentLetter]:
      #if you put the wrong letter in
      wrong += 1
      #underlines the current letter, showing that you have got it wrong
      current = underline + red + string[currentLetter]
      clear()
      if currentLetter == 0:
        print(current + afterCurrent)
      else:
        print(doneString + current + afterCurrent)

      #input the letter again
      inputChar = getkey()

    #have they gone through the whole passage
    if currentLetter >= len(string)-1:
      complete = True

    #increments the current letter variable
    currentLetter += 1


  # all the calculations
  tries += 1
  time2 = time.time()
  clear()
  timeTaken = (time2-time1)/60

  wpm = round((len(string)/5)/timeTaken)
  totalwpm += wpm
  if wpm > bestWPM:
    bestWPM = wpm
  average = round(totalwpm/tries)
  accuracy = round(100-((wrong/(len(string) + wrong)) * 100))
  totalAccuracy += accuracy
  avrgAcc = round(totalAccuracy/tries)

  text = reset+ "Well done!\n\nWPM: " + green + str(wpm) + reset + "\nAverage WPM: " + green + str(average) + reset + "\nYour Highest: " + green + str(bestWPM) + reset + "\n\nAccuracy: " + green + str(accuracy) + "%" + reset + "\nAverage Accuracy: " + green + str(avrgAcc) + "%\n"

  print(text)

  play = input("Play again or see leaderboard? (y/l/n)").lower()
  while play not in ["y","l", "n"]:
    clear()
    print(text)
    play = input("Play again or see leaderboard? (y/l/n)").lower()
  if play == "l":
    leaderboard = underline + red + "The Leaderboard\n" + reset +"1. " + blue + "HahaYes: " + green + "199WPM\n" + reset + "2. " + blue + "ChezCoder: " + green + "188WPM\n" + reset + "3. " +blue + "Ygngt: " + green + "169WPM\n" + reset + "4. " + blue + "kbadrinath_tcsp: " + green + "130WPM\n" + reset + "5. " + blue + "brubert: " + green + "124WPM\n" + reset + "6. " + blue + "AmazingMech2418: " + green + "106WPM\n" + reset + "7. " + blue + "yeetuscleetus: " + green + "80WPM\n" + reset + "8. " + blue + "maxyang: " + green + "75WPM\n" + reset + "9. " + blue + "CodingCactus: " + green + "55WPM\n" + reset
    clear()
    print(leaderboard)
    play = input("Play again? (y/n)").lower()
    while play not in ["y","n"]:
      clear()
      print(leaderboard)
      play = input("Play again? (y/n)").lower()

clear()
print(green + "BYE!!!!" + reset+"\n\n\nComment your highscores!\n\nUpvote if you had fun\n\n:)")