print("Welcome to a quiz game")

Game = input("Do you want to game ?")
score = 0

if Game != "Yes":
    quit
print("Okey lets play")

RSA = input("What is RSA in full ?")
if RSA.lower() == "Republic of south africa":
    print("correct")
    score += 2
else:
    print("Wrong its  repulic of south africa")

Water = input("Name something that have no colour ?")
if Water.lower() == "Water":
    print("correct")
    score += 2
else:
    print("Wrong its Water")
    
    
Name = input("Name something that belong to but poeple use more you ?")
if Name.lower() == "your name":
    print("correct")
    score += 2
else:
    print ("Wrong is Your Name") 


Rain = input("Name something that always go down but never go up ?")
if Rain.lower() == "rain":
    print("correct")
    score += 2
else:
    print("Wrong is a Rain")

IQ = input("What is IQ in full")
if IQ.lower() == "intelligence quotient":
    print("correct")
    score += 2
else:
    print("Wrong is Intelligence quotient")
      
print("The End")
print("You got " + str(score) + " Questions correct!")
print("You got " + str((score/5)*100) +"%")