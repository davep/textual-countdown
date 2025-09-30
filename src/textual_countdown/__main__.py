"""Simple demo of the library."""

##############################################################################
# Textual imports.
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Footer, Header

##############################################################################
# Library imports.
from textual_countdown import Countdown


##############################################################################
class DemoApp(App[None]):
    """A demo application for the library."""

    CSS = """
    Horizontal {
        height: auto;
        align-vertical: middle;
    }

    Countdown {
        padding: 1 0 1 0;
    }
    """

    TITLE = "textual-countdown"
    SUB_TITLE = "Demo"

    def compose(self) -> ComposeResult:
        """Compose the application."""
        yield Header()
        for n in range(10, 100, 10):
            with Horizontal():
                yield Button(f"{n} Seconds", id=f"b-{n}")
                yield Countdown(id=f"c-{n}")
        yield Footer()

    @on(Button.Pressed)
    def start(self, event: Button.Pressed) -> None:
        """Start the countdown."""
        assert event.button.id is not None
        countdown = int(event.button.id[2:])
        self.query_one(f"#c-{countdown}", Countdown).start(countdown)

    @on(Countdown.Started)
    def we_are_off(self, event: Countdown.Started) -> None:
        """Show that the countdown has started."""
        self.notify(f"Started the {event.counting} second countdown!")

    @on(Countdown.Finished)
    def we_are_done(self, event: Countdown.Finished) -> None:
        """Show that the countdown has finished."""
        self.notify(f"And we're done with the {event.counting} second countdown!")


##############################################################################
if __name__ == "__main__":
    DemoApp().run()

### __main__.py ends here
