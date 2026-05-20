# Bandit Level 3 → 4
## 🎯 Objective
Read the password from a hidden file inside a directory called `inhere`

## 💻 Commands Used
ssh bandit3@bandit.labs.overthewire.org -p 2220
ls
cd inhere
ls -a
cat ...Hiding-From-You

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Listed files using ls and found a directory called inhere
- Changed into the inhere directory using cd
- Used ls -a to reveal hidden files (files starting with a dot)
- Found a hidden file called ...Hiding-From-You
- Read it using cat to get the password

## 💡 What I Learned
- Hidden files and directories in Linux start with a dot (.)
- Regular ls does not show hidden files
- ls -a reveals all files including hidden ones

## ✅ Password Found
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
