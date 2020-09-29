#!/usr/bin/env python3

from PIL import Image
import os
import json


def resizeAndSaveAsJpeg(inputfilepath, outputfilepath):
  img = Image.open(inputfilepath)
  img = img.convert('RGB')

  #resize to 600x400
  img_resize = img.resize((600,400))

  #save as jpeg
  img_resize.save(outputfilepath,"JPEG")

  return img_resize


def main():
  settingpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"setting.json")

  with open(settingpath) as f:
    config = json.load(f)

  INPUTDIR=config['imagefolder']
  OUTPUTDIR=INPUTDIR


  for curDir, dirs, files in os.walk(INPUTDIR):
  #  print(files)
    for file in files:
      #operate tiff file only
      if  not  os.path.splitext(file)[1] == ".tiff":
        continue

      #make filename
      filepath = os.path.join(curDir,file)
      newfilename = os.path.splitext(file)[0] +".jpeg"
      outfilepath = os.path.join(OUTPUTDIR,newfilename)

      try:
        resizeAndSaveAsJpeg(filepath, outfilepath)
      except Exception as e:
        print(e)
        
    break




if __name__ == "__main__":
  main()
