from kivy.app import App
from kivy.uix.button import Button
# kv file MUST be named as the name of the class in lowercase minus "App"
class LanguageLearnerApp(App): # A  subclass of type XxxXxxAPP is mandatory with Kivy
    def build(self): 
        return Button(
            text="Hello World",
            pos=(50,50)
            ) # We create a widget -- positioning in kivy start from bottom left !!!


if __name__ == '__main__':
    LanguageLearnerApp().run()