"""Create shields.io badge URLs for GitHub profile README."""


def shield_url(name: str, color: str | None = None) -> str:
    """
    Create shields.io logo badge URL.

    Parameters
    ----------
    name : str
        Logo name (e.g., "R", "Python", "GitHub")
    color : str | None, optional
        HEX color code for the logo (without '#'), by default None

    Returns
    -------
    str
        Full URL to shields.io badge

    Examples
    --------
    >>> shield_url("Python")
    'https://img.shields.io/badge/-Python-05122A?style=flat&logo=python'

    >>> shield_url("Python", color="3776AB")
    'https://img.shields.io/badge/-Python-05122A?style=flat&logo=python&logoColor=3776AB'
    """
    base_url = "https://img.shields.io/badge/"
    logo_color = f"&logoColor={color}" if color else ""
    slug_url = f"-{name}-05122A?style=flat&logo={name.lower()}{logo_color}"

    return base_url + slug_url
