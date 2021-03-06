from lista_duplamente_ligada import Lista_duplamente_ligada


class Fila():
    def __init__(self) -> None:
        self.fila = Lista_duplamente_ligada()

    def entrar(self, conteudo):
        self.fila.inserir_no_fim(conteudo)

    def sair(self):
        return self.fila.remover_do_inicio()

    @property
    def vazia(self):
        return self.fila.quantidade == 0
