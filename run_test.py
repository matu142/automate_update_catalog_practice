import unittest
from unittest import mock

import os
from run import checkExistImageFile
from run import addFruit

IMAGEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","images")
INPUTFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","descriptions","001.txt")
INPUTFILE_NOIMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","descriptions","002.txt")

INPUTFILENOTEXIST = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","descriptions","999.txt")

URL = "http://dummyurl"


def mocked_post(*args, **kargs):
  print("--mocked_post start--")
  print(args)
  print(kargs)
  print("--mocked_post end--")
  return type("dummyresponse", (object,), {"status_code": 201, "text": "mock response xxxx"})

class TestCheckExistImageFile(unittest.TestCase):
  def test_file(self):
    self.assertTrue(checkExistImageFile(os.path.basename(INPUTFILE),IMAGEDIR))
    self.assertFalse(checkExistImageFile(os.path.basename(INPUTFILE_NOIMAGE),IMAGEDIR))


class TestAddFruit(unittest.TestCase):
  @mock.patch("requests.post", side_effect=mocked_post)
  def test_file(self,mock1):
    addFruit(URL,INPUTFILE)
    self.assertTrue(True)
    mock1.return_value =  type("dummyresponse", (object,), {"status_code": 500, "text": "mock response xxxx"})
    with self.assertRaises(Exception):
      addFruit(URL,INPUTFILENOTEXIST)



if __name__ == '__main__':
    unittest.main()