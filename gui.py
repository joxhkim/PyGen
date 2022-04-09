from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.popup import Popup
from gen import *


class PyGen(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.description = Label(
            text="Which program or website will you be using this password for?: ")
        self.window.add_widget(self.description)

        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)

        generate = Button(text="Generate", on_press=self.generate,
                          on_release=self.openPopupWindow)
        self.window.add_widget(generate)

        return self.window

    def openPopupWindow(self, obj):
        layout = GridLayout(cols=1)
        button = Button(text="OK", size_hint=(0.5, 0.2),
                        on_press=self.closePopupWindow)
        layout.add_widget(button)

        self.popup = Popup(title="Successfully generated", content=layout,
                           size_hint=(0.5, 0.2), auto_dismiss=False)
        self.popup.open()

    def closePopupWindow(self, obj):
        self.popup.dismiss()

    def generate(self, obj):
        app = self.user.text
        gen(app)
        self.user.text = ""


if __name__ == "__main__":
    PyGen().run()
