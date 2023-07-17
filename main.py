import json 
import requests

while 420>69:
    seetaken = (input("do you want to see taken accounts? (y/n):  "))
    if seetaken == "y" or seetaken == "n":
        break
    else: 
        print("no, i said choose between y/n")

while 3>2:
    x= str(requests.get(f"https://random-word-api.herokuapp.com/word?number=1")).replace('"', '').replace("'", "").replace('[',"").replace(']',"")

    
    jsoo = str(requests.get(f"https://api.ashcon.app/mojang/v2/user/{x}").json())
    if jsoo.startswith("{'code': 404,") == True:
        print(f"{x} - account available")
    elif jsoo.startswith("{'code': 400,") == True and seetaken == "y":
            print("ok what the fuck, this account isnt supposed to exist")
    elif jsoo.startswith("{'uuid':") == True and seetaken == "y":
            print(f"{x} - account taken")
