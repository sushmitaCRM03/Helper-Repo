import argparse
from github import Github
import base64
import os

parser = argparse.ArgumentParser()
parser.add_argument('--token', type=str, help='GitHub token')
parser.add_argument('--repo', type=str, help='GitHub repository name')
parser.add_argument('--branch', type=str, help='GitHub branch name')
parser.add_argument('--pr', type=int, help='GitHub pull request number') 
args = parser.parse_args()

# Initialize PyGithub client with the token
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
    # Create a file in the current directory and write the decoded content
    with open(os.path.basename(file.filename), 'wb') as f:
        f.write(decoded_content)
        print(f)
        print(os.path.basename(file.filename))
        print(decoded_content)
