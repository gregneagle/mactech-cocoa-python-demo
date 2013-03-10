#
#  MTAppDelegate.py
#  Demo
#
#  Created by Greg Neagle on 12/2/12.
#  Copyright MacTech 2012. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *

class MTAppDelegate(NSObject):
    
    main_window_controller = IBOutlet()
    
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
        self.main_window_controller.getApplication_(self)
