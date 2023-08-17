class IOException(IOError):
    def __init__(self, path: str = None, msg: str = "Файл не найден"):
        if path:
            super().__init__(f"{msg}: '{path}'")
        else:
            super().__init__(f"{msg}")