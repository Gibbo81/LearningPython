class Super:
    counting=0
    def __init__(self):
        self.count=Super.counting
        Super.counting = Super.counting+1
    def method(self):
        print('in Super.method') # Default behavior
    def delegate(self):
     self.action() # Expected to be defined

class Inheritor(Super): # Inherit method verbatim
    pass

class Replacer(Super): # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super): # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super): # Fill in a required method
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):       #Here we do not create the istance!
        print('\n' + klass.__name__ + '...')
        klass().method()
        print('\nProvider...')
        print(klass().count)
    x = Provider()
    x.delegate()