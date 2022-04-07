import os
import shutil
import argparse

files_list = os.listdir("files")  # Creating a list of the files and folders that are in the "files" folder 

extensions = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Docs": [".doc", ".txt", ".odt"],
    "Audio": [".mp3"]
}


def files_order(file_to_move):
    """the function is defined to work along with the argparse module, it takes one argument (input from the command
    line), which will be parsed. The argument must be a valid file name. The function will then identify it and, in case
    it's a file, it will automatically move it in a directory based on the file's extension E.g. .txt will be moved in
    the doc directory, .mp3 will be moved in the audio directory. If a directory does not exist, the function will
    automatically create it and then move the file in it. If the file will be correctly moved, the function return a
    string stating the directory from which the file was taken, and the directory in which the file was moved. If the
    argument passed is not a valid name or the file does not exist in the files directory, the function will return a
    string stating that the file does not exist indeed."""
    
    cwd = os.getcwd()  # Getting current working directory path
    if os.path.isfile(f"files/{file_to_move}"):
        file_name, extension = os.path.splitext(file_to_move)  # Getting the file estension
        for key in extensions:  # Looping the dictionary, "key" will take the dictionary key associated value at each cycle
            if extension in extensions[key]:  # Checking that the file extension is in the dictionary

                # Checking that a directory with the same name of the key dictionary, in case it doesn't exist, i create it.
                if not os.path.isdir(f"files/{key}"):
                    os.makedirs(f"files/{key}")
                src = f"files/{file_to_move}"  # Declaring a variable with the starting path
                dst = f"files/{key}/{file_to_move}"  # And one with the destination path
                shutil.move(src=src, dst=dst)  # Moving the file from starting to destination
                file_info = f"{file_name} type: {key} size: {os.path.getsize(dst)}B"  # File's infos
                return f"{file_info} was correctly moved from {cwd}/{src} to {cwd}/{dst}"
    else:
        return f"{file_to_move} does not exist"


# Making an ArgumentParser type object which i will associate options and arguments i will use
parser = argparse.ArgumentParser(
    description="""
The script will move a file from his original directory to another based on its extension. If the directory doesn't
exist, the script will automatically create one, named with the extension's type name. E.g. .mp3 -->Audio, .txt -->Docs
""")

# Through parser.add_argument, i am adding the requested and optional parameters that are necessary when typing in cmd.
# in this case i am adding: the file name i want to move, i.e. parameter of the declared function above
# The function takes a single argument, by adding it i make its use mandatory for the correct functionality of the script.
# In case of missing argument, the user will be warned
parser.add_argument(
    # The argument is implicitly requestes because it's a positional argument and not a series of flags. As a consequence 
    # The parameter "required=True" is not necessary as it is only in case of the presence of optional arguments
    "file_to_move",  # The input argument the user submitted that will be parsed by the function
    type=str,  # The type that the argument will take
    # A short description of what the submitted argument represent
    help="This is the name of the file to move, type the name of the file with its extension E.g. 'Hello.txt'"
)

# After defining the arguments assignment, i procede with the actual assignment by calling parse_argse on the object (parser)
args = parser.parse_args()

# Calling the function passing args.file_to_move as argument, by doing this the instructions provided through the argparse module will be applied
# To be able to visualize the result, i'll print it
print(files_order(args.file_to_move))



