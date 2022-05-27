from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBody, TwoLineAvatarIconListItem
from kivymd.uix.button import MDIconButton

from utils import avans_saver


class MainWindow(MDBoxLayout):
    pass


class RightButton(IRightBody, MDIconButton):
    pass


class SearchResultItem(TwoLineAvatarIconListItem):
    pass


class MainApp(MDApp):
    def search_name_result(self, query):
        pass

    def save_user_and_switch_to_search(self, name, avans):
        if avans_saver(name, avans):
            pass

    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MainApp().run()
