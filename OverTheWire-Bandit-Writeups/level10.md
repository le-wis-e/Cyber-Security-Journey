# Bandit Level 10 → 11
## 🎯 Objective
Find the password stored in data.txt which contains base64 encoded data

## 💻 Commands Used
ssh bandit10@bandit.labs.overthewire.org -p 2220
ls
base64 -d data.txt

## 🔍 What I Did
- Logged in using SSH with the previous level's password
- Listed files using ls and found data.txt
- Used base64 -d to decode the base64 encoded contents of the file
- Found the password in the decoded output

## 💡 What I Learned
- base64 is an encoding scheme that converts binary data into readable text
- base64 -d decodes base64 encoded data back to its original form
- Encoded data is not encrypted, it can always be decoded without a key

## ✅ Password Found
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr