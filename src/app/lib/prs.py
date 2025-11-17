from typing import Type


class LibPrs:
    @classmethod
    def as_dollars(cls: Type["LibPrs"], arg: float) -> str:
        return f"${arg:.2f}"
