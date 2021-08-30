import os, random

home = os.path.expanduser("~")
number_of_asciis = len(os.listdir(home + "/.config/neofetch")) - 1

number = random.randint(1, number_of_asciis - 1)

os.system("neofetch --source " + home + "/.config/neofetch/" + "ascii" + str(number) + ".txt")
