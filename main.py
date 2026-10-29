from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex

class CoDCalculator(App):
    def build(self):
        self.title = "COD MISSION: CALCULATE"
        
        # رنگ‌های تم نظامی کالاف
        c_black = get_color_from_hex("#255C73")
        c_dark_gray = get_color_from_hex("#255C73")
        c_green = get_color_from_hex("#255C73")
        c_white = get_color_from_hex("#255C73")
        
        # لایه اصلی
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # صفحه نمایش اعداد
        self.display = TextInput(
            text='',
            multiline=False,
            readonly=True,
            halign='right',
            font_size=42,
            background_color=c_black,
            foreground_color=c_green,
            size_hint=(1, 0.25)
        )
        main_layout.add_widget(self.display)
        
        # گرید دکمه‌ها
        buttons_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))
        
        # لیست دکمه‌ها
        buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', 'DEL'
        ]
        
        for btn_text in buttons:
            # رنگ دکمه مساوی خاص باشه
            bg_color = c_green if btn_text == '=' else c_dark_gray
            txt_color = c_black if btn_text == '=' else c_white
            
            btn = Button(
                text=btn_text,
                font_size=26,
                bold=True,
                background_normal='',
                background_color=bg_color,
                color=txt_color
            )
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)
            
        main_layout.add_widget(buttons_layout)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        
        if text == 'C':
            self.display.text = ''
        elif text == 'DEL':
            self.display.text = self.display.text[:-1]
        elif text == '=':
            try:
                # محاسبه نتیجه
                result = str(eval(self.display.text))
                self.display.text = result
            except Exception:
                self.display.text = 'ERROR'
        else:
            if self.display.text == 'ERROR':
                self.display.text = ''
            self.display.text += text

if __name__ == '__main__':
    CoDCalculator().run()
