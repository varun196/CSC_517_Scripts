Attendacne calculator produces following two output files:
1. _count.xlsx   -- # of files in which the given email appears
2. _result.xlsx  -- (  unityid@ncsu  score ) for all emails. Score is 1 if unity id appears in atleast 50% of files, 0 otherwise.
3. _result.csv  --  Ditto above. uploading csv works in webassign; but not xslx

syntax: 
$ python3 attendance_calculator.py  absolute_or_relative_path_to_folder_containing_all_xlsx_files

Assumes all excel files in the given folder contain an email column named 'Email Address' (Can be changed)
