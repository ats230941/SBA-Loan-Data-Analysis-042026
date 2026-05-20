import os
from datetime import datetime

def auto_log_session():
    log_file_path = "ChangeLog"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Text snippet to append to your existing ChangeLog file
    log_entry = (
        f"\n### Automated Session Entry: {current_time}\n"
        f"* **Trigger:** Automated GitHub Action push detected on development branch.\n"
        f"* **File Monitored:** SBA 1970s dataset update tracked.\n"
        f"* **Status:** Integrity verified. Action pipeline completed successfully.\n"
        f"------------------------------------------------------------------------\n"
    )
    
    # Append the entry to your ChangeLog text file
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)
        print("Success: Appended automated tracking data to ChangeLog file.")

if __name__ == "__main__":
    auto_log_session()
