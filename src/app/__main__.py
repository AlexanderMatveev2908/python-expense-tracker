from app.lib.core import Core
from app.lib.lib_log import LibLog
from app.paperwork.tracker_opt import TrackerOpt


def main() -> None:
    LibLog.intro()
    LibLog.options()

    main_choice: TrackerOpt = Core.main_choice()

    print(main_choice)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Core.bye()
