"""Detector Implementations"""

# Imports trigger registration via decorators
from finbot.ctf.detectors.implementations.system_prompt_leak import (
    SystemPromptLeakDetector,
)

__all__ = ["SystemPromptLeakDetector"]
