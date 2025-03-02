from enum import Enum

class SectionState(Enum):
    SELECTED = 'selected'
    CROSSED = 'crossed'
    DEFAULT = 'default'

class LineState(Enum):
    CROSSED = 'crossed'
    DEFAULT = 'default'
