

class NotWellFormedFormula(Exception):
    pass


class InvalidAtomicFormula(Exception):
    def __init__(self, expr: str):
        self.message = (f"Invalid atomic formula in prefix of the expression: "
                        f"{expr}")
