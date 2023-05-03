class Error:

    def __init__(self, estado) -> None:
        self.estado = estado

    @staticmethod  # Atribui um contexto único e inseparável // Usar como especificador
    def error_500():
        print('Internal Server Error')

    @staticmethod  # Atribui um contexto único e inseparável // Usar como especificador
    def error_404():
        print('Not Found')


Error.error_500()
Error.error_404()
