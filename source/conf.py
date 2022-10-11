# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-blog-page'
copyright = '2022, Victor Férat'
author = 'Victor Férat'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'ablog']
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Edit Theme -------------------------------------------------
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/vferat/",
  "twitter_url": "https://twitter.com/ferat_victor",
  "search_bar_text": "Search this site...",
}

html_favicon = "_static/favicon.ico"
html_title = "Pycromancer"

html_static_path = ['_static']

# -- Sidebar Options for HTML output -------------------------------------------------
html_sidebars = {'index': ['sidebar.html'],
                 'about': ['sidebar.html'],
                 'blog': ['tagcloud.html', 'archives.html'],}

# -- Sidebar Options for HTML output -------------------------------------------------
blog_title = html_title
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*"
post_auto_image = 1 # Index of the image that will be displayed
post_auto_excerpt = 1 # Number of paragraphs (default is ``1``) that will be displayed as an excerpt


# -- Add custom CSS -------------------------------------------------
def setup(app):
    app.add_css_file("custom.css")