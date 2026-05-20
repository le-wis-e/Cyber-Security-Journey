# Bandit Level 5 → 6
## 🎯 Objective
Find the password stored in a file with the following properties:
- Human-readable
- 1033 bytes in size
- Not executable

## 💻 Commands Used
ssh bandit5@bandit.labs.overthewire.org -p 2220
ls
cd inhere
find . -type f -size 1033c ! -executable
cat ./maybehere07/.file2

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Found a directory called inhere with 20 subdirectories inside
- Used find with multiple flags to filter by file type, exact size and executable status
- Found the file at ./maybehere07/.file2
- Read it using the full path cat ./maybehere07/.file2
- Found the password (file had trailing whitespace padding to make up 1033 bytes)

## 💡 What I Learned
- find can search by multiple properties at once (-type, -size, ! -executable)
- c in -size means exact bytes (1033c = exactly 1033 bytes)
- ! -executable means the file is not executable
- Always use the full path returned by find when using cat
- Files can be padded with whitespace to reach a specific byte size

## ✅ Password Found
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
