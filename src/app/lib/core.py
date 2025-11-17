import sys
from typing import Type

from app.paperwork.tracker_opt import TrackerOpt


class Core:
    @classmethod
    def tab(cls: Type["Core"]) -> None:
        print("\t")

    @classmethod
    def div(cls: Type["Core"], n: int) -> str:
        return "=" * n

    @classmethod
    def intro(cls: Type["Core"]) -> None:
        print("Welcome to the Expense Tracker CLI!")

    @classmethod
    def bye(cls: Type["Core"]) -> None:
        cls.tab()
        print("✌🏼 bye")
        sys.exit(0)

    @classmethod
    def options(cls: Type["Core"]) -> None:
        cls.tab()
        print(f"{cls.div(3)} Expense Tracker Menu {cls.div(3)}")

        all_options: str = "\n".join([x.txt_of() for x in TrackerOpt])
        print(all_options)
