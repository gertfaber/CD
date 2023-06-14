# Result PYTEST
[![Run Tests](https://github.com/gertfaber/my-project/actions/workflows/run-tests.yml/badge.svg)](https://github.com/gertfaber/my-project/actions/workflows/run-tests.yml)


# Three main components of my solution:
1.	Folder with Code on PC: Here I wrote all the code for the deployment of my website. 
2.	Repository of Code on Github: Here I stored a copy of my code.
3.	Droplet on Digital Ocean server: On this server my website is hosted. A droplet is a Linux-based Virtual Private Server (VPS). 
## Relation between 3 main components:
Via git commands on the PC you can push/upload the code to the Github server. Besides storing code, Github can also run your code with Github Actions. To do this you have to add the folder .github\workflows to you main code folder with a .yml file inside. In this .yml file you specify what you want Github Actions to do. In my case, Github Actions first tested the code. If the test did not encounter any errors, Github Actions logged in to the Droplet on the Digital Ocean server, and used git commands to pull/download the repository to the Droplet. On the Droplet Gunicorn is installed and set to read our main.py file in the farm folder, in which I created a simple website using Flask (just printed: “'Hello, world farm2!'”): http://178.62.203.180/ 

# Three problems and how I solved them:
1.	**PROBLEM**: How to connect to the droplet using Git Actions.  
**SOLUTION**: I solved this by googling and watching a bunch of videos. The challenge was to find a suitable video. First, I found a lot of videos that used the docker platform which was not useful for me. But I learned a lot by watching the videos (eg., https://youtu.be/uijgmwOdcXQ). Finally, I found a more useful video after getting some tips from a Winc mentor: https://youtu.be/gW1TDirJ5E4.
2.	**PROBLEM**: I was a bit overwhelmed/confused by having to combine all the different tools (Flask, Gunicorn, SSH Github, Github Actions, Droplets, SSH, secret keys, Ngnix) and all commands/code involved.  
**SOLUTION**: To understand better how to combine all this tools/knowledge in this assignment, I did most of the previous exercises we did with these tools again, and made a small manual for myself with important code to remember. 
3.	**PROBLEM**: To test the git pull command, I first cloned the repository to another folder on my PC. After, I changed some things in the original folder and pushed it to github. Then I tried pulling it to the new (cloned) folder, but it did not work.  
**SOLUTION**: Together with a mentor we found out that it did not work because I changed one file in the cloned folder that I use to make some notes (Code Notes.py). Because of this Github, gave an error when I tried to pull the data. So, the solution is not to change any files in your cloned folder, but only in the original folder.


 
