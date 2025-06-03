import re
from .patterns import SENSITIVE_PATTERNS
from .tools import dev_count

@dev_count
def replace(message: str):
    sanitized = message
    for pattern, replacement in SENSITIVE_PATTERNS:
        sanitized = re.sub(pattern, replacement, sanitized)
    return sanitized

