# This file will enumerate the contents of a directory and print the results to a table in a csv file
import os

# Set the directory you want to start from
rootDir = 'C:\\Users\\' + os.getlogin() + '\\Documents\\'
# Set the file name for the output
outputFile = 'C:\\Users\\Corey\\Documents\\dir_reveal.csv'

# Open the output file
f = open(outputFile, 'w')

# Write the header row
f.write('Directory,File Name,File Size,File Type \n')

# Loop through the directory and subdirectories
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        # Get the file size
        fsize = os.path.getsize(os.path.join(dirName, fname))
        # Get the file type
        ftype = os.path.splitext(fname)[1]
        # Write the row
        f.write('%s,%s,%s,%s \n' % (dirName, fname, fsize, ftype))

# Close the file
f.close()

# Print a message to the user
print('The directory has been enumerated and the results are in the file: %s' % outputFile)

# End of script
