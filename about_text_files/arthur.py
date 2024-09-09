def message ():
    """Display a simple message"""
    print('I am Arthur')
    print('King of the Britons')

message()

def message (king_name):
    """Display a message with parameter"""
    print('I am', king_name)
    print('King of the Britons')

# Call the message function.
message('Henry VIII')

def message(king_name, kingdom):
    """Display positional arguments"""
    print('I am', king_name)
    print('King of the', kingdom)

# Call the message function.
message (kingdom = 'Lions', king_name = 'Mufasa')

def message (king_name, kingdom = 'Egypt'):
    """Display default value"""
    print ('I am', king_name)
    print ('King of', kingdom)

# Call the message function
message ('Tut')
