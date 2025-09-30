# Using the library

## Including the widget

`textual-countdown` provides just one widget:
[`Countdown`][textual_countdown.Countdown]; this can be composed into your
application like any other widget:

=== "Import and compose"

    ```py
    --8<-- "docs/examples/basic_example.py"
    ```

=== "The Countdown widget"

    ```{.textual path="docs/examples/basic_example.py" lines=5}
    ```

## Starting a countdown

As you can see above, the [`Countdown`][textual_countdown.Countdown] widget
doesn't do anything interesting to start with; it's just a dim line. To have
the widget start to count down and show the user that something is happening
you need to call the [`start`][textual_countdown.Countdown.start] method:

=== "Start a countdown"

    ```py
    --8<-- "docs/examples/start_example.py"
    ```

=== "The started Countdown widget"

    ```{.textual path="docs/examples/start_example.py" lines=5}
    ```

Once the countdown starts, as you can see above in the tab that shows the
result, the countdown bar will change colour to show how much time is left
to go. Over time the highlighted portion of the bar will reduce:

=== "After 1 second"

    ```{.textual path="docs/examples/start_example.py" lines=5 press="wait:1000"}
    ```

=== "After 2 second"

    ```{.textual path="docs/examples/start_example.py" lines=5 press="wait:2000"}
    ```

=== "After 3 second"

    ```{.textual path="docs/examples/start_example.py" lines=5 press="wait:4000"}
    ```

## Knowing when the countdown starts and ends

To help react to a countdown starting and ending the
[`Countdown`][textual_countdown.Countdown] widget [posts two different
messages](https://textual.textualize.io/guide/events/):
[`Started`][textual_countdown.Countdown.Started] and
[`Finished`][textual_countdown.Countdown.Finished].


=== "Reacting to countdown messages"

    ```py
    --8<-- "docs/examples/messages_example.py"
    ```

=== "After the countdown has started"

    ```{.textual path="docs/examples/messages_example.py" lines=10 press="wait:1000"}
    ```

=== "After the countdown has finished"

    ```{.textual path="docs/examples/messages_example.py" lines=10 press="wait:2500"}
    ```

## Cancelling a countdown

There are going to be times when you want to cancel a running countdown,
this can be done with the [`cancel`][textual_countdown.Countdown.cancel]
method. If called the countdown will stop, the display will revert back to
the "not running" appearance, and a
[`Cancelled`][textual_countdown.Countdown.Cancelled] message is posted.

=== "Cancelling a countdown"

    ```py
    --8<-- "docs/examples/cancel_example.py"
    ```

=== "After the countdown has been cancelled"

    ```{.textual path="docs/examples/cancel_example.py" lines=5 press="wait:3000"}
    ```

## Styling the countdown widget

The background of the widget is styled using the usual [Textual `background`
style](https://textual.textualize.io/styles/background/). Likewise, the
"non-counting" portion of the bar is controlled with the usual [Textual
`color` style](https://textual.textualize.io/styles/color/).

To style the time-remaining portion of the bar of a running countdown, use
the `countdown--remaining` component class:


=== "Styling a Countdown widget"

    ```py
    --8<-- "docs/examples/style_example.py"
    ```

=== "The styled Countdown widget"

    ```{.textual path="docs/examples/style_example.py" lines=5 press="wait:2000"}
    ```

[//]: # (using.md ends here)
