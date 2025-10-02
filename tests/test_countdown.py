"""Tests for the Countdown widget."""

##############################################################################
# Textual imports.
from textual import on
from textual.app import App, ComposeResult

##############################################################################
# Local imports.
from textual_countdown import Countdown


##############################################################################
class CountdownApp(App[None]):
    def __init__(self):
        self.captured_messages: list[Countdown.CountdownMessage] = []
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Countdown()

    @on(Countdown.CountdownMessage)
    def _record_countdown_message(self, message: Countdown.CountdownMessage) -> None:
        self.captured_messages.append(message)


##############################################################################
async def test_not_running_to_start_with() -> None:
    """The Countdown should not be running on application startup."""

    async with CountdownApp().run_test() as pilot:
        assert pilot.app.query_one(Countdown).is_running is False


##############################################################################
async def test_is_running_after_start() -> None:
    """The Countdown should be running after we start it."""

    async with CountdownApp().run_test() as pilot:
        pilot.app.query_one(Countdown).start(1)
        assert pilot.app.query_one(Countdown).is_running is True


##############################################################################
async def test_is_not_running_after_cancel() -> None:
    """The Countdown should not be running after we cancel it."""

    async with CountdownApp().run_test() as pilot:
        pilot.app.query_one(Countdown).start(1)
        assert pilot.app.query_one(Countdown).is_running is True
        pilot.app.query_one(Countdown).cancel()
        assert pilot.app.query_one(Countdown).is_running is False


##############################################################################
async def test_started_message() -> None:
    """When we start a countdown we should get a message."""

    async with CountdownApp().run_test() as pilot:
        pilot.app.query_one(Countdown).start(1)
        await pilot.pause(0.1)
        assert isinstance(pilot.app, CountdownApp)
        assert len(pilot.app.captured_messages) == 1
        assert isinstance(pilot.app.captured_messages[0], Countdown.Started)


##############################################################################
async def test_finished_message() -> None:
    """When countdown ends we should get a message."""

    async with CountdownApp().run_test() as pilot:
        pilot.app.query_one(Countdown).start(0.2)
        await pilot.pause(0.5)
        assert isinstance(pilot.app, CountdownApp)
        assert len(pilot.app.captured_messages) == 2
        assert isinstance(pilot.app.captured_messages[-1], Countdown.Finished)


##############################################################################
async def test_cancelled_message() -> None:
    """When countdown is stopped we should get a cancel message."""

    async with CountdownApp().run_test() as pilot:
        pilot.app.query_one(Countdown).start(10)
        await pilot.pause(0.1)
        pilot.app.query_one(Countdown).cancel()
        await pilot.pause(0.1)
        assert isinstance(pilot.app, CountdownApp)
        assert len(pilot.app.captured_messages) == 2
        assert isinstance(pilot.app.captured_messages[-1], Countdown.Cancelled)


##############################################################################
async def test_control_property() -> None:
    """The control property of the messages should be the countdown object."""

    async with CountdownApp().run_test() as pilot:
        pilot.app.query_one(Countdown).start(1)
        await pilot.pause(1.1)
        assert isinstance(pilot.app, CountdownApp)
        for message in pilot.app.captured_messages:
            assert isinstance(message, Countdown.CountdownMessage)
            assert message.countdown == message.control


### test_countdown.py ends here
