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

import os

class MTMainWindowController(NSWindowController):

    applicationFld = IBOutlet()
    installLocationFld = IBOutlet()
    identifierFld = IBOutlet()
    versionFld = IBOutlet()
    
    def getSavePath_(self, app_path):
        '''Uses app_path to generated a suggested name for
        the package to be saved, then opens a Save panel. 
        Returns the chosen pathname or None'''
        
        # get just the name from app_path
        appname = os.path.splitext(
                      os.path.basename(app_path))[0]
        pkgname = appname + '.pkg'
        
        # instantiate the save panel
        panel = NSSavePanel.savePanel()
        # set default package name
        panel.setNameFieldStringValue_(pkgname)
        # '.pkg' extension is mandatory
        panel.setAllowedFileTypes_(['pkg'])
        # show the extension in the dialog
        panel.setExtensionHidden_(NO)
        # set the default button name to
        # 'Build' instead of the default 'Save'
        panel.setPrompt_(u'Build')
        # set the panel title to 'Build package'
        # instead of the default 'Save'
        panel.setTitle_(u'Build package')
        
        # show the Save panel
        result = panel.runModal()
        if result:
            # return the pathname
            return panel.URL().path()
        else:
            # user clicked Cancel
            return None

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
    
        save_path = self.getSavePath_(applicationPath)
        NSLog('Save path: %s' % save_path)

    def awakeFromNib(self):
        self.applicationFld.setStringValue_(u'/path/to/Some.app')
        self.installLocationFld.setStringValue_(u'/Applications')
        self.identifierFld.setStringValue_(u'com.mactech.demo')
        self.versionFld.setStringValue_(u'1.0')
