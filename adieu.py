import inflect

p = inflect.engine()
# create list to keep track of names
names = []
# loop forever
while True:
    try: 
    # get user input
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # create new line and stop the loop
        print()
        break
# printing using inflect module
output = p.join(names)
print(f"Adieu, adieu to {output}")