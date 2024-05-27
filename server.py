import socket
import requests
import threading
import json


# Function to check the type of data received from the client
def check_type_data_of_request(data) :
 try:
    i =json.loads(data)
    return type(i)
 except json.JSONDecodeError:
    return False



# Function to get the headlines from the News API
def get_headlines(det):
    main_url = "https://newsapi.org/v2/top-headlines?"
    try:
        response = requests.get(main_url, params=det)
        
        # Check if the response is successful
        if response.status_code == 200:
            print("type of response:", type(response))
            return response.json()
        else:
            print(f"Failed to retrieve headlines, status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to retrieve headlines: {e}")
        return None
   


# Function to get the headlines from the News API
def get_sources(det):
    main_url = "https://newsapi.org/v2/top-headlines/sources?"
    response = requests.get(main_url, params=det)
    try: 
     # Check if the response is successful
     if response.status_code == 200:
        print("type of response:", type(response))
        return response.json()
     else:
        print(f"Failed to retrieve headlines, status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to retrieve headlines: {e}")
        return None



def create_json_file(resalt,name, option):
    file_name = f"<group_B10>_<{name}>_<{option}>.json"
    with open(file_name, 'w') as file:
            json.dump(resalt, file, indent=4)
            


# Function to get lest of hedlines
def lest_of_hedlines(headlines) :
  result_str = ""
  articles = headlines.get("articles", [])
  num_articles = len(articles)
  print(f"Number of articles: {num_articles}")
  
  
  if num_articles !=0 :
      for i, article in enumerate(headlines["articles"], 1):
        source_name = article["source"]["name"]
        author = article.get("author", "Unknown Author")
        title = article.get("title", "No Title")
        
        result_str += (
            f"Number: {i}\n"
            f"Source: {source_name}\n"
            f"Author: {author}\n \n"    
          )
      
  elif num_articles == 0:
        result_str = "No articles found"
        
  return result_str



# Function to get lest of sources
def lest_of_soruces(data) :
  result_str = ""
  sources = data.get("sources", [])
  num_sources = len(sources)

  
  if num_sources !=0 :
      for i, source in enumerate(data["sources"], 1):
        source_name = source.get("name", "Unknown Source")
        
        result_str += (
            f"Number: {i}\n"
            f"source_name : {source_name}\n"   
          )
      
  elif num_sources == 0:
        result_str = "No source found"
        
  return result_str


# Function to get details of spacific source    
def get_detiles_source(headlines , index):
  result_str = ""
  sources = headlines.get("sources", [])
  num_sources = len(sources)
  
  print(f"Number of articles: {num_sources }")

  if index <= num_sources  :
    
        source_name = sources[index-1]["name"] 
        country = sources[index-1]["country"]
        category = sources[index-1]["category"]
        url = sources[index-1]["url"]
        description = sources[index-1]["description"]
        language =sources[index-1]["language"]
        
        
        result_str += (
            f"Source: {source_name}\n"
            f"country: {country}\n"
            f"Description: {description}\n"
            f"URL: {url}\n"
            f"category: {category}\n"
            f"language : {language}\n\n"
        )
  else:
      result_str ="No articles found"
      
  return result_str


# Function to get details of spacific artical
def get_detiles_artical(headlines , index):
  result_str = ""
  articles = headlines.get("articles", [])
  num_articles = len(articles)
  
  print(f"Number of articles: {num_articles}")

  if index <= num_articles :
    
        source_name = articles[index-1]["source"]["name"] 
        author = articles[index-1]["author"]
        title = articles[index-1]["title"]
        url = articles[index-1]["url"]
        description = articles[index-1]["description"]
        published_at =articles[index-1]["publishedAt"]
        
        # Split the date and time from publishedAt
        if "T" in published_at:
            publish_date, publish_time = published_at.split("T")
            publish_time = publish_time.rstrip("Z")
        else:
            publish_date = published_at
            publish_time = "No Publish Time"
        
        result_str += (
            f"Source: {source_name}\n"
            f"Author: {author}\n"
            f"Title: {title}\n"
            f"URL: {url}\n"
            f"Description: {description}\n"
            f"Publish Date: {publish_date}\n"
            f"Publish Time: {publish_time}\n\n"
        )
  else:
      result_str ="No articles found"
      
  return result_str



def handle_client(client_socket):
    # Receive data from the client
 while True:
    request = client_socket.recv(1024).decode('utf-8')
   
    
    if check_type_data_of_request(request) == type({}):
        # Parse the request (assuming it's in JSON format)
        resalt =json.loads(request)
        
        
        # Extract parameters from the request
        client_name = resalt.pop("client_name")        
        option = resalt.pop("choice")
        source_or_headlines = resalt.pop("suorce_or_headlines")
    
        # send the request to api
        list =""
        if source_or_headlines == "1":
         print(f"[Info] {client_name} request headlines withe thes parameters : \n {request} " )
         api_response = get_headlines(resalt )
        #save the response in the list variable
         list=lest_of_hedlines(api_response)
         
        else :
         print(f"[Info] {client_name} request sources withe thes parameters : \n {request} " )
         api_response = get_sources(resalt)
         #save the response in the list variable
         list=lest_of_soruces(api_response)
    
        
        create_json_file(api_response, client_name, option)
    
        #send the response in the list variable to the client
        client_socket.send(list.encode('utf-8'))
        print ("--------------next--------------")


  
    # the next client request to get more details
    if check_type_data_of_request(request) == type(10):
        
        request = request.encode('utf-8')
        index = int(request)
        if source_or_headlines == "1":
            print(f"[Info] {client_name} request detiles of artical withe this parameters : \n {index} " )
            resp = get_detiles_artical(api_response, index)
        else:
            print(f"[Info] {client_name} request detiles of source withe this parameters : \n {index} " )
            resp = get_detiles_source(api_response, index)
      
        print(resp)
        client_socket.send(resp.encode('utf-8'))
        client_socket.close()
        print(f"[Info] {client_name} is disconnect now " )
        break
    

    
    
    # Close the client socket





# Function to start the server
def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a host and port
    server_socket.bind(('127.0.0.1', 8688))
    
    # Listen for incoming connections
    server_socket.listen()
    print("[INFO] Server is listening on port 8888...")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        name =client_socket.recv(1024)
        print(f"[INFO] Accepted connection from {client_address[0]}:{client_address[1]} with name: {name.decode('utf-8')}")
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
        

if __name__ == "__main__":
    start_server()
    