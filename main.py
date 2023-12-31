from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# from testtele import send_message_to_user

class ButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Define two buttons
        button1 = Button(text='Button 1')
        button2 = Button(text='Button 2')

        # Bind functions to the on_press and on_release events of the buttons
        button1.bind(on_press=self.on_button_press, on_release=self.on_button_release)
        button2.bind(on_press=self.on_button_press, on_release=self.on_button_release)

        # Add buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout

    def on_button_press(self, instance):
        # This function will be called when a button is pressed
        print(f'Button {instance.text} pressed')

    def on_button_release(self, instance):
        # This function will be called when a button is released
        # send_message_to_user(f'Button {instance.text} pressed')
        print(f'Button {instance.text} released')

if __name__ == '__main__':
    ButtonApp().run()
