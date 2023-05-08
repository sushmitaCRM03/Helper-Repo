import argparse
from github import Github

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

# Get the pull request object
pr = repo.get_pull(args.pr)

# Get the head branch of the pull request
head_branch = pr.head.ref

# Get the files changed in the pull request
files = pr.get_files()

# Print the contents of each file
for file in files:
    contents = file.decoded_content.decode('utf-8')
    print(f'Contents of {file.filename}:')
    print(contents)
