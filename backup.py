import os
import shutil
import schedule
import time

def backup_files(source_path, destination_path):
    try:
        # Create a timestamped backup folder
        backup_folder = f"backup_{time.strftime('%Y%m%d_%H%M%S')}"
        backup_path = os.path.join(destination_path, backup_folder)
        os.makedirs(backup_path)
        print(f"Backup created: {backup_path}")

        # Copy files/directories from source to backup
        for item in os.listdir(source_path):
            source_item = os.path.join(source_path, item)
            destination_item = os.path.join(backup_path, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item)
            else:
                shutil.copy2(source_item, destination_item)

        print("Backup completed successfully")

    except Exception as e:
        print(f"Error during backup: {e}")

# Example Usage
if __name__ == "__main__":
    source_directory = "/path/to/your/source"
    destination_directory = "/path/to/your/backup"

    # Schedule a backup every day at 2 AM
    schedule.every().day.at("02:00").do(backup_files, source_directory, destination_directory)

    while True:
        schedule.run_pending()
        time.sleep(1)
