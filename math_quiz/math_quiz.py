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


def Operation(Num_1, Num_2, o):
    """
    This function takes three parameters 
    and computes the necessary operation 

    Parameters:
    Integer (Num_1)
    Integer (Num_2)
    string (o)

    Return:
    String (p)
    Integer (a)

    """

    p = f"{Num_1} {o} {Num_2}"
    if o == '+': 
        a = Num_1 + Num_2
    elif o == '-': 
        a = Num_1 - Num_2
    else: 
        a = Num_1 * Num_2
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
        Num_1 = get_random_integer(1, 10)
        Num_2 = get_random_integer(1, 54)
        o = get_operation()
        question, result = Operation(Num_1, Num_2, o)
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

if __name__ == "_main_":
    math_quiz()