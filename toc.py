import os
import datetime
import pyperclip
import urllib.parse


def replace_string_in_file(file, search, replace):
    with open(file, "r") as read_file:
        file_content = read_file.read()

    new_file_content = file_content.replace(search, replace)

    with open(file, "w") as write_file:
        write_file.write(new_file_content)


def check_args():
    pass


def main(args=None):
    if args is None:
        args = check_args()

    dirapp = os.path.dirname(os.path.realpath(__file__))

    # get current directory folders/files
    fs_elements = os.listdir(dirapp)

    toc = []

    for magazine_folder in fs_elements:
        try:
            magazine_title = datetime.datetime.strptime(magazine_folder, '%Y-%m').strftime("%B %Y")
        except:
            continue
        toc.append(f"* **{magazine_title}**")

        # filter only folder (each folder is a magazine number)
        magazine_fullpath = os.path.join(dirapp, magazine_folder)
        if os.path.isdir(magazine_fullpath):

            # list all files in the magazine folder
            files_in_magazine = os.listdir(magazine_fullpath)

            for file in files_in_magazine:
                if file.endswith(".md"):
                    file_relative_path = os.path.join(magazine_folder, file).replace("\\", "/")
                    toc_text = os.path.splitext(os.path.basename(file_relative_path))[0]
                    toc_link = urllib.parse.quote(os.path.splitext(file_relative_path)[0])
                    toc.append(f"    - [{toc_text}]({toc_link})")
    
    toc_string = "\n".join(toc)
    pyperclip.copy(toc_string)
    c = pyperclip.paste()
    print(toc_string)


if __name__ == '__main__':
    try:
        main(args=None)
    except KeyboardInterrupt:
        print('\n\nBye!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
