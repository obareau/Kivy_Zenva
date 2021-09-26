from kivy.app import App
from kivy.uix.button import Button
# kv file MUST be named as the name of the class in lowercase minus "App"

class FunkyButton(Button):
    pass
    # def __init__(self, **kwargs):
    #     super(FunkyButton, self).__init__(**kwargs)
    #     self.text="Funky Button" 
    #     self.pos=(100,100) # We don't needs comma anymore it's no longer a list of values    
    #     self.size_hint=(.25,.25 )
        
class LanguageLearnerApp(App): # A  subclass of type XxxXxxAPP is mandatory with Kivy
    def build(self): 
        return FunkyButton(
            pos=(100,100),
            size_hint=(None,None ), # Responsive design !!!
            size=(100,100) #size seems to have benn modified from version 1,11,1 
            ) # We create a widget -- positioning in kivy start from bottom left !!!


if __name__ == '__main__':
    LanguageLearnerApp().run()