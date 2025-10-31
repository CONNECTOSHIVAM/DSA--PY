# Inside mypackage/__init__.py

from .module1 import sums
from .module2 import mul
from .one import add

# Expose them as part of the package namespace
__all__ = ['add', 'mul', 'sums']
