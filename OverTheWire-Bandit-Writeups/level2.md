# Bandit Level 2 → 3
## 🎯 Objective
Read the password from a file called `--spaces in this filename--` in the home directory

## 💻 Commands Used
ssh bandit2@bandit.labs.overthewire.org -p 2220
ls
cat "./ --spaces in this filename--"

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Listed files using ls
- Found a file named `--spaces in this filename--`
- Could not use cat directly as the filename has dashes and spaces
- Used quotes to wrap the full filename and ./ to handle the dashes
- Found the password

## 💡 What I Learned
- Filenames with spaces need to be wrapped in quotes (single or double)
- Quotes tell bash to treat everything inside as one single filename
- Combined ./ and quotes to handle both dashes and spaces in a filename

## ✅ Password Found
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
