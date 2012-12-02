#
#  DemoAppDelegate.py
#  Demo
#
#  Created by Greg Neagle on 12/2/12.
#  Copyright MacTech 2012. All rights reserved.
#

from Foundation import *
from AppKit import *

class MTAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
