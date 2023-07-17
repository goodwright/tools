""" Main nf_core module file.

Shouldn't do much, as everything is under subcommands.
"""

import importlib.metadata as importlib_metadata

__version__ = pkg_resources.get_distribution("nf_core").version + "-goodwright"
