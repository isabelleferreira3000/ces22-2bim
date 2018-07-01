import platform


class GuiFactory():
    """Abstract Factory"""

    @classmethod
    def getFactory(Class):
        if platform.system() == "Windows":
            return WinFactory()
        elif platform.system() == "OSX":
            return OSXFactory()
        elif platform.system() == "Linux":
            return LinuxFactory()

    class Button:
        """ Abstract Product"""

        def paint(self):
            raise NotImplementedError

    @classmethod
    def getButton(Class):
        return Class.Button()


class WinFactory(GuiFactory):
    """Concrete Factory"""

    class Button(GuiFactory.Button):
        """Concrete Product"""

        def paint(self):
            print("I am a Windows button")


class LinuxFactory(GuiFactory):
    """Concrete Factory"""

    class Button(GuiFactory.Button):
        """Concrete Product"""

        def paint(self):
            print("I am a Linux button")


class OSXFactory(GuiFactory):
    """Concrete Factory"""

    class Button(GuiFactory.Button):
        """Concrete Product"""

        def paint(self):
            print("I am a OSX button")


def main():
    """Application"""
    factory = GuiFactory.getFactory()
    factory.getButton().paint()


if __name__ == "__main__":
    main()