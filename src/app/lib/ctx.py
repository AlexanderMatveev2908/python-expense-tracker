from dataclasses import dataclass
import datetime
from typing import Self


@dataclass
class Expense:
    desc: str
    amount: float
    date: datetime.date

    def as_dollars(self: Self) -> str:
        return f"${self.amount:.2f}"


class Ctx:
    expenses: list[Expense] = []

    def is_empty(self: "Ctx") -> bool:
        return not self.expenses

    def get_expenses(self: Self) -> None:
        if self.is_empty():
            print("No expenses recorded yet.")
            return

    def add(self: Self, new: Expense) -> None:
        self.expenses.append(new)
