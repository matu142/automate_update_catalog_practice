import unittest
import os
from changeImage import resizeAndSaveAsJpeg

INPUTFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","images","001.tif")
OUTPUTFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","images","test001.jpeg")
class TestResizeAndSaveAsJpeg(unittest.TestCase):
  def test_tiff(self):
    img = resizeAndSaveAsJpeg(INPUTFILE,OUTPUTFILE)
    self.assertTrue(os.path.exists(OUTPUTFILE))




if __name__ == '__main__':
    unittest.main()