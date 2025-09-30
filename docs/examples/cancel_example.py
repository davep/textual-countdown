from textual import on
from textual.app import App, ComposeResult

from textual_countdown import Countdown


class CountdownApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Countdown()

    def on_mount(self) -> None:
        self.query_one(Countdown).start(3)
        self.set_timer(1, self.query_one(Countdown).cancel)

    @on(Countdown.Cancelled)
    def _react_to_cancel(self) -> None:
        self.notify("The countdown was cancelled!")


if __name__ == "__main__":
    CountdownApp().run()
