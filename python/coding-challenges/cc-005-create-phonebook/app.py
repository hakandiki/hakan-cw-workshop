#Write a program that creates a phonebook, adds requested \
# contacts to the phonebook, finds them, and removes them.

phone_dict = {}

while True:
    number_input = input("Welcome to the phonebook application\n\
    1. Find phone number\n\
    2. Insert a phone number\n\
    3. Delete a person from the phonebook\n\
    4. Terminate\n\
    Select operation on Phonebook App (1/2/3) : ")
    try:
        if int(number_input) < 1 or int(number_input) > 4:
            raise Exception
    except:
        print("Invalid input format, cancelling operation ...")
    if number_input == "1":
        try:
            find_name = input("Find the phone number of : ")
            print(phone_dict[find_name])
        except:
            print(f"Couldn't find phone number of {find_name}")
    elif number_input == "2":
        try:
            person_name = input("Insert name of the person : ")
            phone_number = input("Insert phone number of the person: ")
            if not phone_number.isdigit():
                raise Exception
            if person_name.isdigit():
                raise Exception 
            print(f"Phone number of {person_name} is inserted into the phonebook")
            phone_dict[person_name] = phone_number
        except:
            print("Invalid input format, cancelling operation ...")
    elif number_input == "3":
        try:
            delete_whom = input("Whom to delete from phonebook :")
            print(f"{delete_whom} is deleted from the phonebook")
            del phone_dict[delete_whom]
        except:
            print(f"Couldn't find {delete_whom}")
    elif number_input == "4":
        print("Exiting Phonebook")
        break


