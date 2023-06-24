from kivy.app import App
from kivy.uix.button import Button
# from kivy.uix.layout import

class MyApp(App):
    def build(self):

        btn = Button(text='Кажись работает')
        # btn2 = Button(text="Кажись работает 2")

        return btn

if __name__ == "__main__":
    MyApp().run()
