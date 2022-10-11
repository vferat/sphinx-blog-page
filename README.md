# sphinx-blog-page
A repository template to create a blog with Github Pages and Sphinx

https://vferat.github.io/sphinx-blog-page/


create a branch name "gt-pages"
go to respository Settings -> Pages

Source -> deploy from a branch
Branch -> gh-pages

## Sphinx

## Create a new environment
conda create -n sphinx python=3.9
conda activate sphinx

## install sphinx
pip install sphinx

## Start a new sphinx project
sphinx-quickstart

## Build Docs

make html

open build/index.html

# Configure the website

Edit conf.py

## Use markdown
install myst-parser
pip install --upgrade myst-parser

Add myst_parser to the list of configured extensions:
extensions = ['myst_parser']

adjust the source_suffix variable in conf.py
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

## Install a new theme
pip install pydata_sphinx_theme

In conf.py
html_theme = 'pydata_sphinx_theme'

## Configure pydata_sphinx_theme

html_theme_options = {
  "github_url": "https://github.com/vferat/",
  "twitter_url": "https://twitter.com/ferat_victor",
  "search_bar_text": "Search this site...",
}

html_favicon = "_static/favicon.ico"
html_title = "Pycromancer"

## Bonus: Adda custom icon link

html_theme_options = {
  "github_url": "https://github.com/vferat/",
  "twitter_url": "https://twitter.com/ferat_victor",
  "icon_links": [
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0003-1952-7657",
            "icon": "fa-brands fa-orcid",
        },],
  "search_bar_text": "Search this site...",
}

## Configure the nav bar
Create a new page 'about.md'

add a toctree to 'index.md'

```{toctree}
:maxdepth: 2
:hidden:
about.md
```

Add another page:
Create a new page 'blog.md'

```{toctree}
:maxdepth: 2
:hidden:
about.md
blog.md
```

## Create a sidebar

create sidebar.html in _templates
html_sidebars = {'**': ['sidebar.html']}

use the sidebar only for specific pages
html_sidebars = {'index': ['sidebar.html'],
                 'about': ['sidebar.html']}

### Custom the sidebar with css

#### create custom.css in _static

/* Bio area */
div.profile-pic {
    margin-top: 1em;
}

div.profile-pic img {
    border-radius: 50%;
    width: 200px;
    height: 200px;
    margin: 0 auto;
    display: block;
    filter: grayscale(80%);
}

.title {
    margin: 1em auto;
    max-width: 220px;
    text-align: center;
}

.name {
    font-size: 1.5em;
    text-align: center;
}

#### Use css in conf

html_css_files = [
    'custom.css',
]

## Add a blog

https://ablog.readthedocs.io/

create post/_year_/yy_mm_dd_title.md

pip install ablog
extensions = ['...',
             'ablog',
             '...']


### edit blog sidebar

html_sidebars = {...
                 'blog': ['tagcloud.html', 'archives.html'],}


## Edit content

### Bibliography

#### install sphinxbibtex
pip install sphinxcontrib-bibtex

#### Edit conf.py
extensions += ['sphinxcontrib.bibtex']
bibtex_bibfiles = ['bibliography.bib']

#### Create bibliography
create 'bibliography.bib'

# Publications


#### Create bibliography page
create publications.md
add it to toctree in index.md

insert biblio:


```{bibliography}
:list: bullet
:filter: author % "Ferat" or "Férat"
```

### Twitter
"sphinxcontrib.twitter"

### Panels with sphinx_design
pip install sphinx_design

extensions += ['sphinx_design']

## Edit style

https://pydata-sphinx-theme.readthedocs.io/en/v0.5.2/user_guide/customizing.html

conf.py

html_css_files = [
    'custom.css',
]

custom.css

/* Theme */
/* https://pydata-sphinx-theme.readthedocs.io/en/v0.7.2/user_guide/customizing.html */
@import "../basic.css";

html[data-theme="light"] {
    --pst-color-primary: rgb(0, 153, 255);
    --pst-color-text-base: rgb(0, 89, 100);
}

html[data-theme="dark"] {
    --pst-color-primary: rgb(68, 180, 255);
    --pst-color-text-base: rgb(7, 226, 255);
}


# Bonus

## Using giscus

create layout.html in templates


{%- extends "pydata_sphinx_theme/layout.html" %}

{% block docs_body %}
{{ super() }}
<!-- Add a comment box underneath the page's content -->
<script src="https://giscus.app/client.js"
        data-repo="choldgraf/choldgraf.github.io"
        data-repo-id="MDEwOlJlcG9zaXRvcnk1MTIzNzA1NA=="
        data-category="Blog comments"
        data-category-id="DIC_kwDOAw3Qvs4CAV4E"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-theme="light"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>
{% endblock %}
