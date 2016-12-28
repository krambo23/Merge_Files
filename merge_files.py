# Imports necessary module(s)
import sys, os

script_name = str(sys.argv[0])
folder_name = str(sys.argv[1])
merged_output = str(sys.argv[2])
file_list = os.listdir(folder_name)
no_of_files = len(file_list)
file_read = ""
to_merge = ""

# http://stackoverflow.com/a/12468274
encoding_type = input("Input Encoding [Leave blank if UTF-8] : ")
if encoding_type == "" :
	encoding_type = "utf-8"

# Reads each file and merges their content(s)
for i in range(0, no_of_files) :
	file_loc = folder_name + "/" + file_list[i]
	file_read = open(file_loc, "r", encoding = encoding_type, errors = "ignore") # Opening "file_loc" in r mode
	to_merge += file_read.read() # Add content(s) of file into "to_merge"
	file_read.close() # Closes "file_loc"

# Writes to merged file
file_write = open(merged_output, "w", encoding = encoding_type, errors = "ignore") # Opening merged_output in w mode
file_write.write(to_merge) # Writes into merge_output the contents of "to_merge"
file_write.close() # Closes to_merge

print("Merging Complete ;-)")