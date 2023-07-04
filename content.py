import os
import shutil
import subprocess
import time

art = r"""
                               _.-~  )
                    _..--~~~~,'   ,-/     _
                 .-'. . . .'   ,-','    ,' )
               ,'. . . _   ,--~,-'__..-'  ,'
             ,'. . .  (@)' ---~~~~      ,'
            /. . . . '~~             ,-'
           /.  T . .             ,-'
          ; . . I .  - .        ,'
         : . . . .       _     /
        . . N . .          `-.:
       . . . ./  - O          )
      .  . . |  _____..---.G_/ _____
~---~~~~----~~~~             ~~
"""

def show_print_output():
    time.sleep(2)
    subprocess.call(["cmd", "/c", "cls"])

def copy_files_with_matching_suffix(content_directory, output_directory):
    script_directory = os.getcwd()
    if not output_directory:
        output_directory = os.path.join(script_directory, "output")
    else:
        output_directory = os.path.join(output_directory, "output")

    copied_files_count = 0
    subfolders_count = 0

    for root, dirs, files in os.walk(content_directory):
        for file in files:
            if file.endswith(".xml"):
                filename = os.path.splitext(file)[0]
                filename_parts = filename.split("_")

                if len(filename_parts[-2]) == 2:
                    suffix = filename_parts[-3][-10:]
                    destination_folder_name = filename.rsplit("_", 3)[1][-10:]
                else:
                    suffix = filename_parts[-1][-10:]
                    destination_folder_name = filename.rsplit("_", 2)[1][-10:]

                destination_folder = os.path.join(output_directory, destination_folder_name)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                    subfolders_count += 1

                destination_path = os.path.join(destination_folder, file)
                shutil.copy2(os.path.join(root, file), destination_folder)

                copied_files_count += 1

    print(art)
    print("Created", subfolders_count, "subfolders.")
    print("Copied", copied_files_count, "files.")
    show_print_output()


content_directory = input("Enter the location of the content files: ")
output_directory = input("Enter the location to generate the output folder (leave empty for default): ")
copy_files_with_matching_suffix(content_directory, output_directory)
