from kivymd.app import MDApp
from ui.lista_publicadores import ListaPublicadores
from database.db import criar_banco

class SecretarioApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        criar_banco()
        return ListaPublicadores()

if __name__ == "__main__":
git commit    SecretarioApp().run()
