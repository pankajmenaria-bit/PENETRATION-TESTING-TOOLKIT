# PENETRATION-TESTING-TOOLKIT
*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PANKAJ MENARIA

*INTERN ID*: CT08SOJ

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

#The project consists of two main functionalities: Port Scanning and Brute Force Attack.

# Port Scanning
When the user clicks the "Run Port Scanner" button, the application captures the target IP Address or domain from the input field.
It then uses the socket library to scan ports from 20 to 1025.
The socket tries to connect to each port, and if the connection is successful (status code 0), it considers the port Open.
The result is displayed in the result box.

#Brute Force Attack
When the user clicks the "Run Brute Force Attack" button, the application captures the target URL from the input field.
It then uses the requests library to send POST requests to the target URL with a predefined list of commonly used passwords.
If the response does not contain any failure message (like "incorrect password"), it assumes the password was correct and displays it.
If no password matches, it shows a failure message.

#Technologies Used
Technology	Purpose
Python 3	Main programming language
PyQt5	Used for GUI (Graphical User Interface)
Socket	Used for TCP Port Scanning
Requests	Used for sending HTTP POST requests in brute-force
QPalette	Used to design the dark red theme for the app
