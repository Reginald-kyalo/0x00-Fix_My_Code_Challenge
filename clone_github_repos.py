import requests
import os

# Replace with your GitHub username or organization name
username_or_org = "Reginald-kyalo"
# Replace with your GitHub Personal Access Token
access_token = "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"

# Create a directory to store cloned repositories
if not os.path.exists(username_or_org):
    os.mkdir(username_or_org)

# Get the list of repositories for the user or organization
url = f"https://api.github.com/users/{username_or_org}/repos"
headers = {"Authorization": f"token {access_token}"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        repo_name = repo["name"]
        repo_url = repo["clone_url"]
        os.system(f"git clone {repo_url} {username_or_org}/{repo_name}")
else:
    print(f"Failed to retrieve repositories. Status code: {response.status_code}")
