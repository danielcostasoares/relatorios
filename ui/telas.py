from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.toast import toast

from database.publicadores import adicionar_publicador
from pdf.s21 import criar_cartao_ano_servico
from pathlib import Path
from datetime import date


class CadastroPublicador(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        self.nome = MDTextField(hint_text="Nome completo")
        self.nascimento = MDTextField(hint_text="Data de nascimento (dd/mm/aaaa)")
        self.batismo = MDTextField(hint_text="Data de batismo (dd/mm/aaaa)")
        self.sexo = MDTextField(hint_text="Sexo (M ou F)")
        self.grupo = MDTextField(hint_text="Grupo (1, 2, 3...)")

        self.designacoes = MDTextField(hint_text="Designações (ex: Ancião)")
        self.privilegios = MDTextField(hint_text="Privilégios (ex: Pioneiro Regular)")
        self.esperanca = MDTextField(hint_text="Esperança (Outras ou Ungido)")

        botao = MDRaisedButton(
            text="Salvar e criar cartão",
            pos_hint={"center_x": 0.5},
            on_release=self.salvar
        )

        for campo in [
            self.nome, self.nascimento, self.batismo,
            self.sexo, self.grupo,
            self.designacoes, self.privilegios, self.esperanca
        ]:
            layout.add_widget(campo)

        layout.add_widget(botao)
        self.add_widget(layout)

    def salvar(self, *_):
        adicionar_publicador(
            self.nome.text,
            self.nascimento.text,
            self.batismo.text,
            self.sexo.text,
            self.designacoes.text,
            self.privilegios.text,
            self.esperanca.text,
            int(self.grupo.text)
        )

        ano_servico = date.today().year + (1 if date.today().month >= 9 else 0)

        BASE_DIR = Path(__file__).resolve().parent.parent

        criar_cartao_ano_servico(
            modelo_pdf=BASE_DIR / "S-21_T.pdf",
            pasta_cartoes=BASE_DIR / "dados/cartoes",
            nome_completo=self.nome.text,
            data_nascimento=self.nascimento.text,
            data_batismo=self.batismo.text,
            sexo=self.sexo.text,
            designacoes=[self.designacoes.text],
            privilegios=[self.privilegios.text],
            esperanca=self.esperanca.text,
            ano_servico=ano_servico
        )

        toast("Publicador cadastrado com sucesso!")
