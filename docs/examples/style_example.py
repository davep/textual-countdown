from textual.app import App, ComposeResult

from textual_countdown import Countdown


class CountdownApp(App[None]):
    CSS = """
    Countdown {
        background: red;
        color: blue;
        &> .countdown--remaining {
            color: yellow;
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Countdown()

    def on_mount(self) -> None:
        self.query_one(Countdown).start(3)


if __name__ == "__main__":
    CountdownApp().run()
