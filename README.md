WhereGoNow
==========

A Django project inspired by Jon Paine's idea, implemented by Chris Jesse.


Tasks
-----

- [x] Registration  -- needs testing
- [ ] Profiles
- [x] Base models added
- [x] Create basic Places with just name/lat/long
- [ ] Views for base pages
- [ ] Style for mobile
- [ ] Link to Places from Google / Foursquare / similar


Templates
- [ ] Templates for base pages (very basic)
- [ ] Main page with Table for finding hot places to go
- [ ] Vote page
- [ ] Profile page
- [ ] Heatmap page of popular places


Authentication
- [x] Django auth
- [ ] Facebook auth
- [ ] Twitter auth
- [ ] Google auth


Clone Repository
----------------
Windows: You can install "GitHub for Windows" and use the "Clone in Windows" button on github.com

* Over SSH (after having saved your SSH key in your github profile):
  git clone git@github.com:Spudwars/wheregonow.git

* Over HTTP (provide your username and password each time):
  git clone https://github.com/Spudwars/wheregonow.git


VirtualEnv
----------
No virtualenv yet? get started here:
    curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

add the following line to your ~/.bashrc:
    source ${HOME}/.venvburrito/startup.sh


Setup a new VirtualEnv, add the current directory to python path and install the package requirements:
    cd wheregonow
    mkvirtualenv -a . -r requirements.txt wheregonow

Your virtualenv is now stored here:
    ls ~/.virtualenvs/wheregonow

But the most important thing is that you can use the virtualenv as follows:
    workon wheregonow


Setup project
-------------

    workon wheregonow
    # Setup symlink
    cd wheregonow/places/settings/
    ln -s dev.py local.py

    # setup initial database
    cd wheregonow
    python manage.py syncdb
    # setup a root user/pass and remember it!
    python manage.py migrate sentry
    # Run project
    python manage.py runserver

Test it works by browsing to 127.0.0.1:8000/admin/ and log in with you root username and password you created earlier.



Thanks
------

VirtualEnvWrapper install
    https://github.com/brainsik/virtualenv-burrito

Quick start Django project
    http://senko.net/en/django-quickstart-skeleton-project/#dj-skeletor-example

HTML5 Mobile boilerplate
    https://github.com/h5bp/mobile-boilerplate


