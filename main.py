from kivymd.app import MDApp


class Myapp(MDApp):
    def build(self):
        return

    def data(self):
        print("Username:", self.root.ids.data.text)
        print("Password:", self.root.ids.data1.text)


Myapp().run()
