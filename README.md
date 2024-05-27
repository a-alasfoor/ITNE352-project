# News app

## Project Description:
A news application take a request of news sources or hedlines with spacific parmeeter from user and return the response from API 
and display to the user
## Made by :
 Ammar ali alasfoor and mahmood raed
 Gorup 10 , ITNE_352_section 2 

## Table of Contents

## Requirements : 
### Youe should install PyStyle freamwork by typing in command line:

```
pip3 install pystyle
```
## How to: 
After installing the Pystyle framework, you can run the programme smoothly by taking the scripts as we write them, then running the server script first and then the client script.
## The scripts
### on client side :
- On clinte script start_client() is the main funtion that request from user to enter his name and then call miues functions

- After choiceing from miues and enter some information that classified the request , request send by clinet script to server script . This is a main_menu() function that called by start_client():

```pyhthon 
def main_menu():
   print(Box.DoubleCube("main menu"))
   print("1- Search headlines")
   print("2- List of sources")
   print("3- Quite")
```

### On server side :
- On clinte script we use multithreaded technique to handle multiple clint requests

- there many functions on server scripts, and handle_client() one of them , the jop of it start after accepting a client by receiving a client request and hendel it and processing among other functions










## Acknowledgments

## conclusion
This is a small documentation news app that explains the idea of it and how it works.
 
 