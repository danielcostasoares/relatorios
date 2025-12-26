from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from datetime import date

from database.consultas import listar_publicadores, status_relatorio


class ListaPublicadores(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10)

        self.filtro_grupo = MDTextField(
            hint_text="Filtrar por grupo (opcional)",
            input_filter="int"
        )

        btn_filtrar = MDRaisedButton(
            text="Aplicar filtro",
            on_release=self.carregar
        )

        self.lista = MDList()

        layout.add_widget(self.filtro_grupo)
        layout.add_widget(btn_filtrar)
        layout.add_widget(self.lista)

        self.add_widget(layout)
        self.carregar()

    def carregar(self, *_):
        self.lista.clear_widgets()

        grupo = self.filtro_grupo.text
        grupo = int(grupo) if grupo else None

        mes_atual = date.today().month
        ano_servico = date.today().year + (1 if mes_atual >= 9 else 0)

        for pid, nome, grupo in listar_publicadores(grupo):
            status = status_relatorio(pid, ano_servico, mes_atual)

            self.lista.add_widget(
                OneLineListItem(
                    text=f"{nome}  |  Grupo {grupo}  |  {status}"
                )
            )
