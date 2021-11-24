Doctor challenge has a web server running on port 80 as well as port 8000 
The target port for the third challenge was port 80 

Recon: 
Initial nmap results showed 

Nmap scan report for 139.59.34.34
Host is up (0.020s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
**80/tcp   open  http    Apache httpd 2.4.38 ((Debian))**
| http-robots.txt: 1 disallowed entry 
**|_/gazette **
|_http-title: Health - Medical Website Template
8000/tcp open  http    Node.js Express framework
|_http-title: Smash - Bootstrap Business Template
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

On visiting /gazette we can find that the page offers a login. 
On viewing the source code we creds of amit are revealed 

user : amit
pass : HackTheHacker

On accessing the page it reveals sensitive information about the user including mobile number and email id.
