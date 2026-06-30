from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# 🎨 Dark background
Window.clearcolor = (0.08, 0.08, 0.10, 1)


class Calculator(App):

    def build(self):

        self.result = TextInput(
            font_size=40,
            size_hint=(1, 0.2),
            readonly=True,
            halign="right",
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(0, 1, 1, 1)
        )

        layout = GridLayout(cols=4, spacing=8, padding=10)

        layout.add_widget(self.result)

        buttons = [
            "C", "(", ")", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=", "⌫"
        ]

        for btn_text in buttons:
            btn = Button(
                text=btn_text,
                font_size=28,
                background_color=self.get_color(btn_text),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=self.on_press)
            layout.add_widget(btn)

        return layout

    def get_color(self, text):
        if text in ["=", "+", "-", "*", "/"]:
            return (0.2, 0.6, 1, 1)   # blue
        elif text == "C":
            return (1, 0.3, 0.3, 1)   # red
        elif text == "⌫":
            return (1, 0.6, 0, 1)     # orange
        else:
            return (0.15, 0.15, 0.2, 1)  # dark grey

    def on_press(self, instance):
        text = instance.text

        if text == "C":
            self.result.text = ""
            return

        if text == "⌫":
            self.result.text = self.result.text[:-1]
            return

        if text == "=":
            try:
                self.result.text = str(eval(self.result.text))
            except:
                self.result.text = "Error"
            return

        if self.result.text == "Error":
            self.result.text = ""

        self.result.text += text


if __name__ == "__main__":