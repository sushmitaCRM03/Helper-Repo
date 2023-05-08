import requests
import os

repo_name = os.environ['GITHUB_REPOSITORY']
headers = {'Authorization': f'token {os.environ["GITHUB_TOKEN"]}'}
url = f'https://api.github.com/repos/{repo_name}'
response = requests.get(url, headers=headers)