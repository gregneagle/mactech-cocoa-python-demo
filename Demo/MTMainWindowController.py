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

    applicationFld = IBOutlet()
    installLocationFld = IBOutlet()
    identifierFld = IBOutlet()
    versionFld = IBOutlet()

    def awakeFromNib(self):
        self.applicationFld.setStringValue_(u'/path/to/Some.app')
        self.installLocationFld.setStringValue_(u'/Applications')
        self.identifierFld.setStringValue_(u'com.mactech.demo')
        self.versionFld.setStringValue_(u'1.0')
