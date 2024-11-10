import os
import subprocess
import requests
import json
import argparse

# Define your GitHub token here
GITHUB_TOKEN = "<YourGITHUBToken"

# Define headers for GitHub API authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# Function to get list of repositories in the organization
def get_repositories(org):
    url = f"https://api.github.com/orgs/{org}/repos"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch repositories: {response.status_code}")
        return []

# Function to run trufflehog on a specific repository
def run_trufflehog(repo_url, output_file):
    try:
        # Run trufflehog and capture output
        command = ["trufflehog", "github", "--json", repo_url]
        result = subprocess.run(command, capture_output=True, text=True)

        # Parse JSON output and filter for verified secrets
        output_lines = result.stdout.strip().split("\n")
        verified_secrets = [json.loads(line) for line in output_lines if '"verified": true' in line]

        # Save the verified secrets to the output file
        with open(output_file, "w") as f:
            json.dump(verified_secrets, f, indent=2)
        print(f"Verified secrets saved to {output_file}")
    except Exception as e:
        print(f"Failed to run trufflehog on {repo_url}: {str(e)}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Run Trufflehog on all repositories in a GitHub organization")
    parser.add_argument("-org", "--organization", required=True, help="GitHub organization name")
    args = parser.parse_args()
    
    # Retrieve the organization name from command line arguments
    organization = args.organization
    
    repos = get_repositories(organization)

    # Process each repository
    for repo in repos:
        repo_name = repo["name"]
        repo_url = repo["html_url"]
        output_file = f"{repo_name}_verified_secrets.json"
        
        print(f"Running Trufflehog on {repo_name} ({repo_url})...")
        run_trufflehog(repo_url, output_file)

if __name__ == "__main__":
    main()
