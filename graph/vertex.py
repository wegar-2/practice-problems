from typing import Optional

__all__ = ["Vertex"]


class Vertex:

    _COUNTER: int = 0

    def __init__(self, id_: Optional[int] = None):
        if id_:
            self._id = id_
        else:
            self._id = self._COUNTER
            self._COUNTER += 1

    @property
    def id(self) -> int:
        return self._id

    def __str__(self) -> str:
        return f"Vertex(id_={self._id})"


if __name__ == "__main__":
    v = Vertex()
    print(f"{id(v)=}") # just return the object's location in the memory
