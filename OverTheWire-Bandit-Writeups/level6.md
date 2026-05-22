# Bandit Level 6 → 7
## 🎯 Objective
Find the password stored somewhere on the server with the following properties:
- Owned by user bandit7
- Owned by group bandit6
- 33 bytes in size

## 💻 Commands Used
ssh bandit6@bandit.labs.overthewire.org -p 2220
find / -type f -user bandit7 -group bandit6 -size 33c
cat /var/lib/dpkg/info/bandit7.password

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Used find from the root / to search the entire server
- Filtered by file type, owner user, owner group and exact size
- Got many Permission denied errors but ignored them
- Spotted the result /var/lib/dpkg/info/bandit7.password among the errors
- Read it using cat to get the password

## 💡 What I Learned
- find / searches the entire server from root
- -user and -group flags filter files by their owner
- Permission denied errors are normal when searching the whole server as bandit6 cannot access everything
- The actual result appears among the errors so you have to look carefully

## ✅ Password Found
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj