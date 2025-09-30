from textual import on
from textual.app import App, ComposeResult

from textual_countdown import Countdown


class CountdownApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Countdown()

    def on_mount(self) -> None:
        self.query_one(Countdown).start(2)

    @on(Countdown.Started)
    def _react_to_start(self) -> None:
        self.notify("The countdown has begun!")

    @on(Countdown.Finished)
    def _react_to_finish(self) -> None:
        self.notify("The countdown has ended!")


if __name__ == "__main__":
    CountdownApp().run()
