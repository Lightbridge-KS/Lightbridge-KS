"""GitHub Top Languages Card URL generation."""


def gh_top_lang_card_url(
    username: str,
    exclude_repo: list[str] | None = None,
    hide: list[str] | None = None,
    langs_count: int = 5,
    layout_compact: bool = False,
    theme: str | None = None,
) -> str:
    """
    Create GitHub Top Languages Card URL.

    Parameters
    ----------
    username : str
        Your GitHub username
    exclude_repo : list[str] | None, optional
        Repository names to exclude from language statistics, by default None
    hide : list[str] | None, optional
        Language names to hide (e.g., ["html", "scss"]), by default None
    langs_count : int, optional
        Number of languages to display (must be between 1 and 10), by default 5
    layout_compact : bool, optional
        Use compact card layout, by default False
    theme : str | None, optional
        Built-in theme name, by default None

    Returns
    -------
    str
        URL of GitHub Top Languages Card

    Raises
    ------
    TypeError
        If exclude_repo or hide are not lists of strings
    ValueError
        If langs_count is not between 1 and 10

    Notes
    -----
    Based on: https://github.com/anuraghazra/github-readme-stats

    Examples
    --------
    >>> gh_top_lang_card_url("octocat")
    'https://github-readme-stats.vercel.app/api/top-langs/?username=octocat&langs_count=5'

    >>> gh_top_lang_card_url("octocat", hide=["html"], layout_compact=True, theme="algolia")
    'https://github-readme-stats.vercel.app/api/top-langs/?username=octocat&hide=html&langs_count=5&layout=compact&theme=algolia'
    """
    # Validate exclude_repo
    if exclude_repo is not None:
        if not isinstance(exclude_repo, list) or not all(
            isinstance(repo, str) for repo in exclude_repo
        ):
            raise TypeError("`exclude_repo` must be a list of repository names to exclude")

    # Validate hide
    if hide is not None:
        if not isinstance(hide, list) or not all(isinstance(lang, str) for lang in hide):
            raise TypeError("`hide` must be a list of language names to hide")

    # Validate langs_count
    if not isinstance(langs_count, int) or not (1 <= langs_count <= 10):
        raise ValueError("`langs_count` must be an integer between 1 and 10")

    # Build query parameters
    params = []

    if exclude_repo:
        exclude_str = ",".join(exclude_repo)
        params.append(f"exclude_repo={exclude_str}")

    if hide:
        hide_str = ",".join(hide)
        params.append(f"hide={hide_str}")

    params.append(f"langs_count={langs_count}")

    if layout_compact:
        params.append("layout=compact")

    if theme:
        params.append(f"theme={theme}")

    # Construct URL
    base_url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={username}"
    query_string = "&".join(params)

    return f"{base_url}&{query_string}"


def gh_top_lang_card(
    username: str,
    exclude_repo: list[str] | None = None,
    hide: list[str] | None = None,
    langs_count: int = 5,
    layout_compact: bool = False,
    theme: str | None = None,
) -> str:
    """
    Create GitHub Top Languages Card markdown link.

    Parameters
    ----------
    username : str
        Your GitHub username
    exclude_repo : list[str] | None, optional
        Repository names to exclude, by default None
    hide : list[str] | None, optional
        Language names to hide, by default None
    langs_count : int, optional
        Number of languages to display (1-10), by default 5
    layout_compact : bool, optional
        Use compact layout, by default False
    theme : str | None, optional
        Built-in theme name, by default None

    Returns
    -------
    str
        Markdown link rendering GitHub Top Languages Card

    Notes
    -----
    Based on: https://github.com/anuraghazra/github-readme-stats
    """
    url = gh_top_lang_card_url(
        username=username,
        exclude_repo=exclude_repo,
        hide=hide,
        langs_count=langs_count,
        layout_compact=layout_compact,
        theme=theme,
    )

    return f"[![Top Langs]({url})](https://github.com/{username}/{username})\n"
