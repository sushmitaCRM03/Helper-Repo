import argparse
from github import Github
import base64
import os
import openai
import json
import base64
import requests

openai.api_key = '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'
# Usage
username = "techsibsbusiness3@gmail.com"
password = "ATATT3xFfGF0wbxiCkUkOwgYDEoMZOdUrNu8TnBIzopcbY8qqAXjs9Q0N6iaWLfIDcBUXDlXPL3gvsgVtQ6_djqiaca9EulIooJ4BAWMIx0gPvCvAdvpUzT0_4T9c2_OJbdqHFHSnGd3K9zn1y-yiBIsrCFJKR3m0l5ylqWRlKaP8EqWah6YMi8=2FDCC6F0"

parser = argparse.ArgumentParser()
parser.add_argument('--token', type=str, help='GitHub token')
parser.add_argument('--repo', type=str, help='GitHub repository name')
parser.add_argument('--branch', type=str, help='GitHub branch name')
parser.add_argument('--pr', type=int, help='GitHub pull request number') 
args = parser.parse_args()


# Initialize PyGithub client with the token ggh
g = Github(args.token)

# Get the repository object
repo = g.get_repo(args.repo)
print(repo)
# Get the pull request object
pr = repo.get_pull(args.pr)  
print(pr)
# Get the head branch of the pull request
head_branch = pr.head.ref
print (head_branch) 
# Get the files changed in the pull request
files = pr.get_files() 
print(files)

# Iterate over the files and get the code changes from pr branch
for file in files:
    print(file)
    # Get the file content from the pr branch
    file_content = repo.get_contents(file.filename, ref=head_branch).content
    print(file_content)
    # Decode the base64 encoded content
    decoded_content = base64.b64decode(file_content)
    print(decoded_content)
    # # Create a file in the current directory and write the decoded content
    # with open(os.path.basename(file.filename), 'wb') as f:
    #     f.write(decoded_content)
    #     print(f)
    #     print(os.path.basename(file.filename))
    #     print(decoded_content)

#async function call to generate_text function

async def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # Degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
    
async def sum_of_series(n):
    return n * (n + 1) / 2

async def generate_text():
    result = get_jira_ticket_details()
    # add prompt to the result
    # convert the result to a string
    result = str(result)
    prompt = """
        using the bug description and analyzing bug fix code given below pls create a 200 words confluence documentation content \

        1. description """ + result + """ bugfix code """ + decoded_content + """

        Please provide a list of JIRA task titles related to the above array of objects.
    """

    # Call the asynchronous function to get the completion
    response = await get_completion(prompt)
    print (response)


def get_jira_ticket_details():
    url =  "https://noniking0302.atlassian.net/rest/api/3/issue/GP-51"
    auth_header = "Basic " + base64.b64encode((username + ":" + password).encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": auth_header,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        ticket_data = response.json()
        description = ticket_data.get("fields", {}).get("description", {}).get("content", [])
        print(description)
        return description
    else:
        print("Failed to retrieve ticket details. Status code:", response.status_code)
        return None
 

generate_text();