# Render README.qmd to GitHub Flavored Markdown (README.md)
# This target:
# 1. Renders README.qmd to README.md using Quarto
# 2. Runs post_render.py script to remove .png extensions from shields.io URLs
#    (Quarto automatically appends .png to image URLs, which breaks shields.io badges)
render-readme:
	quarto render README.qmd --to gfm && python scripts/post_render.py