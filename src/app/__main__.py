from app.lib.core import Core


def main() -> None:
    Core.intro()
    Core.options()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Core.bye()
