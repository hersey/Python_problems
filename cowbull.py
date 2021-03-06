"""
Create a program that will play the cows and bulls game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
user guessed correctly in the correct place, they have a cow. For every digit the user guessed
correctly in the wrong place is a bull. Every time the user makes a guess, tell them how many
cows and bulls they have. Once the user guesses the correct number, the game is over. Keep track
of the number of guesses the user makes throughout teh game and tell the user at the end.
 
Say the number generated by the computer is 1038. An example interaction could look like this:
  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
"""

#####  reference: http://www.programmingforums.org/post176491.html   ######

import random

machine=random.randint(0,9999)  #A four digit number generated by the computer
machine_str=str(machine)
stop=len(machine_str)

print machine

user=int(input("Give me a four digit number: "))  #user's guess of a four digit number
tries=1

while machine!=user:  
  cow=0
  bull=0
  user_str=str(user)
  for i, user in enumerate(user_str):      #enumerate() is to circle through a sequence 'thing' as (1,thing[1])
    for j, machine in enumerate(machine_str):
      if(user==machine):
        if i==j:
          cow+=1
        else:
          bull+=1

  print cow, "Cows and ", bull, "Bulls"
  user=int(raw_input("\nTry again:"))
  tries+=1

print "\nYou guessed it! \nThe number was", machine, "You took ", tries, "times to guess."



'''
def compare_num(number,user_guess):
	cowbull=[0,0] #first cows, then bulls
	for i in range(len(number)): 
		if number[i]==user_guess[i]:
			cowbull[0]+=1
		elif user_guess[i] in number:
			cowbull[1]+=1
	return cowbull


if __name__=="__main__":
	playing= True
	number=str(random.randint(0,9999))#generate random 4 digit number
	guesses=0

	print("Let us play a game of Cowbull!") #explanation

  while playing:
    user_guess=input("Give me a four digit number: ")
    if user_guess=="exit":
    	break
    cownbullcount=compare_num(number,user_guess)
  guesses+=1

    print("You have "+ str(cownbullcount[0]) + "cows, and "+ str(cownbullcount[1])+"bulls.")

    if cowbullcount[1]==4:
    	playing=False
    	print('You win the game after'+ str(guesses)+"! The number was"+ str(number))
    	break
    else: 
    	print ("Your guess isn't quite right, try again.")

'''










