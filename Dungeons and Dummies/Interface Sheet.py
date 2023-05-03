from copyreg import pickle
import PySimpleGUI as sg
import json


class telasheet:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome', size=(4, 0)), sg.Input(size=(15, 0), k='name'), sg.Text('Raça', size=(4, 0)), sg.Input(size=(
                10, 0), key='race'), sg.Text('Classe:'), sg.Input(size=(10, 0), key='class'), sg.Push(), sg.Text('C.A'), sg.Input(size=(3, 0), key='ca')],
            [sg.Text('Alinhamento', size=(9, 0)), sg.Input(size=(12, 0), key=('align')), sg.Text('Exp:', size=(4, 0)), sg.Input(size=(
                12, 0), key='experience'), sg.Text('Lvl:', size=(4, 0)), sg.Input(size=(3, 0), key='level'), sg.Push(), sg.Multiline(size=(14, 3), no_scrollbar=True)],
            [sg.Text('For', size=(3, 0)), sg.Input(size=(3, 0), key='str'), sg.Text('Des', size=(3, 0)), sg.Input(size=(3, 0), key='dex'), sg.Text('Con', size=(3, 0)), sg.Input(size=(3, 0), key='con'), sg.Text('Int', size=(3, 0)), sg.Input(
                size=(3, 0), key='int'), sg.Text('Sab', size=(3, 0)), sg.Input(size=(3, 0), key='wisd'), sg.Text('Car', size=(3, 0)), sg.Input(size=(3, 0), k='char'), sg.Push(), sg.Text('Iniciativa'), sg.Input(size=(3, 0), k='ini')],
            [sg.Push(), sg.Text('HP', text_color='Red'), sg.Push(), sg.Text('MP', text_color='Blue'), sg.Push(
            ), sg.Text('Desvantagens', size=(14)), sg.Push(), sg.Text('Idiomas', size=(12)), sg.Push()],
            [sg.Push(), sg.Multiline(size=(5, 4), k='hp', no_scrollbar=True), sg.Push(), sg.Multiline(size=(5, 4), k='hp', no_scrollbar=True), sg.Push(
            ), sg.Multiline(size=(14, 4), k='weak', no_scrollbar=True), sg.Push(), sg.Multiline(size=(12, 4), k='lang', no_scrollbar=True), sg.Push(), sg.Push()],
            [sg.HorizontalSeparator()],
            [sg.Push(), sg.Text('Inventário'), sg.Push(),
             sg.Push(), sg.Text('Habilidades'), sg.Push()],
            [sg.Multiline(size=(36, 20), k='inv'), sg.VSep(),
             sg.Multiline(size=(36, 20), k='heb')],
            [sg.SaveAs('Salvar', file_types=".json")], [sg.FileBrowse('Open')]
        ]

        # Janela
        self.sheet = sg.Window('Character Sheet').layout(layout)

    def iniciar(self):
        while True:
            # Extrair dados tela
            self.button, self.values = self.sheet.Read()
            nome = self.values['name']
            with open(f'{nome}.json', 'w') as prs:
                json.dump(self.values, prs)


tela = telasheet()
tela.iniciar()
