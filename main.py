import random

sex  = ["Male", "Female"]
race = ["Dragonborn","Dwarf", "Elf", "Gnome", "Half-Elf",
        "Half-Orc", "Halfling", "Human", "Tiefling"]
classes = ["Ranger", "Barbarian", "Bard", "Cleric", "Druid", "Fighter",
           "Monk", "Paladin", "Rogue", "Sorcerer", "Warlock", "Wiazrd"]

rc = random.choice
rr = random.randint
ru = random.uniform

userChoice = 1

while(userChoice == 1):
    sexPlayer = rc(sex)
    racePlayer = rc(race)
    classPlayer = rc(classes)
    agePlayer = rr(15, 350)
    heightPlayer = rr(50, 300)
    weightPlayer = ru(20, 250)

    weightPlayer = round(weightPlayer, 2)

    nameFile = input("Enter name of the file: ")+".txt"
    namePlayer = input("Enter the name of your character: ")

    with open(nameFile, "w") as text_file:
        print(f"Name: {namePlayer}", file=text_file)
        print(f"Sex: {sexPlayer}", file=text_file)
        print(f"Race: {racePlayer}", file=text_file)
        print(f"Class: {classPlayer}", file=text_file)
        print(f"Age: {agePlayer} yrs", file=text_file)
        print(f"Height: {heightPlayer} cm", file=text_file)
        print(f"Weight: {weightPlayer} kg", file=text_file)

    f = open(nameFile, "r")
    fileContent = f.read()
    openFile = str(input("Do you wish to see your character? [y/n] "))
    if(openFile == "y"):
        print(fileContent)
        f.close()
        userChoice = int(input("Another Character? Y[1], N[0]: "))
    elif(openFile == "n"):
        userChoice = int(input("Another Character? Y[1], N[0]: "))
        
