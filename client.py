import socket
import json
from pystyle import Box, Colors, Colorate , Write, Center
#address and port
port = 8688
ip = '127.0.0.1'
addr= (ip,port)


 
def main_menu():
   print(Box.DoubleCube("main menu"))
   print("1- Search headlines")
   print("2- List of sources")
   print("3- Quite")
   
def search_headlines_menu():
    print(Box.DoubleCube("headlines menu"))
    print("1- Search for keyword")
    print("2- Search by category")
    print("3- Search by country")
    print("4- list all new headlines")
    print("5- back to main menu") 
 
def list_of_source_menu():
       print(Box.DoubleCube("source menu"))    
       print("1- Search by category")
       print("2- Search by country")
       print("3- search by language")
       print("4- list all sources")
       print("5- back to main menu")
       
       
       
def start_client():
 connected = True
 while connected: 
  client_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_soket.connect(addr)
  print(Box.Lines("Welcome to the news app"))
  client_name = input("Enter your name: ")
  client_soket.send(client_name.encode())
  Write.Print(f"CLinet name :{client_name} Connected to server at {ip}:{port} \n", Colors.white_to_blue, interval=0.01)
    

  print("\n")
  main_menu()
  userinput = input("- Enter your option: ", ) 
   
  if userinput == "1":  
        print("\n")
        search_headlines_menu()
        request_data = {
         "apiKey": "5adb9309522544a98697fb257eee3f8b",
         "client_name": client_name,
         "pageSize": 15,
      
          }
        option = input("Enter your option: ")
        if option == "1":
          parms = input("Enter your keyword: ")
          request_data.update({"q":parms})
          
        elif option == "2":
          parms = input("Enter your category: ")
          request_data.update({"category":parms})
        elif option == "3":
           parms = input("Enter your country: ")
           request_data.update({"country":parms})
        elif option == "4":
           parms1 = input("Enter your keyword: ")
           parms2 = input("Enter your category: ")
           parms3 = input("Enter your country: ")
           request_data.update({"q":parms1})
           request_data.update({"category":parms2})
           request_data.update({"country":parms3})
            
           
        elif option == "5":
           continue;
       
        request_data.update({"choice":option})
        request_data.update({"suorce_or_headlines":userinput})
        client_soket.send(json.dumps(request_data).encode('utf-8'))
        response = client_soket.recv(1024).decode('utf-8')
        Write.Print(f"We have received the following response from the server: \n ", Colors.white_to_blue, interval=0.01)
        Write.Print(response, Colors.white_to_blue, interval=0.0001)
        print("\n")



        
        if response != "No articles found":
         print("\n")
         more_details = input("choice which one of them you whant to get more detiles abuot: ")
         client_soket.send(more_details.encode('utf-8'))
         result = client_soket.recv(1024).decode('utf-8')
         Write.Print(f"We have received the following response from the server: \n ", Colors.white_to_blue, interval=0.01)
         Write.Print(result, Colors.white_to_blue, interval=0.01)

  
        
        

           
           
    
  elif userinput == "2":
       print("\n")
       list_of_source_menu()
       
       choice = (input("- Enter your choice: "))
       request_data = {
         "apiKey": "5adb9309522544a98697fb257eee3f8b",
         "choice": "choice",
         "client_name": f"{client_name}",
         "pageSize": 15,
      
          }
       if choice == "1":
          parms = input("Enter your category: ")
          request_data.update({"category":parms})
       elif choice == "2":
         parms = input("Enter your country: ")
         request_data.update({"country":parms})
       elif choice == "3":
         parms = input("Enter your language: ")
         request_data.update({"language":parms})
       elif choice == "4":
         parms1 = input("Enter your category: ")
         parms2 = input("Enter your country: ")
         parms3 = input("Enter your language: ")
         request_data.update({"category":parms1})
         request_data.update({"country":parms2})
         request_data.update({"language":parms3})
       elif choice == "5":
         continue;
     
       request_data.update({"choice":choice})
       request_data.update({"suorce_or_headlines":userinput})
       client_soket.send(json.dumps(request_data).encode('utf-8'))
       response = client_soket.recv(4096).decode('utf-8')
       Write.Print(f"We have received the following response from the server: \n ", Colors.white_to_blue, interval=0.01)
       Write.Print(response, Colors.white_to_blue, interval=0.0001)
       print("\n")


       if response != "No source found":
         print("\n")
         more_details = input("choice which one of them you whant to get more detiles abuot: ")
         client_soket.send(more_details.encode('utf-8'))
         result = client_soket.recv(1024).decode('utf-8')
         Write.Print(f"We have received the following response from the server: \n ", Colors.white_to_blue, interval=0.01)
         Write.Print(result, Colors.white_to_blue, interval=0.0001)


  
      
         
    
       
  elif userinput == "3":
       Write.Print(f"Thank you !!", Colors.white_to_green, interval=0.01)
       connected = False
       break;
   
 client_soket.close()

       
   
if __name__ == "__main__":
 start_client()

       



       




   
   
   
   
   
   

   
        
