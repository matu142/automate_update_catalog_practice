#! /usr/bin/env python3

import os
import requests
import json


def uploadFile(url, filepath) :
  with open(filepath , "rb") as f :
    requests.post(url, files={"file":f})
    #print(filepath,url)




def main():
  settingpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"setting.json")

  with open(settingpath) as f:
    config = json.load(f)

  INPUTDIR=config['imagefolder']
  APIURL = config['imageUploadEndpoint']

  for curDir, dirs, files in os.walk(INPUTDIR):
  #  print(files)
    for file in files:

      extention = os.path.splitext(file)[1]
      #if not jpeg file  then skip
      if ".jpeg" != extention :
        continue

      filepath = os.path.join(curDir,file)

      try:
        uploadFile(APIURL,filepath)
      except Exception as e:
        print(e)
        
    break



if __name__ == "__main__":
  main()
