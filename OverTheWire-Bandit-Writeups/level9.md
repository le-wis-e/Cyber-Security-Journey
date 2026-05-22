# Bandit Level 9 → 10
## 🎯 Objective
Find the password stored in data.txt in one of the few human-readable strings preceded by = signs

## 💻 Commands Used
ssh bandit9@bandit.labs.overthewire.org -p 2220
ls
strings data.txt | grep "="

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Listed files using ls and found data.txt
- Used strings to extract all human-readable text from the binary file
- Piped the output into grep to filter for lines containing = signs
- Found the password preceded by several == signs

## 💡 What I Learned
- strings extracts human-readable text from binary files
- Binary files contain mostly garbage data with some readable text hidden inside
- Combining strings and grep with a pipe helps narrow down results quickly
- The password was revealed as part of a readable sentence: "the password is FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey"

## ✅ Password Found
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey