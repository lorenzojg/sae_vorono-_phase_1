class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self._x = x
        self._y = y
    
    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y
    
