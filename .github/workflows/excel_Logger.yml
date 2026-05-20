name: Automated SBA Change Logger

# 1. Trigger the workflow only when pushing to your specific 1970s branch
on:
  push:
    branches:
      - 05_20_26_1970s

jobs:
  build-and-log:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Clone your repository files onto the GitHub virtual server
      - name: Checkout Repository Code
        uses: actions/checkout@v4

      # Step 2: Set up Python on the virtual server
      - name: Set up Python Environment
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      # Step 3: Install the Excel reader tool (openpyxl) so Python can read your workbook
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install openpyxl

      # Step 4: Run your worker Python script to parse the changes
      - name: Execute Change Log Parser
        run: python scripts/parse_sba_changes.py

      # Step 5: Automatically push the updated ChangeLog file back to your repo
      - name: Commit and Push Updated Log
        run: |
          git config --global user.name "GitHub Actions Bot"
          git config --global user.email "actions@github.com"
          git add ChangeLog
          git diff-index --quiet HEAD || git commit -m "docs: auto-update ChangeLog via GitHub Action [skip ci]"
          git push origin 05_20_26_1970s
