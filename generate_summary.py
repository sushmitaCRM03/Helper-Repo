import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--token', type=str, help='GitHub token')
parser.add_argument('--repo', type=str, help='GitHub repository name')
parser.add_argument('--branch', type=str, help='GitHub branch name')
args = parser.parse_args()

token = args.token
repo = args.repo
branch = args.branch

# Use the token, repo, and branch variables to fetch the PR code and generate the summary
