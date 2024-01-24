This is a small python program to find and count all unique file extentions 
in a directory or a file containing the desired files for analysis (dir list).
You can provide the root directory and the program recurses in all the subdirectories so no worries there.
The program checks for weird extentions using a WEIRDNESS factor. By default it is set to 8, which means that every extention detected that is more than 8 character is considered weird by the program and is shown separately. Feel free to change it to your needs.

Usage:
python3 findExtentions.py -i (dir or file path)

The program checks if you provide a file or a directory so you don't have to specify, just throw it in there:)
