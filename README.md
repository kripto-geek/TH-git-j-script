# TH-git-j-script

# GitHub Organization Secret Scanner

This Python script scans all repositories in a specified GitHub organization for secrets using Trufflehog and saves verified secrets in separate JSON files for each repository. This tool is helpful for ethical security auditing and testing your organization’s repositories for sensitive information leaks.

## Features

- Scans all repositories within a specified GitHub organization.
- Uses Trufflehog to detect secrets and filters for verified secrets.
- Saves verified secrets to a JSON file for each repository.

## Prerequisites

1. **Trufflehog**: This tool must be installed on your system. Install it with:
    ```bash
    pip3 install trufflehog
    ```
2. **GitHub Personal Access Token**: You’ll need a GitHub token with `repo` read permissions for the organization. Generate it from your GitHub settings under Developer Settings > Personal Access Tokens.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kripto-geek/TH-git-j-script.git

## Usage
  ```bash
  python3 trufflehog_scan.py -org <orgname>
