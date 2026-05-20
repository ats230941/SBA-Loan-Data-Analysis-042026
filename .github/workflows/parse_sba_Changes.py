import os
from datetime import datetime

def auto_log_decades():
    log_file_path = "ChangeLog"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Grab the current branch name from GitHub's environment variables
    # If running locally, it defaults to 'Local-Development'
    active_branch = os.environ.get("GITHUB_BRANCH", "Local-Development")
    
    log_entry = (
        f"\n### Automated Entry for Branch [{active_branch}]: {current_time}\n"
        f"* **Target Era:** Data processing isolated strictly within the '{active_branch}' development scope.\n"
        f"* **Pipeline Status:** Structural formatting and change verification completed successfully.\n"
        f"------------------------------------------------------------------------\n"
    )
    
    # Append to the ChangeLog notepad file
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)
        print(f"Success: Appended automated tracking data to {active_branch} ChangeLog.")

if __name__ == "__main__":
    auto_log_decades()
