"""
Unicode to Plain Text Mapping Engine
Provides bidirectional exact conversion for:
- Bold
- Italic
- Script
- Fraktur
- Monospace
- Double-struck

These map specifically to Mathematical Alphanumeric Symbols and other
Unicode styled character variants commonly used in Social Media.
"""

# Plain characters
PLAIN_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PLAIN_LOWER = "abcdefghijklmnopqrstuvwxyz"
PLAIN_DIGITS = "0123456789"

# Unicode variants
STYLES = {
    "bold": {
        "upper": "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙",
        "lower": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
        "digits": "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
    },
    "italic": {
        "upper": "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍",
        "lower": "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧",
        "digits": "" # typically no italic digits in Mathematical Alphanumeric
    },
    "script": {
        "upper": "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
        "lower": "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏",
        "digits": ""
    },
    "fraktur": {
        "upper": "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "lower": "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷",
        "digits": ""
    },
    "monospace": {
        "upper": "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
        "lower": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
        "digits": "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
    },
    "double_struck": {
        "upper": "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "lower": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
        "digits": "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
    }
}

# Precompute translation dictionaries
_to_plain = {}
_to_style = {style: {} for style in STYLES}

for style, mappings in STYLES.items():
    if "upper" in mappings and mappings["upper"]:
        for p, u in zip(PLAIN_UPPER, mappings["upper"]):
            _to_plain[u] = p
            _to_style[style][p] = u
    if "lower" in mappings and mappings["lower"]:
        for p, u in zip(PLAIN_LOWER, mappings["lower"]):
            _to_plain[u] = p
            _to_style[style][p] = u
    if "digits" in mappings and mappings["digits"]:
        for p, u in zip(PLAIN_DIGITS, mappings["digits"]):
            _to_plain[u] = p
            _to_style[style][p] = u

def convert_to_plain(text: str) -> str:
    """Converts any supported styled unicode text to plain text."""
    return "".join(_to_plain.get(char, char) for char in text)

def convert_to_style(text: str, style: str) -> str:
    """
    Converts plain text to a specific unicode style.
    Supported styles: bold, italic, script, fraktur, monospace, double_struck
    """
    if style not in _to_style:
        raise ValueError(f"Style '{style}' not supported.")
    
    mapping = _to_style[style]
    return "".join(mapping.get(char, char) for char in text)

def get_available_styles() -> list:
    """Returns a list of supported styles."""
    return list(STYLES.keys())

def detect_styles(text: str) -> set:
    """Detects which styles are present in the text."""
    detected = set()
    for char in text:
        if char in _to_plain:
            # Reverse lookup the style
            for style, mappings in _to_style.items():
                if char in mappings.values():
                    detected.add(style)
                    break
    return detected
