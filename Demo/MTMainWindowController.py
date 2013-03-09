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
import subprocess

class MTMainWindowController(NSWindowController):

    applicationFld = IBOutlet()
    installLocationFld = IBOutlet()
    identifierFld = IBOutlet()
    versionFld = IBOutlet()
    
    def getApplicationPath(self):
        '''Display NSOpenPanel to get the path to an
        application to package.
        Returns a pathname or None'''
    
        # instantiate open panel object
        panel = NSOpenPanel.openPanel()
        # allow only .app files
        panel.setAllowedFileTypes_(['app'])
        # set the intiallly displayed directory
        # to /Applications
        panel.setDirectoryURL_(
            NSURL.fileURLWithPath_('/Applications'))
        # set the default button name to
        # 'Select' instead of the default 'Save'
        panel.setPrompt_(u'Select')
        # set a custom panel title
        # instead of the default 'Open'
        panel.setTitle_(u'Select an application')
    
        # show the Open panel
        result = panel.runModal()
        if result:
            # return the pathname from the
            # first (only) URL
            return panel.URLs()[0].path()
        else:
            # user clicked Cancel
            return None

    def getApplicationBundleInfo_(self, app_path):
        '''Uses Foundation methods to read an application's 
           Info.plist'''
        
        info_path = os.path.join(
                    app_path, 'Contents/Info.plist')
        if not os.path.exists(info_path):
            return {}
        
        plistData = NSData.dataWithContentsOfFile_(
                    info_path)
        dataObject, plistFormat, error = \
            NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_(
                plistData, NSPropertyListMutableContainers,
                None, None)
        if error:
            return {}
        return dataObject

    def getSavePath_(self, app_path):
        '''Uses app_path to generated a suggested name for
        the package to be saved, then opens a Save panel. 
        Returns the chosen pathname or None'''
        
        # get just the name from app_path
        appname = os.path.splitext(
                      os.path.basename(app_path))[0]
        pkgname = appname + '.pkg'
        
        # instantiate the save panel object
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
    def getApplication_(self, sender):
        pathname = self.getApplicationPath()
        if pathname:
            self.applicationFld.setStringValue_(pathname)
            info_dict = self.getApplicationBundleInfo_(
                        pathname)
            identifier = info_dict.get(
                         'CFBundleIdentifier', '')
            version = info_dict.get(
                      'CFBundleShortVersionString', '')
            self.identifierFld.setStringValue_(identifier)
            self.versionFld.setStringValue_(version)
            self.installLocationFld.setStringValue_(
                u'/Applications')
            
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
        
        if not save_path:
            # user cancelled Save dialog
            return
        
        # call pkgbuild to build our package
        pkgbuild = '/usr/bin/pkgbuild'
        cmd = [pkgbuild,
               '--install-location', installLocation,
               '--component', applicationPath,
               '--identifier', identifier,
               '--version', version,
               save_path]
        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError, err:
            NSLog('ERROR: %s' % err)

    def awakeFromNib(self):
        self.getApplication_(self)
        self.installLocationFld.setStringValue_(u'/Applications')
