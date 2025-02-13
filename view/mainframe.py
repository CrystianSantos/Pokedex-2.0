from tkinter import Frame, Tk
from abc import ABC, abstractmethod

class MainFrame(ABC):
    def __init__(
        self: object,
        master: Tk,
        mainframe: Frame,
        tela: object = None,  # Se não for necessário, pode ser removido.
    ) -> None:
        self._master = master
        self._mainframe = mainframe
        self._tela = tela  # Caso não seja necessário, pode ser removido.

    def _kill_own_widgets(self: object) -> None:
        """Destroi todos os widgets filhos do mainframe."""
        for name, child in self._mainframe.children.items():
            child.destroy()

    @abstractmethod
    def _create_things(self: object, **kwargs) -> None:
        """Método abstrato que deve ser implementado nas subclasses."""
        pass

