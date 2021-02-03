import sys
err = sys.stderr
import nose
import re
from nose.plugins import Plugin

class RegexPicker(Plugin):
    name = "regexpicker"
    def __init__(self):
        Plugin.__init__(self)
        self.verbose = False
