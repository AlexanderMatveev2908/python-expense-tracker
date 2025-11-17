from dataclasses import dataclass
import datetime
from typing import Self

from app.paperwork.types import Nullable


@dataclass
class Expense:
    desc: str
    amount: float
    date: datetime.date


class Ctx:
    expenses: list[Expense] = []

    def is_empty(self: "Ctx") -> bool:
        return not self.expenses

    def add(self: Self, new: Expense) -> None:
        self.expenses.append(new)

    def delByIdx(self: Self, target: int) -> Nullable[Expense]:
        for idx, x in enumerate(self.expenses):
            if idx == target:
                self.expenses.remove(x)
                return x
        return None

    def delByDesc(self, target: str) -> Nullable[Expense]:
        for x in self.expenses:
            if x.desc == target:
                self.expenses.remove(x)
                return x
        return None

    def acc_total(self: Self) -> float:
        acc: float = 0

        for x in self.expenses:
            acc += x.amount

        return acc
