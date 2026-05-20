# Bandit Level 4 → 5
## 🎯 Objective
Find the only human-readable file in the inhere directory and read the password from it

## 💻 Commands Used
ssh bandit4@bandit.labs.overthewire.org -p 2220
ls
cd inhere
ls
file ./*
cat ./-file07

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Listed files using ls and found a directory called inhere
- Changed into the inhere directory using cd
- Found 10 files named -file00 to -file09
- Used file ./* to check the type of all files at once
- Identified -file07 as the only ASCII text (human-readable) file
- Read it using cat ./-file07 to get the password

## 💡 What I Learned
- file ./* checks the type of all files in a directory at once
- ASCII text means human-readable while data/binary files are not
- Filenames starting with - need ./ prefix when using cat
- No space should be between ./ and the filename

## ✅ Password Found
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
