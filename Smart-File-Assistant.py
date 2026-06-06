from pathlib import Path
import os,shutil

folder_path = Path(input("Enter the folder path: "))

if not folder_path.exists():
    print("The folder doesn't exists!")

else:
    categories = {"Images": [],
                  "Archives": [],
                  "Other": [],
                  "Data": [],
                  "Programming": [],
                  "Documents": [],
                  "Videos": [],
                  "Audio": [],
                  }

    image_ext = (".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".avif", ".tiff", ".tif", ".heic", ".heif", ".raw", ".bmp")
    archive_ext = (".zip", ".zipx", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso", ".jar", ".apk", ".dmg")
    programming_ext = (".html", ".css", ".js", ".ts", ".c", ".cpp", ".java", ".cs", ".go", ".py", ".rs", ".kt", ".swift", ".dart", ".php", ".ex", ".exs", ".hs", ".sh", ".ps1", ".rb", ".pl",".ino")
    document_ext = (".key", ".numbers", ".gdoc", ".gsheet", ".gslides", ".docx", ".doc", ".pdf", ".txt", ".rtf", ".odt", ".pages", ".xlsx", ".xls", ".ods", ".pptx", ".ppt", ".odp", ".odg", ".epub", ".mobi", ".azw", ".djvu", ".tex", ".yaml")
    video_ext = (".mp4", ".mov", ".mkv", ".webm", ".avi", ".wmv")
    audio_ext = (".mp3", ".wav", ".m4a", ".flac", ".aac", ".wma", ".aiff", ".ogg")
    data_ext = (".csv", ".json", ".sql", ".parquet")

    if folder_path.is_dir():

        for file in folder_path.iterdir():

            if file.is_file():

                if file.suffix.lower() in image_ext:
                    categories["Images"].append(file)

                elif file.suffix.lower() in archive_ext:
                    categories["Archives"].append(file)

                elif file.suffix.lower() in data_ext:
                    categories["Data"].append(file)

                elif file.suffix.lower() in document_ext:
                    categories["Documents"].append(file)

                elif file.suffix.lower() in video_ext:
                    categories["Videos"].append(file)

                elif file.suffix.lower() in audio_ext:
                    categories["Audio"].append(file)

                elif file.suffix.lower() in programming_ext:
                    categories["Programming"].append(file)

                else:
                    categories["Other"].append(file)

        for keys, values in categories.items():

            print(f"{keys} ({len(values)} files)")

            for value in values:
                print(f"-> {value.name}")

            print()

        print(f"\nTotal files detected: {sum(len(value) for value in categories.values())}")

        compare_file = {}

        for file in folder_path.iterdir():

            if file.is_file():
                compare_file[file.name] = file.stat().st_size / 1024

        if compare_file:

            max_file_key = max(compare_file, key=compare_file.get)
            max_file_value = compare_file[max_file_key]

            low_file_key = min(compare_file, key=compare_file.get)
            low_file_value = compare_file[low_file_key]

            def get_folder_size(folder_path):

                with os.scandir(folder_path) as entries:

                    total_folder_size = 0

                    for entry in entries:

                        if entry.is_file():
                            total_folder_size += entry.stat().st_size

                        else:
                            total_folder_size += get_folder_size(entry.path)

                return total_folder_size

            print(f"\nLargest file: {max_file_key} ({max_file_value:.2f} KB)")
            print(f"Smallest file: {low_file_key} ({low_file_value:.2f} KB)")
            print(f"Total size of folder: {folder_path.name} ({get_folder_size(folder_path)/1024:.2f} KB)")

        else:
            print("No files found.")

        print("\nAbout to move files....")
        
        for category in categories:
            (folder_path/category).mkdir(exist_ok=True)
            for file in categories[category]:
                print(f"Moving {file.name} -> {category}")
                shutil.move(str(file),str(folder_path/category))






    
        

