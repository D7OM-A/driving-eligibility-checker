age = int(input("How old are you?\n"))
license = input("Do you have a license? Type (Yes) or (No)\n")

if age >= 18 and license.lower() == "yes":
    print("You can drive")
elif age < 18 or license.lower() == "no":
    print("You can't drive")
else:
    print(f"Sorry, your entry [{license}] is not understood")

       

    