import json
import requests
import csv


def add_user_to_group(user, group):
    base_url = "http://localhost:7990"
    api_url = f"{base_url}/rest/api/latest/admin/users/add-groups"

    admin_username = "admin"
    admin_password = "nogomet91"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "groups": [
            group
        ],
        "user": user
    })

    response_add_user_to_group = requests.post(
        api_url,
        auth=(admin_username, admin_password),
        data=payload,
        headers=headers
    )

    if response_add_user_to_group.status_code == 200:
        print(f"User '{user}' added to {group} successfully.")
    else:
        print(f"Failed to add user '{user}' to group {group}. Error: {response_add_user_to_group.text}")


# Open the CSV file
with open("files/BitbucketStaging_UserAndGroup.csv", "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Iterate over the rows
    for index, row in enumerate(reader, start=1):
        try:
            group = row[6]
            user = row[2]
            response_group_create = add_user_to_group(user,group)
        except IndexError:
            print(f"Row {index}: Invalid row format. Skipping adding {user} in {group}.")
