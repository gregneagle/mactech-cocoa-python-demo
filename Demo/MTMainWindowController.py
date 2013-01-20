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
    
    @IBAction
    def buildPackage_(self, sender):
        applicationPath = self.applicationFld.stringValue()
        installLocation = self.installLocationFld.stringValue()
        identifier = self.identifierFld.stringValue()
        version = self.versionFld.stringValue()
        
        NSLog('Application path: %s' % applicationPath)
        NSLog('Install location: %s' % installLocation)
        NSLog('Identifier: %s' % identifier)
        NSLog('Version: %s' % version)

    def awakeFromNib(self):
        self.applicationFld.setStringValue_(u'/path/to/Some.app')
        self.installLocationFld.setStringValue_(u'/Applications')
        self.identifierFld.setStringValue_(u'com.mactech.demo')
        self.versionFld.setStringValue_(u'1.0')
