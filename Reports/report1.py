class First(object):
    def __init__(self):
        print ("first")
class Second(object):
    def __init__(self):
        print ("second")
class Third(First, Second):
        def __init__(self):
            super(Third, self).__init__()
            print ("that's it")
class Fourth(First, Second):
        def __init__(self):
            super(First, self).__init__()
            print ("that's it")  
class Five(First, Second):
        def __init__(self):
            super(Second, self).__init__()
            print ("that's it")                      
ob1=Third()
#output
# first
#that's it
ob2=Fourth()
#output
# second
#that's it
ob3=Five()
#output
#that's it

            




        
            