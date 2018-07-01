# the Window base class
class Window(object):
    def draw(self, device):
        device.append('flat window')

    def info(self):
        pass


# The decorator pattern approch
class WindowDecorator:
    def __init__(self, w):
        self.window = w

    def draw(self, device):
        self.window.draw(device)

    def info(self):
        self.window.info()


class BorderDecorator(WindowDecorator):
    def draw(self, device):
        self.window.draw(device)
        device.append('borders')


class ScrollDecorator(WindowDecorator):
    def draw(self, device):
        self.window.draw(device)
        device.append('scroll bars')


def Main():
    # The way of using the decorator classes
    w = ScrollDecorator(BorderDecorator(Window()))
    dev = []
    w.draw(dev)
    print(dev)


Main()
