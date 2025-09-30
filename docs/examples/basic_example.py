from textual.app import App, ComposeResult

from textual_countdown import Countdown


class CountdownApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Countdown()


if __name__ == "__main__":
    CountdownApp().run()
