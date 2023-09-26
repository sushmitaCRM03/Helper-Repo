import argparse
import base64
import openai
import requests
from github import Github

# Define your GitHub and OpenAI API keys as environment variables or secrets
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Initialize the PyGithub client
g = Github(GITHUB_TOKEN)

def get_github_pull_request_content(token, repo_name, pr_number):
    try:
        # Get the repository object
        repo = g.get_repo(repo_name)

        # Get the pull request object
        pr = repo.get_pull(pr_number)

        # Get the head branch of the pull request
        head_branch = pr.head.ref

        # Get the files changed in the pull request
        files = pr.get_files()

        # Initialize a dictionary to store file content
        file_contents = {}

        # Iterate over the files and get the code changes from the PR branch
        for file in files:
            file_content = repo.get_contents(file.filename, ref=head_branch).content
            decoded_content = base64.b64decode(file_content).decode("utf-8")
            file_contents[file.filename] = decoded_content

        return file_contents

        except Exception as e:
            print(f"Error getting GitHub PR content: {str(e)}")
            return None

async def generate_text(prompt, model="gpt-3.5-turbo"):
    try:
        openai.api_key = OPENAI_API_KEY

        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.7,  # Adjust the temperature for randomness
        )

        return response.choices[0].message["content"]

    except Exception as e:
        print(f"Error generating text with OpenAI: {str(e)}")
        return None

def get_jira_ticket_detail(username, password):
    try:
        url = https://noniking0302.atlassian.net/rest/api/3/issue/GP-51'
        auth_header = "Basic " + base64.b64encode((username + ":" + password).encode("utf-8")).decode("utf-8")
        headers = {
            "Authorization": auth_header,
            "Content-Type": "application/json"
        }

        response = requests,get(url, headers=headers)
        
        if response.status_code == 200:
            ticket_data = response.json()
            description = ticket_data.get("fields", {}).get("description", {}).get("content", [])
            return description
        else:
            print("Failed to retrieve ticket details. Status code:", response.status_code)
            return None

    except Exception as e:
        print(f"Error getting Jira ticket details: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, help='GitHub token')
    parser.add_argument('--repo', type=str, help='GitHub repository name')
    parser.add_argument('--pr', type=int, help='GitHub pull request number')
    args = parser.parse_args()

    # Get the PR content from GitHub
    pr_content = get_github_pull_request_content(args.token, args.repo, args.pr)

    if pr_content:
        # Assuming there's a specific file you want to use for generating text
        file_to_generate_text = "example_file.txt"

        if file_to_generate_text in pr_content:
            prompt = f"Generate text based on changes in {file_to_generate_text}:\n\n{pr_content[file_to_generate_text]}"

            # Get Jira ticket details
            jira_description = get_jira_ticket_detail("techsibsbusiness3@gmail.com", "YOUR_JIRA_PASSWORD")

            if jira_description:
                prompt += f"\n\nJira Ticket Description:\n\n{jira_description}"

            # Generate text using OpenAI
            generated_text = generate_text(prompt)

            if generated_text:
                print("Generated Text:")
                print(generated_text)

if __name__ == "__main__":
    main()
