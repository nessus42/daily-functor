#!/usr/bin/env python

# -*- coding: utf-8 -*- #
DEFAULT_LANG='en'

AUTHOR = "Douglas Alan"
SITENAME = "The Daily Functor"
SITESUBTITLE = '2.0 Steps Forward, 1.0 Steps Back'
# SITEURL = 'http://nessus42.github.com/daily-functor'
SITEURL = 'http://dailyfunctor.gaffa.org'

# Comment this entry out if you don't want the GitHub banner in the top right
# corner of every page. (Note that you can also change the color of the ribbon
# by editing the github.html template. Google for "github banner" to find the other
# choices.):
GITHUB_URL = 'http://github.com/nessus42/daily-functor'

DISQUS_SITENAME = "dailyfunctor"

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 2
CLEAN_URLS = False

TIMEZONE = 'America/New_York'



# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
    ('You can modify those links in your config file', '#')
         )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('lastfm', 'http://lastfm.com/user/akounet'),
          ('github', 'http://github.com/ametaireau'),)


# For da-clean and mnmlist, the default css file is main.css. I have no idea
# how this is being set, however. Maybe it's done by Pelican, even though
# the documenation says that it defaults to "style.css".

THEME = 'da-clean'
# CSS_FILE = 'style.css'
# THEME = 'mnmlist'
# THEME = 'Just-Read'
#THEME = 'bootstrap'


# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ['images']

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
