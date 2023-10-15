#add import
import question_b

def perform_sum():
    while True:
        user_input = input("Enter 'go' to perform Sum of Evens or enter 'quit' to exit: ")
        if user_input == "quit" or user_input == "QUIT":
            print("Now Exiting...Goodbye!")
            break
        if user_input == "go" or user_input == "GO":
            run_main()
            break

def run_main():
    while True:         
        try:
            val = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid Number...")
    sum = (question_b.get_sum_of_evens(val))
    print(sum)
    perform_sum()
run_main()