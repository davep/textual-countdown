"""Provides a countdown widget."""

##############################################################################
# Python imports.
from importlib.metadata import version

######################################################################
# Main library information.
__author__ = "Dave Pearson"
__copyright__ = "Copyright 2024, Dave Pearson"
__credits__ = ["Dave Pearson"]
__maintainer__ = "Dave Pearson"
__email__ = "davep@davep.org"
__version__ = version("textual_countdown")
__licence__ = "MIT"

##############################################################################
# Local imports.
from .countdown import Countdown

##############################################################################
# Exports.
__all__ = ["Countdown"]

### __init__.py ends here
