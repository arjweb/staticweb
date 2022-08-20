AUTHOR = 'Alan Jones'
SITENAME = 'Witney Water Polo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# I added this for the menu ordering & control
 
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# MENUITEMS = (
#     ('About', '/pages/about-me.html'),
#     ('Blog', '/index.html'),
#     ('Wibbly', '/pages/location.html'),
#     )

LINKS = (
    ('About', '/pages/about-me.html'),
    ('BLOG', '/index.html'),
    ('WIBBLY', '/pages/location.html'),
    )

# If I enable marble theme it will not build?
# THEME = "./pelican-themes/marble"
THEME = "./pelican-themes/alchemy"

HIDE_AUTHORS = True 
SITESUBTITLE = "Have fun, keep fit"