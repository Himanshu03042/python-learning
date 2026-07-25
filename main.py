import os
import shutil
from dotenv import load_dotenv
from rich import print

# Load environment variables
load_dotenv()

# Get folder path from .env or default
FOLDER_PATH = os.getenv("FOLDER_PATH", "test_folder")

# File categories
categories = {
    "images": [".jpg", ".png", ".jpeg"],
    "documents": [".pdf", ".txt"],
    "videos": [".mp4"],
    "others": []
}


def organise_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"[red]Folder '{folder_path}' does not exist[/red]")
        return

    files = os.listdir(folder_path)

    # Create category folders
    for category in categories:
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)

    # Move files
    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        moved = False

        for category, extensions in categories.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                dest = os.path.join(folder_path, category, file)
                shutil.move(file_path, dest)
                print(f"[green]Moved[/green] {file} → [bold]{category}[/bold]")
                moved = True
                break

        if not moved:
            dest = os.path.join(folder_path, "others", file)
            shutil.move(file_path, dest)
            print(f"[yellow]Moved[/yellow] {file} → others")


if __name__ == "__main__":
    print("[bold blue]📂 File Organiser Started[/bold blue]")
    organise_folder(FOLDER_PATH)