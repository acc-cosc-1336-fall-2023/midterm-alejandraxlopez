#add import
from question_a import get_assessment_value, get_tax_assessed

property_value = ""
exit = "quit" or "QUIT"

while True:
    property_value = input("Enter Property Value or enter 'quit' to exit: ")
    
    if property_value == exit:
        print("Now Exiting...Goodbye!")
        break
    
    try: 
        final = float(property_value)
        property_assessment = get_assessment_value(final)
        property_tax = get_tax_assessed(final)
        
        print(f"Assessment Value of Property is: ${property_assessment:.2f}")
        print(f"Property Tax is: ${property_tax:.2f}")
    except ValueError:
        print("Invalid Number")
