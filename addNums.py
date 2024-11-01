from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class AddNumsApp(App):
    def build(self):
        self.title = 'Add Numbers'
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input1 = TextInput(multiline=False, size_hint=(1, 0.2),
                                hint_text='Enter an integer')
        self.input2 = TextInput(multiline=False, size_hint=(1, 0.2),
                                hint_text='Enter an integer')

        self.adding_button = Button(text='Add', size_hint=(1, 0.4))
        self.adding_button.bind(on_press=self.add)

        self.result = Label(text='', size_hint=(1, 0.4))

        self.layout.add_widget(self.input1)
        self.layout.add_widget(self.input2)
        self.layout.add_widget(self.adding_button)
        self.layout.add_widget(self.result)

        return self.layout

    def add(self, instance):
        num1_text = self.input1.text
        num2_text = self.input2.text

        # Check if both inputs are valid integers
        if num1_text.isdigit() and num2_text.isdigit():
            num1 = int(num1_text)
            num2 = int(num2_text)
            result = num1 + num2
            self.result.text = f'Result: {result}'
        else:
            self.result.text = 'Please enter valid integers'


AddNumsApp().run()