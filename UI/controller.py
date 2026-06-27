import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno=None
        self._forma=None

    def fillDDAnni(self):
        anni = self._model.getAnni()
        anniDDI = list(map(lambda x: ft.dropdown.Option(x, on_click=self._choiceAnnoI), anni))

        self._view.ddyear.options = anniDDI

        self._view.update_page()

    def fillDDForme(self):
        forme = self._model.getForma()
        fDDI = list(map(lambda x: ft.dropdown.Option(x, on_click=self._choiceForma), forme))

        self._view.ddshape.options = fDDI

        self._view.update_page()

    def _choiceForma(self,e):
        self._forma=e.control.data



    def _choiceAnnoI(self,e):
        self._anno=e.control.data

    def handle_graph(self, e):
        anno = self._view.ddyear.value
        forma = self._view.ddshape.value

        if anno is None or forma is None:
            self._view.txt_result1.controls.append(ft.Text("Attenzione, selezionare un anno e una forma"))
            self._view.update_page()
            return

        self._model.creaGrafo(forma, anno)
        n, m = self._model.getGraphDetails()
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo correttamente creato! ", color="green"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di nodi: {n}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {m}"))

        compConn=self._model.get_num_connesse()
        self._view.txt_result1.controls.append(ft.Text(f"Il grafo ha {compConn} componenti connesse"))
        compMaggiore, lunghezza = self._model.compConnMaggiore()
        self._view.txt_result1.controls.append(ft.Text(f"La più grande componente connessa è lunga {lunghezza}"))
        for c in compMaggiore:
            self._view.txt_result1.controls.append(ft.Text(c))

        self._view.update_page()
    def handle_path(self, e):
        pass
