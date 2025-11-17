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
    expenses: list[Expense] = [
        Expense(
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis, itaque porro, earum enim illum illo commodi dolor aut, consequatur explicabo at ex hic dolore similique repellat error. Sapiente, fugiat debitis.",
            25,
            datetime.date(2025, 1, 1),
        ),
        Expense(
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis, itaque porro, earum enim illum illo commodi dolor aut, consequatur explicabo at ex hic dolore similique repellat error. Sapiente, fugiat debitis.",
            25,
            datetime.date(2025, 1, 1),
        ),
    ]

    def is_empty(self: "Ctx") -> bool:
        return not self.expenses

    def add(self: Self, new: Expense) -> None:
        self.expenses.append(new)
