class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__state = estado

    def get_state(self) -> bool:
        return self.__state

    def set_state(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__state = value
