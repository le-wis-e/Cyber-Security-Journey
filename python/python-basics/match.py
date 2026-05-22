name = input("What is your name? ").capitalize()

match name:
    case "Harry" | "Daniel" | "Lewis" :
        print("Lives in Dalla")

    case "Ron":
        print("Lives in Atlanta")
    
    case _:
        print("who?")