"""Create shields.io badge URLs for GitHub profile README."""


def shield_url(
    name_logo: str, name_disp: str | None = None, color: str | None = None
) -> str:
    """
    Create shields.io logo badge URL.
    """
    base_url = "https://img.shields.io/badge/"

    name_disp_url = f"-{name_disp}" if name_disp else ""

    # Remove leading '#' from hex color if present
    if color:
        color_cleaned = color.removeprefix("#")
        logo_color = f"&logoColor={color_cleaned}"
    else:
        logo_color = ""

    slug_url = f"{name_disp_url}-05122A?style=flat&logo={name_logo.lower()}{logo_color}"

    return base_url + slug_url
