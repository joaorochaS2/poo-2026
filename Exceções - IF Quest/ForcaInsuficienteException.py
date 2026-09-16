class ForcaInsuficienteException(Exception):
    def __init__(self, forca):
        super().__init__("força insuficiente: " + str(forca))
