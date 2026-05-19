# Bandit Level 1 → 2
## 🎯 Objective
Read the password from a file called `-` in the home directory

## 💻 Commands Used
ssh bandit1@bandit.labs.overthewire.org -p 2220
ls
cat ./-

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Listed files using ls
- Found a file named `-`
- Could not use cat - directly as bash interprets `-` as stdin
- Used cat ./- to explicitly reference the file by path
- Found the password

## 💡 What I Learned
- Files with special names like `-` need a workaround to read
- Prefixing with ./ forces bash to treat the name as a file path rather than a flag

## ✅ Password Found
263JGJPfgU6LtdEvgfWU1XP5yac29mFx
