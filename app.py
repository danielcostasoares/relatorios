from kivymd.app import MDApp
from ui.telas import CadastroPublicador
from database.db import criar_banco


class SecretarioApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        criar_banco()
        return CadastroPublicador()


if __name__ == "__main__":
    SecretarioApp().run()
