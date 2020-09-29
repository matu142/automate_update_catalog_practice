import unittest
from unittest import mock
import re
import os
from report_email import createTitle
from report_email import createContent

TEXTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),"supplier_data","descriptions")

class TestCreateTitle(unittest.TestCase):
  def test_createTitle(self):
    title = createTitle()
    print(title)
    self.assertIsNotNone(re.match(r'^Processed Update on [A-Z][a-z]{2,} \d+, \d+$', title))

  def test_createContent(self):
    contents = createContent(TEXTDIR)
    print(contents)
    self.assertIsNotNone(re.match(r'^name:.*weight: \d+ lbs', contents))


if __name__ == '__main__' :
  unittest.main()