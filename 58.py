class vscode:
    def execute(self):
        print("compiling")
        print("running")

class myedit:
    def execute(self):
        print("spell")
        print("check")
        print("compiling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=myedit()

a1=Laptop()
a1.code(ide)