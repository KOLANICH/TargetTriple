#!/usr/bin/env python3
import sys
from pathlib import Path
from collections import OrderedDict
import unittest

thisFile = Path(__file__).absolute()
thisDir = thisFile.parent.absolute()
repoMainDir = thisDir.parent.absolute()
sys.path.insert(0, str(repoMainDir))

dict = OrderedDict

from TargetTriple import TargetTriple

class SimpleTests(unittest.TestCase):
	def testSimple(self):
		self.assertEqual(str(TargetTriple("x86_64", "linux", "gnu")), "x86_64-linux-gnu")

	def testKeyability(self):
		a = {TargetTriple("x86_64", "linux", "gnu"): 1}
		self.assertEqual(a[TargetTriple("x86_64", "linux", "gnu")], 1)


if __name__ == "__main__":
	unittest.main()
