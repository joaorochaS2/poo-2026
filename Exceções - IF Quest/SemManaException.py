class SemManaException(Exception):
    def __init__(self, mana):
        super().__init__("mana insuficiente: " + str(mana))
