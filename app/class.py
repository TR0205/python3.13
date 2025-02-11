class Car(object):
    def __init__(self, model=None):
        self.model = model
        # print('init')
    def run(self):
        print('run')

class ToyotaCar(Car):
    def __init__(self, model=None, enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print('toyota')

c = ToyotaCar('Lexus')
c.enable_auto_run = True
print(c.enable_auto_run)
