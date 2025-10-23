#!/usr/bin/env python3
"""Post-render script to fix shields.io URLs by removing .png extension."""

import re
import sys
from pathlib import Path


def remove_png_from_shields(content: str) -> tuple[str, int]:
    """
    Remove .png extension from shields.io URLs in markdown content.

    Parameters
    ----------
    content : str
        Markdown content with shields.io URLs

    Returns
    -------
    tuple[str, int]
        Cleaned content and count of replacements made
    """
    # Pattern to match shields.io URLs ending with .png
    # Matches: (https://img.shields.io/...anything except closing paren...).png
    pattern = r'(https://img\.shields\.io/[^\)]+)\.png'

    # Replace .png with empty string
    cleaned_content, count = re.subn(pattern, r'\1', content)

    return cleaned_content, count


def main() -> None:
    """Run post-render cleanup on README.md."""
    readme_path = Path("README.md")

    # Check if README.md exists
    if not readme_path.exists():
        print(f"Error: {readme_path} not found", file=sys.stderr)
        sys.exit(1)

    # Read the content
    try:
        content = readme_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {readme_path}: {e}", file=sys.stderr)
        sys.exit(1)

    # Clean the content
    cleaned_content, num_replacements = remove_png_from_shields(content)

    # Write back only if changes were made
    if num_replacements > 0:
        try:
            readme_path.write_text(cleaned_content, encoding="utf-8")
            print(f"✓ Post-render: Removed .png from {num_replacements} shields.io URL(s)")
        except Exception as e:
            print(f"Error writing {readme_path}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("✓ Post-render: No shields.io URLs needed cleaning")


if __name__ == "__main__":
    main()
