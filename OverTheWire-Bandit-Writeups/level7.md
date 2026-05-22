# Bandit Level 7 → 8
## 🎯 Objective
Find the password stored in data.txt next to the word millionth

## 💻 Commands Used
ssh bandit7@bandit.labs.overthewire.org -p 2220
ls
grep "millionth" data.txt

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Listed files using ls and confirmed data.txt exists
- Used grep to search for the word millionth inside data.txt
- Found the password next to the word millionth

## 💡 What I Learned
- grep searches for a word or pattern inside a file
- grep "word" filename returns the line containing that word
- Linux is exact with filenames, one wrong character will cause a file not found error
- .txt and .text are different extensions, Linux treats them as completely different files

## ✅ Password Found
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc