import unittest
from unittest import mock

import os
from supplier_image_upload import uploadfile

INPUTFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","images","001.jpeg")
INPUTFILENOTEXIST = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","images","xxxxx")

URL = "http://dummyurl"


def mocked_post(*args, **kargs):
  print("--mocked_post start--")
  print(args)
  print(kargs)
  print("--mocked_post end--")


class TestUploadFile(unittest.TestCase):
  @mock.patch("requests.post", side_effect=mocked_post)
  def test_file(self,mock1):
    uploadfile(URL,INPUTFILE)
    self.assertTrue(True)

    with self.assertRaises(Exception):
        uploadfile(URL,INPUTFILENOTEXIST)


if __name__ == '__main__':
    unittest.main()