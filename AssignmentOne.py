import math


def question_one():
    # Declare ages
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    print(f"Ages: {ages}")
    # Sort
    ages = sorted(ages)
    print(f"Sorted ages: {ages}")
    # Grab min and max
    mina, maxa = min(ages), max(ages)
    print(f"The minimum is: {mina}\nThe maximum is: {maxa}")
    # Throw min and max back in
    ages.append(mina)
    ages.append(maxa)
    print(f"Ages with min and max put in again: {ages}")
    # Sort again so that when getting median, it's in order
    ages = sorted(ages)
    print(f"Ages sorted again: {ages}")
    # Grab median
    median = ages[len(ages) // 2] if len(ages) % 2 != 0 else (ages[len(ages) // 2 + 1] + ages[len(ages) // 2]) / 2
    print(f"The median is {median}")
    print(f"The range is {min(ages) + max(ages)}")


def question_two():
    # Create empty dog dictionary
    dog = {}
    # Create specified keys
    dog["name"], dog["color"], dog["breed"], dog["legs"], dog["age"] = "", "", "", "", ""
    print(dog)
    # Create empty student dictionary
    student = {}
    # Create specified keys
    student["first_name"], student["last_name"], student["gender"], student["age"], student[
        "marital_status"] = "", "", "", "", ""
    student["skills"], student["country"], student["city"], student["address"] = [], "", "", ""
    # Print info you want
    print(f"The length of student dictionary: {len(student)}")
    print(f"Value of skills is {student['skills']} and the data type is {type(student['skills'])}")
    # Update skills value
    student["skills"].append("Computer Science")
    student["skills"].append("Python")
    # More prints
    print(f"The value of skills is {student['skills']}")
    print(f"The keys of the student dictionary: {student.keys()}")
    print(f"The values of the student dictionary: {student.values()}")


def question_three():
    # Create two tuples
    brothers = ("Gage",)
    sisters = ("Eden",)
    # Add them with + concatenation
    siblings = brothers + sisters
    # Print length and names
    print(f"I have {len(siblings)} siblings with the names {siblings}")
    # Old tuple plus new tuple
    family_members = siblings + ("Noelle", "Michael")
    # Print
    print(f"My family members are: {family_members}")


def question_four():
    # Create sets
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]
    # Print length
    print(f"Length of it_companies: {len(it_companies)}")
    # Add twitter
    it_companies.add('Twitter')
    print(it_companies)
    # Add new companies
    it_companies.update(['Company1', 'Company2'])
    print(it_companies)
    # Remove google
    it_companies.remove('Google')
    print(it_companies)
    # Print the information you want
    print(A.union(B))
    print(A.intersection(B))
    print(f"A is a subset of B: {A.issubset(B)}")
    print(f"A is a disjoint set of B: {A.isdisjoint(B)}")
    print(f"A joined with B: {A.union(B)}, B joined with A: {B.union(A)}")
    print(f"The symmetric difference between A and B is: {A.symmetric_difference(B)}")
    # Fully delete the sets
    del A
    del B
    # Print lengths
    print(f"The len of age as a list is {len(age)} and the len of it as a set is {len(set(age))}")


def question_five():
    # Grab radius from user
    radius = eval(input("Enter the radius of a circle: "))
    # Calc Area
    _area_of_circle_ = math.pi * pow(radius, 2)
    # Calc circumference
    _circum_of_circle_ = 2 * math.pi * radius
    # Print
    print(f"The area is {_area_of_circle_:.2f} and the circumference is {_circum_of_circle_:.2f}")


def question_six():
    msg = "I am a teacher and I love to inspire and teach people"
    # Split
    words = msg.split()
    the_set = set({})
    for i in words:
        # Add each word to a set since there can not be repeated values in a set
        the_set.add(i)
    # Get length of set
    print(f"There are {len(the_set)} unique words")


def question_seven():
    # Print
    print(f"Name\tAge\tCountry City\nAsabench\t250\tFinland Helsinki")


def question_eight():
    # Take radius and area then print
    radius = 10
    area = 3.14 * radius ** 2
    print(f"The area of a circle with radius {radius} is {area:.2f} meters square")


def question_nine():
    weight_in_lbs = list(eval(input("Enter the weights separated by a comma: ")))
    # Using list comprehension to create the new list
    weight_in_kilograms = [round(x * 0.453592, 2) for x in weight_in_lbs]
    print(weight_in_lbs)
    print(weight_in_kilograms)


if __name__ == "__main__":
    question_one()
    # question_two()
    # question_three()
    # question_four()
    # question_five()
    # question_six()
    # question_seven()
    # question_eight()
    # question_nine()
