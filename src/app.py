"""Entry point — instancia GUI e roda mainloop."""

from src.gui import EverythingForMDApp


def main() -> None:
    app = EverythingForMDApp()
    app.mainloop()


if __name__ == "__main__":
    main()
