from kivy.app import App
from kivy.uix.button import Button
# kv file MUST be named as the name of the class in lowercase minus "App"
class LanguageLearnerApp(App): # A  subclass of type XxxXxxAPP is mandatory with Kivy
    def build(self): 
        return Button(text="Hello World") # We create a widget


if __name__ == '__main__':
    LanguageLearnerApp().run()