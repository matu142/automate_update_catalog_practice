import os
import json
import requests

def addFruit(url, textfilepath) :
  #operate each file
  with open(textfilepath, "r") as f:
    #read text file
    name = f.readline().rstrip()
    weight = int(f.readline().rstrip())
    description = f.read().rstrip()

    imagefilename = os.path.splitext(os.path.basename(textfilepath))[0] + ".jpeg"

    #create request data
    data = {
        "name":name
        ,"weight": weight
        ,"description":description
        ,"image_name" : imagefilename
    }

    #throw request
    response = requests.post(url,json=data)

    #analyze response
    print("text: {} \nstatus_code: {} \ntext(response): {}".format(
      textfilepath, response.status_code, response.text[:]))


def checkExistImageFile(textfilename, imagedir):
  imagefilepath = os.path.join(imagedir,os.path.splitext(textfilename)[0]+".jpeg")
  return os.path.exists(imagefilepath)


def main():
  settingpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"setting.json")

  with open(settingpath) as f:
    config = json.load(f)

  INPUTDIR=config['textfolder']
  IMAGEDIR=config['imagefolder']
  APIURL = config['addFruitEndpoint']

  for textfile in os.listdir(INPUTDIR):

    #create full path of a text file
    textfilepath = os.path.join(INPUTDIR, textfile)

    #check exist image file
    if checkExistImageFile(textfilepath, IMAGEDIR):
      addFruit(APIURL, textfile)
    else :
      raise Exception("image not found for {}".format(textfile))


if __name__ == "__main__":
  main()
