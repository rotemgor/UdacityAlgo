import os
def check_sub_dir(path,found_files_list,suffix):
    files_list=os.listdir(path)
    for file in files_list:
        if os.path.isfile(file):
            if file.endswith(suffix):
                found_files_list.append(file)
        else: # this is a directory
            check_sub_dir(os.path.join(path,file),found_files_list,suffix)

    return found_files_list
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_found_files=[]
    res = check_sub_dir(path, list_of_found_files, suffix)
    print(res)

    return None
# OS Module Exploration Code
## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python


# # Let us print the files in the directory in which you are running this script
# print (os.listdir("."))
#
# # Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))
#
# # Does the file end with .py?
# print ("./ex.py".endswith(".py"))
find_files(".c", "")