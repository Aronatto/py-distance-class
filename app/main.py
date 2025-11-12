from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        if not isinstance(km, (int, float)):
            raise TypeError("Distance must be a number.")
        if km < 0:
            raise ValueError("Distance cannot be negative.")
        self.km = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km:.2f} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # Dodawanie
    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other: Union[int, float]) -> "Distance":
        return self.__add__(other)

    # +=
    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    # Mnożenie
    def __mul__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: Union[int, float]) -> "Distance":
        return self.__mul__(other)

    # Dzielenie
    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Distance(self.km / other)
        return NotImplemented

    # Porównania
    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
