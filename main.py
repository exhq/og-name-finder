import json 
import requests

while 420>69:

    seetaken = (input("do you want to see taken accounts? (y/n):  "))
    if seetaken == "y" or "n":
        break
    else: 
        print("no, i said choose between y/n")

while 3>2:
    randomnumb = requests.get(f"https://random-word-api.herokuapp.com/word?number=1")
    randomnumbstr = str(randomnumb.json())
    x = (randomnumbstr.replace('"', '').replace("'", "").replace('[',"").replace('[',"").replace(']',""))

    
    resp = requests.get(f"https://api.ashcon.app/mojang/v2/user/{x}")
    jsoo = str(resp.json())
    if jsoo.startswith("{'code': 404,") == True:
        print(f"{x} - account available")
    elif jsoo.startswith("{'code': 400,") == True:
        if seetaken == "y":
            print(f"ok what the fuck, this account isnt supposed to exist")
    elif jsoo.startswith("{'uuid':") == True:
        if seetaken == "y":
            print(f"{x} - account taken")
