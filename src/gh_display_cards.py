"""Display GitHub cards side by side using HTML."""

from dominate import tags


def gh_display_cards(
    username: str, src_lt: str, src_rt: str, height: str = "160em"
) -> str:
    """
    Display GitHub cards side by side.

    Parameters
    ----------
    username : str
        Your GitHub username
    src_lt : str
        URL of the left GitHub card
    src_rt : str
        URL of the right GitHub card
    height : str, optional
        Height of the cards (CSS units), by default "160em"

    Returns
    -------
    str
        HTML string with two cards displayed side by side

    Examples
    --------
    >>> stats_url = "https://github-readme-stats.vercel.app/api?username=octocat"
    >>> langs_url = "https://github-readme-stats.vercel.app/api/top-langs/?username=octocat"
    >>> html = gh_display_cards("octocat", stats_url, langs_url)
    >>> print(html)
    <p align="center">
      <a href="https://github.com/octocat">
        <img height="160em" src="...">
        <img height="160em" src="...">
      </a>
    </p>
    """
    with tags.p(align="center") as container:
        with tags.a(href=f"https://github.com/{username}"):
            tags.img(height=height, src=src_lt)
            tags.img(height=height, src=src_rt)

    return str(container)
