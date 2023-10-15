#add import
import question_c

age = ""
exit = "quit" or "QUIT"

while(age != exit):
    age = input("Enter 'quit' or enter a persons age: ")
    if(age != exit):
        result = question_c.get_person_category(int(age))
        print ("This person is a(n): " + result)
    else:
        print("Now Exiting...Goodbye!")
        break