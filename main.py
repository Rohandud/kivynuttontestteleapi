from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import telebot

bot = telebot.TeleBot('6549292499:AAHacZBWyJ8p2ZAmdZj94II941lF638UV7Q')  # Replace with your actual bot token

class ButtonApp(App):
    def send_message_to_user(self, txt):
        USER_ID = 922758956
        bot.send_message(USER_ID, txt)

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Define two buttons
        button1 = Button(text='Button 1')
        button2 = Button(text='Button 2')

        # Bind functions to the on_press events of the buttons
        button1.bind(on_press=self.on_button_press)
        button2.bind(on_press=self.on_button_press)

        # Add buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout

    def on_button_press(self, instance):
        # This function will be called when a button is pressed
        print(f'Button {instance.text} pressed')
        
        # Schedule sending a message to the user after a delay
        Clock.schedule_once(lambda dt: self.send_message_to_user(f'Button {instance.text} pressed'), 1)

if __name__ == '__main__':
    ButtonApp().run()
