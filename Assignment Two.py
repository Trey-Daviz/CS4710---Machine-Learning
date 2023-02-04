def question_one():
    # Forwards loop
    for i in range(1, 6):
        print("* " * i)
    # Backwards loop
    for i in range(4, 0, -1):
        print("* " * i)


def question_two():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # Checking for if it is odd, if it is, print
    for x, i in enumerate(my_list):
        if x % 2 != 0:
            print(i)


def question_three(x):
    y = []
    # Check the type() function for type, append, then return
    for i in x:
        y.append(type(i))
    return y


def question_four(x):
    # Sets have unique values, so cast it to set and back
    x_set = set(x)
    y = list(x_set)
    return y


def question_five(x):
    # Use ascii to determine whether it is uppercase or not
    num_uppercase = 0
    num_lowercase = 0
    for i in x:
        if 65 <= ord(i) <= 90:
            num_uppercase += 1
        elif 97 <= ord(i) <= 122:
            num_lowercase += 1
    print(f"Number of uppercase: {num_uppercase}\nNumber of lowercase: {num_lowercase}")


if __name__ == "__main__":
    # question_one()
    # question_two()
    # print(question_three([23, 'Python', 23.98]))
    # print(question_four([1,2,3,3,3,3,4,5]))
    question_five('The quick Brow Fox')

