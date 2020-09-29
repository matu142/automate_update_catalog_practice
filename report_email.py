#!/usr/bin/env python3

import os
import json
import datetime

from reports import generate_report


def createContent(textfolderpath):
  result = ""
  for textfile in os.listdir(textfolderpath):
    textfilepath = os.path.join(textfolderpath, textfile)
    with open(textfilepath) as f:
      name = f.readline().rstrip()
      weight = f.readline().rstrip()
      result += "name: {}<br/>weight: {} lbs<br/><br/>".format(name, weight)

  return result

def createTitle():
  d =datetime.date.today()
  return "Processed Update on " +d.strftime( "%B %d, %Y")

def main():
  settingpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"setting.json")

  with open(settingpath) as f:
    config = json.load(f)

  PDFFILEPATH=config['pdfpath']
  TEXTFOLDER = config['textfolder']
  title = createTitle()
  content = createContent(TEXTFOLDER)
  generate_report(PDFFILEPATH,title,content)
  

if __name__ == "__main__":
  main()
