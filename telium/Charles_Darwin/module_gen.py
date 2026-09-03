import random

def generate_modules():

    # Ask how many modules you want, though I might be able to take it from main.py
    total_modules = int(input("How many modules do you want? (Minimum 1, Maximum 40): "))

    # yo i added input validation, for NO reason are we proud?
    if total_modules < 1 or total_modules > 40:
        print("please stay in the bounds, defaulting to 17")
        total_modules = 17

    # Loop through each module number to create the connected modules
    for module_num in range(1, total_modules + 1):
        connections = []

        # Connect the modules to the previous and next module ID
        if module_num > 1:
            connections.append(module_num - 1)

        if module_num < total_modules:
            connections.append(module_num + 1)

        # add the zeros if it has less than 4
        while len(connections) < 4:
            connections.append(0)

        # generating the modules, and adding the values to the modules
        # Also sadly I can't use the CORRECT module_(number) because it breaks
        # The stupid messy base code. So i have to use module(number). Ugh. 0/10 base code.
        filename = "module" + str(module_num) + ".txt"
        file = open(filename, "w")
        for i in connections:
            file.write(str(i) + "\n")

        # closes da file
        file.close()

    print("Generated: " + str(total_modules) + " module files.")


