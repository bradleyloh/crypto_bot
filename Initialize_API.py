from binance.client import Client

def InitializeAPI():

    file1 = open('api_key.txt', 'r') 
    Lines = file1.readlines()
    apiarray = []

    for line in Lines: 
        apiarray.append(line.strip())
    client = Client(apiarray[0], apiarray[1])
    return client