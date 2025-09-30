"""Provides a visual countdown widget."""

##############################################################################
# Backward compatibility.
from __future__ import annotations

##############################################################################
# Python imports.
from dataclasses import dataclass
from functools import partial
from time import monotonic

##############################################################################
# Textual imports.
from textual.app import RenderResult
from textual.geometry import Size
from textual.message import Message
from textual.renderables.bar import Bar
from textual.widget import Widget


##############################################################################
class Countdown(Widget):
    """A countdown widget."""

    DEFAULT_CSS = """
    Countdown {
        width: 1fr;
        height: auto;
        color: $panel;

        &> .countdown--remaining {
            color: $accent;
        }
    }
    """

    COMPONENT_CLASSES = {"countdown--remaining"}
    """
    | Class | Description |
    | :- | :- |
    | `countdown--remaining` | Targets the remaining portion of the countdown display. |
    """

    @dataclass
    class CountdownMessage(Message):
        """Base class for the [`Countdown`][textual_countdown.Countdown] message classes."""

        countdown: Countdown
        """The [`Countdown`][textual_countdown.Countdown] widget that sent the message."""

        @property
        def control(self) -> Countdown:
            """An alias for [`countdown`][textual_countdown.Countdown.CountdownMessage.countdown]."""
            return self.countdown

    class Cancelled(CountdownMessage):
        """Message sent if the countdown is cancelled."""

    @dataclass
    class Timed(CountdownMessage):
        """Base class for messages that include a time value."""

        counting: float
        """The amount being counted."""

    class Started(Timed):
        """Message sent when the countdown starts."""

    class Finished(Timed):
        """Message sent when the countdown finishes."""

    def __init__(
        self,
        name: str | None = None,
        id: str | None = None,  # pylint:disable=redefined-builtin
        classes: str | None = None,
        disabled: bool = False,
    ) -> None:
        """Initialise the [`Countdown`][textual_countdown.Countdown] widget.

        Args:
            name: The name of the countdown widget.
            id: The ID of the countdown widget in the DOM.
            classes: The CSS classes of the countdown widget.
            disabled: Whether the countdown widget is disabled or not.
        """
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._timer = self.set_interval(0.2, self._tick, pause=True)
        """The timer that is used to invoke the ticks when counting down."""
        self._started: float = 0
        """When the countdown was started."""
        self._countdown: float | None = None
        """How long the current countdown is for."""

    def get_content_height(self, container: Size, viewport: Size, width: int) -> int:
        del container, viewport, width
        return 1

    def start(self, countdown: float) -> None:
        """Start a countdown.

        Args:
            countdown: The amount of time to count down.

        Note:
            When the countdown starts a
            [`Started`][textual_countdown.Countdown.Started] message is
            posted.
        """
        self._countdown = abs(countdown)
        self._started = monotonic()
        self._timer.resume()
        self.post_message(self.Started(self, self._countdown))
        self.set_class(True, "countdown--running")

    def _stop(self) -> None:
        """Stop the countdown."""
        self.set_class(False, "countdown--running")
        self._countdown = None
        self._timer.pause()

    def cancel(self) -> None:
        """Cancel the countdown timer from running.

        Note:
            When the countdown is cancelled a
            [`Cancelled`][textual_countdown.Countdown.Cancelled] message is
            posted.
        """
        self.post_message(self.Cancelled(self))
        self._stop()
        self.refresh()

    @property
    def is_running(self) -> bool:
        """Is the countdown currently running?"""
        return self._countdown is not None

    def _tick(self) -> None:
        """Handle a tick of the countdown."""
        if self._countdown is not None:
            if monotonic() >= (self._started + self._countdown):
                self.post_message(self.Finished(self, self._countdown))
                self._stop()
            self.refresh()

    def render(self) -> RenderResult:
        width = self.size.width
        beam = partial(
            Bar, background_style=self.styles.color.rich_color.name, width=width
        )
        if self._countdown is None:
            return beam()
        half = width / 2.0
        highlight = (half / self._countdown) * abs(
            (self._started + self._countdown) - monotonic()
        )
        return beam(
            highlight_range=(half - highlight, half + highlight),
            highlight_style=self.get_component_rich_style(*self.COMPONENT_CLASSES),
        )


### countdown.py ends here
