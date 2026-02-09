import json


# ... (deine anderen Funktionen bleiben gleich) ...

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)
    # Filtern nach E-Mail (ebenfalls Case-Insensitive mit .lower())
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name/age/email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age: "))
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")