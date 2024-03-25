from enum import StrEnum
from typing import Optional, Union

from .common import Color
from .css import _BaseCss


class FontWeight(StrEnum):
    normal = "normal"
    bold = "bold"


class FontStyle(StrEnum):
    normal = "normal"
    italic = "italic"


class TextDecoration(StrEnum):
    none = "none"
    underline = "underline"


class TextTransform(StrEnum):
    capitalize = "capitalize"
    lowercase = "lowercase"
    uppercase = "uppercase"


class FontFamily(StrEnum):
    serif = "serif"
    sans_serif = "sans-serif"
    monospace = "monospace"


class Font(_BaseCss):
    family: Optional[Union[FontFamily, str]]
    size: Optional[int]
    transform: Optional[TextTransform]
    decoration: Optional[TextDecoration]
    style: Optional[FontStyle]
    weight: Optional[FontWeight]
    color: Optional[Color]


class Text(Font): ...
