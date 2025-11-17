from app.lib.core import Core
from app.lib.ctx import Ctx
from app.lib.lib_log import LibLog
from app.paperwork.tracker_opt import TrackerOpt


def main(ctx: Ctx = Ctx(), with_intro: bool = True) -> None:
    if with_intro:
        LibLog.intro()

    LibLog.options()

    main_choice: TrackerOpt = Core.main_choice()
    Core.mng_choice(ctx, main_choice)

    main(ctx, False)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Core.bye()
