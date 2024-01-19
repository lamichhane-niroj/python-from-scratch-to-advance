#Constructor is the magic function that will be invoked whenever object is created, so necessary things can be initialize at first

# COC without gui
class Coc:
    def __init__(self, conn: bool, main: bool):
        # assert the value to the above or below threshold using assert keyword
        # assert quantity >= 0, "string for error"
        self.connection = conn
        self.maintenence = main
        print('Opening clash of clans')
        self.checkconnection() 

    def checkconnection(self):
        if not self.connection:
            print('You are not connected with internet')
        else:
            self.checkmaintenance()

    def checkmaintenance(self):
        if self.maintenence:
            print('Maintenance break occured')
        else:
            self.showfrontpage()
            self.traintroops()
            self.battle()

    def showfrontpage(self):
        print('showing image')
        print('loading----')
        print('Spring trap doesn\'t work on pekkas')
    
    def traintroops(self):
        print('Troops added to the barrack')

    def battle(self):
        print('Ready to battle')
    

user1 = Coc(True,False)
