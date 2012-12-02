#
#  main.py
#  Demo
#
#  Created by Greg Neagle on 12/2/12.
#  Copyright MacTech 2012. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import MTAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
