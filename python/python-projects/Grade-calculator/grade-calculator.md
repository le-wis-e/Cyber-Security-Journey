markdown

````markdown
# Grade Calculator

## 📅 Date
23-05-2026

## 🎯 Objective
Build a student grade calculator that:
- Takes student name and validates it
- Takes 6 unit names
- Takes 6 scores and validates they are between 0 and 100
- Calculates the average
- Assigns a grade based on the average

## 💻 Code
```python
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
            print("Score must be between 0 and 100!")

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
```

## ▶️ How To Run
```bash
python3 grade_calculator.py
```

## 📤 Sample Output
````

Enter your name: Lewis

Enter unit names:- First unit: Compiler Construction Second unit: Psychology Third unit: Cybersecurity Fourth unit: Artificial Intelligence Fifth unit: Networking Sixth unit: Database

Enter your scores (0-100): Enter Compiler Construction score: 75 Enter Psychology score: 88 Enter Cybersecurity score: 92 Enter Artificial Intelligence score: 89 Enter Networking score: 95 Enter Database score: 79

Average score is: 86.33 Grade: B Great!

```

## 💡 What I Applied
- input() — get user input
- print() — display output
- f-strings — format output cleanly
- int() — convert input to integer
- capitalize() — format student name
- functions — separate each task
- parameters & arguments — pass values between functions
- return values — send values back from functions
- while True loops — validate invalid input
- if/elif/else — assign grade based on average
- boolean conditions — validate name and scores
- operators (+ / <=) — calculate average and compare
- tuples — return and unpack multiple values
- main() — entry point called at bottom

## ❓ Challenges I Faced
- Forgot to add return statement inside functions
  → Fixed by adding return after every function
- Variables not accessible across functions
  → Fixed by passing return values as arguments
- while True missing in student_name()
  → Fixed by wrapping input in while True loop
- Wrong syntax for average calculation
  → Removed {} from math expression
- NoneType error
  → Caused by missing return statement in function

## 🔑 Key Concepts Learned

### Parameters vs Arguments
- Parameter = placeholder in function definition
- Argument = actual value passed when calling

### Tuples
- Return multiple values using commas
- Unpack them using matching variable names

### While True + Return
- Use while True to keep asking until valid input
- Use return to exit the loop when input is valid

### Indentation
- Controls what is inside a function or loop
- Wrong indentation = wrong behaviour

## 🔗 Resources Used
- CS50P — cs50.harvard.edu/python
- Claude AI — guidance and debugging
