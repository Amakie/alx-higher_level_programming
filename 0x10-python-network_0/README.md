Project: 0x10-python-network_0
This project aims to enhance your understanding of fundamental concepts related to networking, HTTP, and cURL. Below are the learning objectives, requirements, and tasks to be completed.

Learning Objectives
After completing this project, you should be able to explain the following concepts without the help of Google:

General
What a URL is
What HTTP is
How to read a URL
The scheme for an HTTP URL
What a domain name is
What a sub-domain is
How to define a port number in a URL
What a query string is
What an HTTP request is
What an HTTP response is
What HTTP headers are
What the HTTP message body is
What an HTTP request method is
What an HTTP response status code is
What an HTTP Cookie is
How to make a request with cURL
What happens when you type google.com in your browser (Application level)
Copyright - Plagiarism
Understanding the importance of avoiding plagiarism.
Strict adherence to ethical guidelines and avoiding copying and pasting someone else's work.
The prohibition of publishing any content related to this project.
Requirements
General
Allowed editors: vi, vim, emacs
A README.md file at the root of the project folder is mandatory.
All Bash scripts must be exactly 3 lines long (wc -l file should print 3).
All files should end with a new line.
All files must be executable.
The first line of all Bash files should be #!/bin/bash.
The second line of all Bash scripts should be a comment explaining the script's purpose.
All curl commands must include the -s option (silent mode).
All files will be tested on Ubuntu 20.04 LTS.
All Bash scripts should be tested in the provided sandbox using the web server running on port 5000.
The first line of all Python files should be #!/usr/bin/python3.
Code should follow PEP 8 style guidelines (pycodestyle version 2.8.*).
All modules, classes, and functions should be documented.
Tasks
0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
The size must be displayed in bytes.
Use curl for the request.
1. cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
Display only the body of a 200 status code response.
Use curl for the request.
2. cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
Use curl for the request.
3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
Use curl for the request.
4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
Include the header variable X-School-User-Id with the value 98.
Use curl for the request.
5. cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the URL, and displays the body of the response.
Include POST parameters: email with the value test@gmail.com and subject with the value I will always be here for PLD.
Use curl for the request.
6. Find a peak
Write a Python function, find_peak(list_of_integers), that finds a peak in a list of unsorted integers.
The function must have the lowest complexity.
Document the complexity of your algorithm in 6-peak.txt (O(log(n)), O(n), O(nlog(n)), or O(n^2)).