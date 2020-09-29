import unittest
from unittest import mock

import os

from reports import generate_report


class TestCheckExistImageFile(unittest.TestCase):
  def test_createPDF(self):
    filepath = "./test.pdf"
    generate_report(filepath,"test title", "body line1.<br/> body line2<br/>")
    self.assertTrue(os.path.exists(filepath))


if __name__ == '__main__':
    unittest.main()