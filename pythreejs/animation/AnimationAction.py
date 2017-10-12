from ipywidgets import register, DOMWidget, Widget
from traitlets import Unicode, Union, CInt, CFloat

from .._package import npm_pkg_name
from .._version import EXTENSION_VERSION

from .._base.Three import ThreeWidget
from .AnimationAction_autogen import AnimationAction as AnimationActionBase


@register
class AnimationAction(AnimationActionBase, DOMWidget):
    """AnimationAction is a three widget that also has its own view.

    The view offers animation action controls.
    """
    _view_name = Unicode('AnimationActionView').tag(sync=True)
    _view_module = Unicode(npm_pkg_name).tag(sync=True)
    _view_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)

    # Normally an int, but can also be inf:
    repititions = Union([CInt(), CFloat()], default_value=float('inf'), allow_none=False).tag(sync=True)

    # Override default super MRO resolution (this is a mixin):
    def _ipython_display_(self, **kwargs):
        return Widget._ipython_display_(self, **kwargs)