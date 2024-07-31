import mimetypes

def main():
    # Prompting the user for the file name
    file_name = input("Enter the file name: ")

    # Removendo espaços em branco do nome do arquivo e convertendo para minúsculas
    file_name_stripped = file_name.strip().lower()

    # Getting the file's extension (suffix)
    file_extension = file_name_stripped.split(".")[-1]

    # Checking if the file's extension matches one of the specified suffixes
    if file_extension in ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]:
        # Getting the media type for the given extension
        media_type, _ = mimetypes.guess_type(file_name_stripped)
        if media_type:
            print(media_type)
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
