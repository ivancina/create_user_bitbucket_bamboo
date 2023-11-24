import requests
import csv

def create_group(name):

    base_url = "your_site_url"
    api_url = f"{base_url}/rest/api/latest/admin/groups?name={name}"

    admin_username = "your_username"
    admin_password = "your_password"

    headers = {
        'Content-Type': 'application/json'
    }

    response_create_group = requests.post(
        api_url,
        auth=(admin_username, admin_password),
        headers=headers
    )

    if response_create_group.status_code == 200:
        print(f"Group '{name}' created successfully.")
    else:
        print(f"Failed to create group '{name}'. Error: {response_create_group.text}")



# Open the CSV file
with open("files/BitbucketStaging_group.csv", "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Iterate over the rows
    for index, row in enumerate(reader, start=1):
        try:
            group = row[0]
            response_group_create = create_group(group)
        except IndexError:
                print(f"Row {index}: Invalid row format. Skipping group creation.")


