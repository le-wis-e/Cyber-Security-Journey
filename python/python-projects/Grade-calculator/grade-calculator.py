def main():
    name = student_name()
    units = unit_name()
    scores = unit_score(units)
    average = average_score(scores)
    Grade(average)

def student_name():
    while True:
        name = input("Enter your name: ").capitalize()
        if name != "":
            return name
        print("Name cannot be empty")

def unit_name():
    print("\nEnter unit names:-")
    unit1 = input("First unit: ")
    unit2 = input("Second unit: ")
    unit3 = input("Third unit: ")
    unit4 = input("Fourth unit: ")
    unit5 = input("Fifth unit: ")
    unit6 = input("Sixth unit: ")
    return unit1,unit2,unit3,unit4,unit5,unit6

def unit_score(units):
    unit1,unit2,unit3,unit4,unit5,unit6 = units   
    print("\nEnter your scores (0-100): ")
    score1 = get_valid_score(unit1)
    score2 = get_valid_score(unit2)
    score3 = get_valid_score(unit3)
    score4 = get_valid_score(unit4)
    score5 = get_valid_score(unit5)
    score6 = get_valid_score(unit6)
    return score1,score2,score3,score4,score5,score6

def get_valid_score(unit):
    while True:
        score = int(input(f"Enter {unit} score: "))
        if 0 <= score <= 100:
            return score
        else:
            print("Score must bewtween 0 and 100!")

def average_score(scores):
    score1,score2,score3,score4,score5,score6 = scores
    average = (score1 + score2 + score3 + score4 + score5 + score6)/6
    print(f"Average score is: {average:.2f}")
    return average

def Grade(average):
        if 90 <= average <= 100:
            print("Grade : A")
            print("Excellent")
        elif average >= 80:
            print("Grade: B")
            print("Great!")
        elif average >= 70:
            print("Grade: C")
            print("Good.")
        elif average >= 60:
            print("Grade: D")
            print("Room for improvement.")
        else:
            print("Fail")
            print("Can do better.")
        
        
            
main()
