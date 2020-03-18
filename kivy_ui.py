import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView


# UI DEF
class SMLM(App):
	def build(self):
		layout = BoxLayout(orientation="horizontal")
		layout.add_widget(ModList())
		layout.add_widget(BottomButtons())
		return layout


class ModList(ScrollView):
	def __init__(self, **kwargs):
		super(ModList, self).__init__(**kwargs)
		self.size_hint_y = None
		self.size = (100, 50)
		self.add_widget(Label(text="SCROLL BOX"))


class BottomButtons(BoxLayout):
	def __init__(self, **kwargs):
		super(BottomButtons, self).__init__(**kwargs)
		self.orientation = 'vertical'

		self.btn_sort = Button(text="Sort")
		self.btn_sort.bind(on_press=sort_action)
		self.add_widget(self.btn_sort)

		self.btn_apply = Button(text="Apply")
		self.btn_apply.bind(on_press=apply_action)
		self.add_widget(self.btn_apply)


# BUTTON DEF
def sort_action(btn):
	print("SORTED!")


def apply_action(btn):
	print("APPLIED!")


# DEV RUN
if __name__ == '__main__':
	SMLM().run()
