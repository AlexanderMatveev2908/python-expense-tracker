import datetime
from typing import Type

from app.lib.ctx import Ctx, Expense
from app.paperwork.tracker_opt import TrackerOpt
from app.paperwork.types import Nullable


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

    @classmethod
    def desc_in_col(cls: Type["LibLog"], txt: str, width: int = 35) -> str:
        words: list[str] = txt.split()
        lines: list[str] = []
        curr: str = ""

        for w in words:
            if len(curr) + len(w) + 1 > width:
                lines.append(curr)
                curr = w
            else:
                curr = w if curr == "" else curr + " " + w

        if curr:
            lines.append(curr)

        return "\n".join(lines)

    @classmethod
    def __or_empty_str(cls: Type["LibLog"], arg: Nullable[str]) -> str:
        return arg or ""

    @classmethod
    def print_row(
        cls: Type["LibLog"],
        header: bool = False,
        *,
        idx: str,
        desc: str,
        amount: str,
        date: str,
    ) -> None:
        IDX_SPACE: int = 10
        DESC_SPACE: int = 35
        AMOUNT_SPACE: int = 15
        DATE_SPACE: int = 15

        B = " | "

        print(
            f"{cls.__or_empty_str(idx):^{IDX_SPACE}}{B}"
            f"{cls.__or_empty_str(desc):^{DESC_SPACE}}{B}"
            f"{cls.__or_empty_str(amount):^{AMOUNT_SPACE}}{B}"
            f"{cls.__or_empty_str(date):^{DATE_SPACE}}{B}"
        )

    @classmethod
    def pretty_expenses(cls: Type["LibLog"], ctx: Ctx) -> None:
        cls.tab()

        if ctx.is_empty():
            print("No expenses recorded yet.")
            return

        # ? 75 chars + 3 offset of bar on each col = 75 + 3 * 4
        DIVS_SPACE: int = 87

        print(cls.div(DIVS_SPACE))
        cls.print_row(
            header=True,
            idx="Index",
            desc="Description",
            amount="Amount",
            date="Date",
        )
        print(cls.div(DIVS_SPACE))

        for idx, exp in enumerate(ctx.expenses):
            wrapped: list[str] = cls.desc_in_col(exp.desc).split("\n")

            cls.print_row(
                idx=str(idx),
                desc=wrapped[0],
                amount=exp.as_dollars(),
                date=str(exp.date),
            )

            for line in wrapped[1:]:
                cls.print_row(idx="", desc=line, amount="", date="")

            print("-" * DIVS_SPACE)
