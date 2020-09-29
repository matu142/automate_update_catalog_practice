#!/usr/bin/env python3

import os
import json
import datetime

from reports import generate_report
from emails import generate_email
from emails import send_email


def createContent(textfolderpath):
  result = ""
  for textfile in os.listdir(textfolderpath):
    textfilepath = os.path.join(textfolderpath, textfile)
    with open(textfilepath) as f:
      name = f.readline().rstrip()
      weight = f.readline().rstrip()
      result += "name: {}<br/>weight: {}<br/><br/>".format(name, weight)

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
  MAILFROM = config['mailfrom']
  MAILTO = config['mailto']
  MAILSUBJECT = "Upload Completed - Online Fruit Store"
  MAILBODY = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  title = createTitle()
  content = createContent(TEXTFOLDER)
  generate_report(PDFFILEPATH,title,content)

  mail_message = generate_email(MAILFROM,MAILTO,MAILSUBJECT,MAILBODY, PDFFILEPATH)  
  send_email(mail_message)

  

if __name__ == "__main__":
  main()
