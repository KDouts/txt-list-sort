# file name backUp.py
# import regex
import re
# newFiles opens the new txt document to read
newFiles = open("New.sha1.txt", "r")
# newData will read the txt document as one element
newData = newFiles.read()
# splitNew uses regex to split the txt element into separate elements when a space is encountered
splitNew = re.split('\s+', newData)

# oldFiles opens the old txt document to read
oldFiles = open("Old.sha1.txt", "r")
# oldData will read the txt document as one element
oldData = oldFiles.read()
# splitOld uses regex to split the txt element into separate elements when a space is encountered
splitOld = re.split('\s+', oldData)
# for loop that loops over the splitNew array 
for line in splitNew:
    # if line is NOT in the splitOld array of elements
    if line not in splitOld:
        # create a new txt file "newNotInOld.txt" that can be appended
        newNotOld = open("newNotInOld.txt", "a")
        # append the document with the line that is being read and move to a new line
        newNotOld.write(line + '\n')
        # stop appending the txt document
        newNotOld.close()
        # continue to the next statement
        continue
    # else if the line IS in Spl
    elif line in splitOld:
        # continue to the next statement
        continue

# for loop that loops over the splitOld array of elements
for line in splitOld:
    # if the line is NOT in splitNew
    if line not in splitNew:
        # create a new txt document "oldNotInNew.txt" that can be appended
        oldNotNew = open("oldNotInNew.txt", "a")
        # appned the document with the line that is being read and move to a new line
        oldNotNew.write(line + '\n')
        # stop appending the txt document
        oldNotNew.close()
        # continue to the next statement
        continue
    # else if the line IS in splitNew
    elif line in splitNew:
        # continue to the next statement
        continue