from enum import Enum
from typing import Self, Type

from app.lib.dev.error import ErrApp


class TrackerOpt(Enum):
    ADD = "ADD"
    EXP = "EXP"
    DEL = "DEL"
    TOT = "TOT"
    QUIT = "QUIT"

    @classmethod
    def from_int(cls: Type["TrackerOpt"], ch: int) -> "TrackerOpt":
        for idx, opt in enumerate(cls):
            if idx == ch:
                return opt
        raise ErrApp("invalid user choice")

    def txt_of(self) -> str:
        match self:
            case TrackerOpt.ADD:
                return "1. Add Expense"
            case TrackerOpt.EXP:
                return "2. View expenses"
            case TrackerOpt.DEL:
                return "3. Delete expense"
            case TrackerOpt.TOT:
                return "4. Show total"
            case TrackerOpt.QUIT:
                return "5. Exit"
            case _:
                raise ErrApp("invalid match")
