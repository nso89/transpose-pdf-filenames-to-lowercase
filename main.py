from pathlib import Path


SOURCE = Path.home().joinpath("Downloads")
Destination_PARENT = Path.home().joinpath("Documents\\News")
VALID_FILE_EXT = ".pdf"


def main():

    try:
        
        for file in SOURCE.iterdir():
            if file.is_file() and file.suffix == VALID_FILE_EXT:
                converted_file_name = file.name.lower().replace(" ","-")
                destination = Destination_PARENT.joinpath(converted_file_name)
                print(f"{file} -> {destination}")
                file.rename(destination)
    
    except (FileExistsError, FileNotFoundError, OSError, ValueError) as e:
        print(e)
        
if __name__ == "__main__":
    main()
