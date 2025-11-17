import sys
from typing import Type

from app.lib.dev.error import ErrApp
from app.lib.lib_log import LibLog
from app.paperwork.tracker_opt import TrackerOpt


class Core:

    @classmethod
    def bye(cls: Type["Core"]) -> None:
        LibLog.tab()
        print("✌🏼 bye")
        sys.exit(0)

    @classmethod
    def main_choice(cls: Type["Core"]) -> TrackerOpt:
        while True:
            try:
                ch: str = input("Enter your choice (1-5): ").lower().strip()
                as_int: int = int(ch)
                if 1 > as_int > 5:
                    raise ErrApp("_")
                parsed: TrackerOpt = TrackerOpt.from_int(as_int - 1)

                return parsed
            except Exception:
                ErrApp.err_log("invalid choice")
