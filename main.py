import os
import sys
from modules.send_request import send_request
from modules.contributors import list_all_contributors
from dotenv import load_dotenv

load_dotenv(override=True)

API_URL = 'https://api.github.com'
TOKEN = os.getenv("TOKEN_KEY")
TEAM = os.getenv("TEAM")
ORG = os.getenv("ORG")

HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {TOKEN}', # Has to be generated through github developer settings, permissions have to be enabled for different api calls
    'User-Agent': 'Python',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    "Cache-Control": "no-cache",
    'X-GitHub-Api-Version': '2022-11-28'
}

def main():
    try:
        endpoint_get_repos = f'{API_URL}/orgs/{ORG}/repos?per_page=100'
        repos = send_request("GET", endpoint_get_repos, HEADERS) # Get all repositories under organistion, limited max amount is 100 per page
        print(f'Number of repos found: {repos.__len__()}')
        for repo in repos:
            endpoint_get_contributors = f'{API_URL}/repos/{ORG}/{repo["name"]}/contributors' # Get all contributor per repository
            contributors = send_request("GET", endpoint_get_contributors, HEADERS)
            list_all_contributors(repo["name"], contributors)
            # for contributor in contributors:
            #     endpoint_remove_collaborators = f'{API_URL}/repos/{ORG}/{repo["name"]}/collaborators/{contributor["login"]}' # Removes all individual contributors (team privileges not affected), use it with caution, irreversible action
            #     send_request("DELETE", endpoint_remove_collaborators, HEADERS)
    except ValueError as e:
        print(f'Error: {e}')
        sys.exit('Terminated.')

if __name__ == "__main__":
    main()