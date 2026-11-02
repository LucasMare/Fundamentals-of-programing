def isValidCommand(command):
    valid_commands = ["add", "undo", "ls"]
    if command not in valid_commands: 
        raise ValueError("Invalid command")

def isValidAddArg(arg):#to be tested
    valid_args = ["--new", "-n", "--help", "-h"]
    if arg not in valid_args:
        raise ValueError("Invalid argument for add command")

def isValidNewArgs(args): #to be tested
    if len(args)!=4: raise ValueError("Invalid amount of arguments! Please input the start and end date(dd/mm/yyyy), destination and price of the travel")