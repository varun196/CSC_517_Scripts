'''
move this to the temp folder provided to argument of 1_generate_tests.py and execute.
'''

import os
import subprocess
import re
import glob
import shutil

temp_location = "./*.rb"
temp_files = glob.glob(temp_location)

for path_file in temp_files:   
    if "test_" in path_file:
        file = re.sub(r'.*\/','',path_file)
        filename = re.sub(r'\..*','',file)
        command_ruby = "ruby "+path_file
        command_redir = command_ruby+" > ../results/result_"+filename+".txt"
        os.system(command_redir)