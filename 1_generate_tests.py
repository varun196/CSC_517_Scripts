'''
Ensure that you set the `orig_test_file` to point to the tests. Do not include imports in `orig_test_file` 
Ensure that the directory provided as argument contains files. Move files from sub directory to parent directory if required. Use:

find /src/dir -type f -exec mv --backup=numbered -t /dst/dir {} +

i.e.       find . -type f -exec mv --backup=numbered -t . {} +

Move 2_generate_results.py to temp folder and run to get results in result folder. -- the test file searches the file to load from the directory where ruby command is run, irrespective of the file path mentioned in load.

Copying the 2_generate_results.py and executing can be automated too.

TODO: fetch test file name from cmdline
'''

import os
import subprocess
import re
import glob
import shutil
import sys

if(len(sys.argv)==2):
    path = "" + sys.argv[1]
else:
    print("Please enter path of the folder as first command line argument.\n Folder must contain only tean-submitted ruby files.")
    exit(0)

orig_test_file = "./ruby_intro_test_19spring.rb"
location = path + "*.rb"
print("Fetching files matching: "+location)

files = glob.glob(location)
print("fetched: " + str(len(files)) + " files")

# Create Test files directory
command = "mkdir "+path+"test_files"
os.system(command)
test_dir_path = path+"test_files/"

# Create solutions directory
command = "mkdir "+path+"results"
os.system(command)
result_path = path+"results/"

for path_file in files:
    '''
    Create test files
    ''' 
    # NOTE : Will work only with linus-style paths ::  parent/child/child/file.ext
    # Extrace filename :: Remove path and extension
    file = re.sub(r'.*\/','',path_file)
    filename = re.sub(r'\..*','',file)
    replace_line = "load './"+file+"'"

    test_file= test_dir_path + "test_" + filename + ".rb"

    # shutil :: referenced from https://stackoverflow.com/questions/14947238/change-first-line-of-a-file-in-python
    # Add 1 line to orig_test_file and save it as test_filename in test dir
    from_file = open(orig_test_file)
    to_file = open(test_file,mode="w")
    to_file.write(replace_line)
    shutil.copyfileobj(from_file, to_file)

print("Saved " + str(len(files)) + " files to "+test_dir_path)

test_location = test_dir_path+"*.rb"
test_files = glob.glob(test_location)

print("Fetched " + str(len(test_files)) + " files from "+test_dir_path)

command = "mkdir "+path+"temp"
os.system(command)
temp_path = path+"temp/"

for path_file in files:
    command = "cp "+path_file+" "+temp_path
    os.system(command)

for path_file in test_files:
    command = "cp "+path_file+" "+temp_path
    os.system(command)

'''
Please copy 2_generate_results.py to temp folder and run to get results in result folder.
'''
