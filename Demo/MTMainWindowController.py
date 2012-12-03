#
#  MTMainWindowController.py
#  Demo
#
#  Created by Greg Neagle on 12/2/12.
#  Copyright (c) 2012 MacTech. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *

class MTMainWindowController(NSWindowController):
    
    textField = IBOutlet()
    
    def awakeFromNib(self):
        self.textField.setStringValue_(u'Hello World!')

    @IBAction
    def okBtnClicked_(self, sender):
        NSApp.terminate_(self)
