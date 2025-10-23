"""GitHub Stats Card URL generation."""


def gh_stats_card_url(
    username: str,
    hide: list[str] | None = None,
    count_private: bool = False,
    show_icons: bool = False,
    theme: str | None = None,
) -> str:
    """
    Create GitHub Stats Card URL.

    Parameters
    ----------
    username : str
        Your GitHub username
    hide : list[str] | None, optional
        Stats to hide. Options: "stars", "commits", "prs", "issues", "contribs"
        by default None
    count_private : bool, optional
        Add count of all private contributions to total commits count,
        by default False
    show_icons : bool, optional
        Enable icons on the card, by default False
    theme : str | None, optional
        Built-in theme name (e.g., "dark", "radical", "merko", "gruvbox",
        "tokyonight", "onedark", "cobalt", "synthwave", "highcontrast", "dracula"),
        by default None

    Returns
    -------
    str
        URL of GitHub Stats Card

    Notes
    -----
    Based on: https://github.com/anuraghazra/github-readme-stats

    Examples
    --------
    >>> gh_stats_card_url("octocat")
    'https://github-readme-stats.vercel.app/api?username=octocat'

    >>> gh_stats_card_url("octocat", count_private=True, show_icons=True, theme="radical")
    'https://github-readme-stats.vercel.app/api?username=octocat&count_private=true&show_icons=true&theme=radical'
    """
    # Validate hide options
    if hide is not None:
        valid_hide_options = {"stars", "commits", "prs", "issues", "contribs"}
        invalid_options = set(hide) - valid_hide_options
        if invalid_options:
            raise ValueError(
                f"Invalid hide options: {invalid_options}. "
                f"Valid options are: {valid_hide_options}"
            )

    # Build query parameters
    params = []

    if hide:
        hide_str = ",".join(hide)
        params.append(f"hide={hide_str}")

    if count_private:
        params.append("count_private=true")

    if show_icons:
        params.append("show_icons=true")

    if theme:
        params.append(f"theme={theme}")

    # Construct URL
    base_url = f"https://github-readme-stats.vercel.app/api?username={username}"
    if params:
        query_string = "&".join(params)
        return f"{base_url}&{query_string}"

    return base_url


def gh_stats_card(
    username: str,
    hide: list[str] | None = None,
    count_private: bool = False,
    show_icons: bool = False,
    theme: str | None = None,
) -> str:
    """
    Create GitHub Stats Card markdown link.

    Parameters
    ----------
    username : str
        Your GitHub username
    hide : list[str] | None, optional
        Stats to hide, by default None
    count_private : bool, optional
        Add count of private contributions, by default False
    show_icons : bool, optional
        Enable icons on the card, by default False
    theme : str | None, optional
        Built-in theme name, by default None

    Returns
    -------
    str
        Markdown link rendering GitHub Stats Card

    Notes
    -----
    Based on: https://github.com/anuraghazra/github-readme-stats
    """
    url = gh_stats_card_url(
        username=username,
        hide=hide,
        count_private=count_private,
        show_icons=show_icons,
        theme=theme,
    )

    return f"[![{username} GitHub stats]({url})](https://github.com/{username}/{username})"
