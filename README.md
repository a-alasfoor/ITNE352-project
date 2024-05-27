# News app

## Project Description:
A news application takes a request of a news source or headline with a specific parameter from the user and returns the response from the API and display it to the user

## Table of Contents
- [Project Description](#project-description)
- [Made by](#made-by)
- [Requirements](#requirements)
- [How to](#how-to)
- [The scripts](#the-scripts)
  - [On client side](#on-client-side)
  - [On server side](#on-server-side)
- [Additional concept](#additional-concept)
- [Acknowledgments](#acknowledgments)
- [Conclusion](#conclusion)
## Made by :
 Ammar ali alasfoor and mahmood raed
 Gorup 10 , ITNE_352_section 2 



## Requirements 
### Youe should install PyStyle freamwork by typing in command line:

```
pip3 install pystyle
```
## How to
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









## Additional concept
When the server receives a response from the API, it stores the data in a JSON file by using the write file concept. We use this concept in the create_json_file() function, which takes three arguments:

- Response from API on dictionary object
- Name of client 
- Option of request that client chooses

```pyhthon 
def create_json_file(resalt,name, option):
 file_name = f"<group_B10>_<{name}>_<{option}>.json"
 with open(file_name, 'w') as file:
     json.dump(resalt, file, indent=4)
```

## Acknowledgments
Therefore, the first thing that we would want to mention is our gratitude to our doctor. We have had the opportunity to learn and improve our coding skills by doing this project. Ideas related to the complex area of network have been better taught and understood through his teachings. Also, he has been of great help in introducing us to Git & GitHub, something that will be of much assistance now and in the future. It means that with the help of these tools, one can demonstrate the work to others and expand the set of commands in cmd for projects.

## Conclusion
At the end, we hope the documentation was a helpful and meaningful explanation.
 