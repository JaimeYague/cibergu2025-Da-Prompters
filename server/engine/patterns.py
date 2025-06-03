# /server/engine/patterns.py

SENSITIVE_PATTERNS = [
    (r"\b(?:\d[ -]*?){13,16}\b", "### TARJETA ###"),   # tarjeta de crédito
    (r"\b\d{8}[a-hj-np-tv-zA-HJ-NP-TV-Z]\b", "### DNI ###"),        # DNI español
    (r"\b(6\d{8}|7\d{8}|9\d{8})\b", "### TELÉFONO ###"), # teléfono ES
    (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "### EMAIL ###"), # email
    (r"SENSIBLE", "CENSURADO")
]
