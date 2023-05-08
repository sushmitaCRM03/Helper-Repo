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

# Print the contents of each file
for file in files:
    # Get the file name
    filename = file.filename
    # Get the file contents
    contents = repo.get_contents(filename, ref=head_branch).content 
    # Decode the file contents
    decoded_contents = base64.b64decode(contents)
    # Print the file contents
    print(decoded_contents)
    # Write the file contents to a file
    with open(os.path.basename(filename), 'wb') as f:
        f.write(decoded_contents)
