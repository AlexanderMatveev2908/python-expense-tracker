import datetime
import sys
from typing import Callable, Type

from app.lib.ctx import Ctx, Expense
from app.lib.dev.error import ErrApp
from app.lib.lib_log import LibLog
from app.paperwork.reg import Reg
from app.paperwork.tracker_opt import TrackerOpt
from app.paperwork.types import T


class Core:

    @classmethod
    def bye(cls: Type["Core"]) -> None:
        LibLog.tab()
        print("Thank you for using Expense Tracker CLI! ✌🏼")
        sys.exit(0)

    @classmethod
    def __in_loop(cls: Type["Core"], cb: Callable[[], T], if_err: str) -> T:
        while True:
            try:
                res: T = cb()

                if res:
                    return res
            except Exception as err:
                msg: str

                if isinstance(err, ErrApp):
                    msg = err.msg
                else:
                    msg = if_err

                ErrApp.err_log(msg)

    @classmethod
    def __get_description(cls: Type["Core"]) -> str:
        msg_err: str = "invalid description text"

        def cb() -> str:
            desc: str = input("Enter description: ").strip()

            if not Reg.txt_ok(desc):
                raise ErrApp(msg_err)

            return desc

        return cls.__in_loop(cb, msg_err)

    @classmethod
    def __get_amount(cls: Type["Core"]) -> float:
        def cb() -> float:
            arg: str = input("Enter amount: ").strip()
            as_float: float = float(arg)

            if as_float <= 0:
                raise ErrApp("enter an amount greater than or equal to 0.01")

            return as_float

        return cls.__in_loop(cb, "invalid amount")

    @classmethod
    def __get_date(cls: Type["Core"]) -> datetime.date:
        def cb() -> datetime.date:
            arg: str = input("Enter date (YYYY-MM-DD): ").strip()
            as_date: datetime.date = datetime.datetime.strptime(arg, "%Y-%m-%d").date()

            return as_date

        return cls.__in_loop(cb, "invalid date")

    @classmethod
    def main_choice(cls: Type["Core"]) -> TrackerOpt:
        msg_err: str = "invalid choice, enter a number between 1 and 5 inclusive"

        def cb() -> TrackerOpt:
            ch: str = input("Enter your choice (1-5): ").lower().strip()
            as_int: int = int(ch)
            if 1 > as_int > 5:
                raise ErrApp(msg_err)
            parsed: TrackerOpt = TrackerOpt.from_int(as_int - 1)

            return parsed

        return cls.__in_loop(cb, msg_err)

    @classmethod
    def mng_choice(cls: Type["Core"], ctx: Ctx, opt: TrackerOpt) -> None:
        match opt:
            case TrackerOpt.ADD:
                desc: str = cls.__get_description()
                amount: float = cls.__get_amount()
                date: datetime.date = cls.__get_date()
                new: Expense = Expense(desc, amount, date)

                ctx.add(new)
                LibLog.added_expense(new)

            case TrackerOpt.EXP:
                ctx.get_expenses()
            case TrackerOpt.DEL:
                pass
            case TrackerOpt.TOT:
                pass
            case TrackerOpt.QUIT:
                cls.bye()
