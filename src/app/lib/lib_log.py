from typing import Type

from app.lib.ctx import Expense
from app.paperwork.tracker_opt import TrackerOpt


class LibLog:
    @classmethod
    def tab(cls: Type["LibLog"]) -> None:
        print("\t")

    @classmethod
    def div(cls: Type["LibLog"], n: int) -> str:
        return "=" * n

    @classmethod
    def intro(cls: Type["LibLog"]) -> None:
        print("Welcome to the Expense Tracker CLI!")

    @classmethod
    def options(cls: Type["LibLog"]) -> None:
        cls.tab()
        title: str = f"{cls.div(3)} Expense Tracker Menu {cls.div(3)}"
        print(title)

        all_options: str = "\n".join([x.txt_of() for x in TrackerOpt])
        print(all_options)
        print(cls.div(len(title)))

    @classmethod
    def added_expense(cls: Type["LibLog"], new: Expense) -> None:
        cls.tab()
        print(
            f"Expense added successfully: {new.desc} — {new.as_dollars()} — {new.date}"
        )
