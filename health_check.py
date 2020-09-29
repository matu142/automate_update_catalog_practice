#!/usr/bin/env python3
import psutil
import socket
import time
import os
import json

from emails import generate_email, send_email


def checkCPUusage(threshold) :
  """Return false if CPU usage is over `threshold`%"""
  usage = psutil.cpu_percent()
  if usage > threshold :
    return False
  else:
    return True


def checkDiskSpace(threshold):
  """Return false if disk space is less than `threshold`% in '/' """
  data = psutil.disk_usage('/').percent 
  free_space_percent = 100 - data
  if  free_space_percent < threshold :
    return False
  else:
    return True

def checkMemoryUsage(threshold) :
  """Return false if memory available is less than `threshold` MB  """
  data = psutil.virtual_memory().available
  if data  < threshold * 1024 * 1024:
    return False
  else:
    return True

def checkResolveLocalhost() :
  """Return false if the hostname "localhost" cannot be resolved to 127.0.0.1 """
  ip = socket.gethostbyname("localhost")
  if ip == "127.0.0.1" :
    return True
  else:
    return False


def sendErrorMail(sender, recipient, title):
  body = "Please check your system and resolve the issue as soon as possible."
  msg = generate_email(sender,recipient,title,body,"")
  send_email(msg)

def main() :
  settingpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"setting.json")

  with open(settingpath) as f:
    config = json.load(f)

  MAILFROM = config['mailfrom']
  MAILTO = config['mailto']

  while True :
    print("checking...")
    if not checkCPUusage(80) :
      sendErrorMail(MAILFROM, MAILTO, "Error - CPU usage is over 80%")

    if not checkDiskSpace(20) :
      sendErrorMail(MAILFROM, MAILTO, "Error - Available disk space is less than 20%")
    
    if not checkMemoryUsage(500) :
      sendErrorMail(MAILFROM, MAILTO, "Error - Available memory is less than 500MB")

    if not checkResolveLocalhost() :
      sendErrorMail(MAILFROM, MAILTO, "Error - localhost cannot be resolved to 127.0.0.1")

    time.sleep(60)

if __name__ == '__main__' :
  main()
  