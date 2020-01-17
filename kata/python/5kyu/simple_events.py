class Event:
    def __init__(self):
        self.handlers = []

    def subscribe(self, fun):
        self.handlers += [fun]

    def unsubscribe(self, fun):
        self.handlers.remove(fun)

    def emit(self, *args):
        for h in self.handlers:
            h(*args)


event = Event()


class Testf:
    def __init__(self):
        self.calls = 0
        self.args = []

    def __call__(self, *args):
        self.calls += 1
        self.args += args


f = Testf()

event.subscribe(f)
event.emit(1, 'foo', True)
    
print(f.calls, 1)  # calls a handler
print(f.args, [1, 'foo', True])  # passes arguments
    
event.unsubscribe(f)
event.emit(2)
    
print(f.calls, 1)  # no second call
