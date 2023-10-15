# write functions here, don't add input('') statements here!
def get_person_category(age):
    category = ""

    if age < 0:
        category = "Invalid Number"
    elif age >= 0 and age < 1:
        category = "Infant"
    elif age >= 1 and age < 13:
        category = "Child"
    elif age >= 13 and age < 20:
        category = "Teenager"
    elif age >= 20 and age <= 125:
        category = "Adult"
    else:
        category = "Invalid Number"

    return category


   