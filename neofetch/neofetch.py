import os, random

home = os.path.expanduser("~")
number_of_asciis = os.listdir(home + "/.config/neofetch")

number = random.randint(1, len(number_of_asciis) - 1)

os.system("neofetch --source " + home + "/.config/neofetch/" + "ascii" + str(number) + ".txt")
