import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    name= ObjectProperty(None)
    pizza = ObjectProperty(None)



    def press(self):
        name = self.name.text
        pizza = self.pizza.text


        #self.add_widget(Label(text=f"hello, {name}, your pizza is {pizza}"))
        print(f"hello, {name}, your pizza is {pizza}")

        #to clear the  output
        name = self.name.text = ""
        pizza = self.pizza.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()