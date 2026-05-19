first_name = input("What is your first name? ").strip().title().capitalize() # strip removes white spaces before and after the string, while capitalize capitalizes first letter of the string. Can use title to capitalize first letter of each name if there are two following each other like first and second name.
print("First name: ", first_name)

middle_name = input("What is your middle name? ").strip().title()
print("Middle name: " + middle_name)

last_name = input("What is your last name? ").strip().title()
print("Last name: ", end="") # prints on the same line 
print(last_name)

print(f"Your name is \"{first_name} {middle_name} {last_name}\"") # Special string i.e format string

