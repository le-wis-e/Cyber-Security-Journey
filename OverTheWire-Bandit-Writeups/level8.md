# Bandit Level 8 → 9
## 🎯 Objective
Find the password stored in data.txt that occurs only once

## 💻 Commands Used
ssh bandit8@bandit.labs.overthewire.org -p 2220
ls
sort data.txt | uniq -u

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Listed files using ls and found data.txt
- Used sort to arrange all lines alphabetically so duplicates are grouped together
- Piped the output into uniq -u to show only the line that appears exactly once
- Found the password

## 💡 What I Learned
- sort arranges lines alphabetically grouping duplicates together
- uniq -u filters to show only lines that appear exactly once
- uniq only works on consecutive lines so sort must be used first
- The | pipe sends the output of one command as input to the next command

## ✅ Password Found
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM