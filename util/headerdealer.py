import random

def randomHeader():
    with open("util/user-agents.txt", "r") as file:
        #allLines = file.read()
        #line = list(map(str, allLines.split()))

        lines = file.readlines()
        line_random = random.choice(lines)


        return line_random.strip("'b\n")