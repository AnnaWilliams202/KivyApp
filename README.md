# KivyApp
# another version to perform more operations 
 def calculate(self, instance):
        try:
            num1 = float(self.num1.text)
            num2 = float(self.num2.text)
            if self.operation.text == "Add":
                result = num1 + num2
            elif self.operation.text == "Subtract":
                result = num1 - num2
            elif self.operation.text == "Multiply":
                result = num1 * num2
            elif self.operation.text == "Divide":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Unknown operation"
            self.result_label.text = f'Result: {result}'
        except ValueError:
            self.result_label.text = "Please enter valid numbers."


# version with separate functions 

This solution modularizes the code by creating separate functions for each operation. This improves readability and maintainability and allows for easy expansion.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
 
class ModularCalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
 
        # Input fields
        self.num1 = TextInput(multiline=False, size_hint=(1, 0.2), hint_text="Enter first number")
        self.num2 = TextInput(multiline=False, size_hint=(1, 0.2), hint_text="Enter second number")
 
        # Dropdown for selecting operation
        self.operation = Spinner(text="Add", values=["Add", "Subtract", "Multiply", "Divide"], size_hint=(1, 0.2))
        
        self.result_label = Label(text='Result: ', size_hint=(1, 0.4))
 
        # Button to perform calculation
        self.calculate_button = Button(text='Calculate', size_hint=(1, 0.2))
        self.calculate_button.bind(on_press=self.calculate)
 
        # Add widgets to layout
        self.layout.add_widget(self.num1)
        self.layout.add_widget(self.num2)
        self.layout.add_widget(self.operation)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)
        return self.layout
 
    def calculate(self, instance):
        try:
            num1 = float(self.num1.text)
            num2 = float(self.num2.text)
            operation = self.operation.text
 
            # Call the respective function based on the operation
            result = {
                "Add": self.add(num1, num2),
                "Subtract": self.subtract(num1, num2),
                "Multiply": self.multiply(num1, num2),
                "Divide": self.divide(num1, num2)
            }.get(operation, "Unknown operation")
            
            self.result_label.text = f'Result: {result}'
        except ValueError:
            self.result_label.text = "Please enter valid numbers."
 
    # Define individual operations
    def add(self, a, b):
        return a + b
 
    def subtract(self, a, b):
        return a - b
 
    def multiply(self, a, b):
        return a * b
 
    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"
