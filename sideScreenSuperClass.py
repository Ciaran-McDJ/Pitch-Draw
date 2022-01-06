import typing 
import variables


class SideScreenSuperClass():
    """class to have some rigidity between the side screen's the initiateScreen and update function should be overiden by the child, cleanup can also be overiden but if so make sure to resetactiveTextBox to None"""
    def __init__(self) -> None:
        self.groupsOfMutuallyExclusiveButtons:typing.List[variables.mutuallyExclusiveButtons] = []
        self.textBoxes:typing.List[variables.TextBox] = []
    
    def initiateScreen(self):
        print("Hey you didn't override the super's initiateScreen function!")
    
    
    def cleanupScreen(self):
        variables.TextBox.activeTextBox = None #This is all that really needs to happen in general. If required the screen can overide this
    
    
    def update(self):
        print("Hey you didn't override the super's update function!")