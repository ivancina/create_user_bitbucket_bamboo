import requests
import csv

def create_user(username_value, password_value, email_value, display_name_value):
    base_url = "your_site_url"
    url = f"{base_url}/rest/api/latest/admin/users?name={username_value}&password={password_value}&emailAddress={email_value}&displayName={display_name_value}"
    url_get_user = f"{base_url}/rest/api/latest/admin/users/{username_value}"

    admin_username = "your_username"
    admin_password = "your_password"

    headers = {
        'Content-Type': 'application/json'
    }

    # Check if the user already exists
    response_check_if_user_exists = requests.get(
        url_get_user,
        auth=(admin_username, admin_password),
        headers=headers
    )

    if response_check_if_user_exists.status_code == 200:
        return f"User '{username_value}' already exists. Skipping creation."


    response = requests.post(
        url,
        auth=(admin_username, admin_password),
        headers=headers
    )

    return response.text


# Open the CSV file
with open("files/users.csv", "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Iterate over the rows
    for index, row in enumerate(reader, start=1):
        try:
            username = row[0]
            display_name = row[1]
            password = row[2]
            email = row[3]
            response_user_created = create_user(username, password, email, display_name)
            if not response_user_created.startswith("User"):
                print(f"Row {index}: User '{username}' created successfully.")
        except IndexError:
            print(f"Row {index}: Invalid row format. Skipping user creation.")
