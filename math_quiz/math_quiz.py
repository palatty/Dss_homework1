import random

def get_random_integer(min, max):
    """
    This function takes two parameters min and max 
    and return a random integer between min and max 
    Parameter:
    integer (min)
    integer (max)
    Return:
    integer
    """
    return random.randint(min, max)


def get_operation():
    """ 
    This function chooses an operation among '+' '-' and '*'
    Parameters:
    None
    Return:
    string
    """
    return random.choice(['+', '-', '*'])


def compute(num_1, num_2, op):
    """
    This function takes three parameters 
    and computes the necessary operation 
    Parameters:
    Integer (num_1)
    Integer (num_2)
    string (op)
    Return:
    String (p)
    Integer (a)
    """
    p = f"{num_1} {op} {num_2}"
    if op == '+': 
        a = num_1 + num_2
    elif op == '-': 
        a = num_1 - num_2
    else: 
        a = num_1 * num_2
    return p,a

def math_quiz():
    """
    This function conducts Maths quiz and display result

    Parameter:
    None

    Return:
    None
    """
    Score = 0
    t_q = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        num_1 = get_random_integer(1, 10)
        num_2 = get_random_integer(1, 5)
        op = get_operation()
        question, result = compute(num_1, num_2, op)
        print(f"\nQuestion: {question}")
        try:
            userinput = input("Your answer: ")
            userinput = int(userinput)  # Try converting the input to a int
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        else:
            print(f"Valid input! You entered: {userinput}")

        if userinput == result:
            print("Correct! You earned a point.")
            Score += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {Score}/{t_q}")

if __name__ == "__main__":
    math_quiz()