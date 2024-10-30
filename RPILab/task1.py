# This program replicated the functionality of figure 5
# We will take the input of a radius and calculate either the surface area or volume

pi = 3.14159

radius = float(input("Enter the radius of a sphere: "))
print("To calculate surface area, enter 1 \nTo calculate volume, enter 2")


invalid = True # variable to make sure valid input is made
while invalid:
    quantity = int(input("What do you want to calculate: "))
    if quantity ==1:
        surface_area = 4*pi*radius*radius
        print("The sphere surface area is ", surface_area)
        invalid = False
    elif quantity ==2:
        volume = (4*pi*(radius*radius*radius))/3
        print("The sphere volume is ", volume)
        invalid = False
    else:
        print("please re-enter a valid choice.")
