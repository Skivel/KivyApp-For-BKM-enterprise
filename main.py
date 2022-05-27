from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBody, TwoLineAvatarIconListItem
from kivymd.uix.button import MDIconButton

from utils import avans_saver, show_all_for_name


class MainWindow(MDBoxLayout):
    pass


class RightButton(IRightBody, MDIconButton):
    pass


class SearchResultItem(TwoLineAvatarIconListItem):
    pass


class MainApp(MDApp):
    def search_name_result(self, query):
        app = MDApp.get_running_app()
        result_list_widget = app.root.ids.search_results
        result_list_widget.clear_widgets()
        for users in show_all_for_name(query):
            result_list_widget.add_widget(
                SearchResultItem(text=f"{users[0]}", secondary_text=f"{users[1]}")
            )

    def save_user_and_switch_to_search(self, name, avans):
        if avans_saver(name, avans):
            app = MDApp.get_running_app()
            sm = app.root.ids.bottom_nav
            sm.switch_tab("screen home")

    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MainApp().run()
