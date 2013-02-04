Hot Places
==========

A Django project for Jon


First Time?
-----------
No virtualenv yet? get started here:
  curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

add the following line to your ~/.bashrc:
  source ${HOME}/.venvburrito/startup.sh


Setup a new VirtualEnv, add the current directory to python path and install the package requirements:
  cd hot-places
  mkvirtualenv -a . -r requirements.txt hot-places

Your virtualenv is now stored here:
  ls ~/.virtualenvs/hot-places

But the most important thing is that you can use the virtualenv as follows:
  workon hot-places

Setup project
-------------

  # Setup symlink
  cd hot-places/places/settings/
  ln -s dev.py local.py

  # setup initial database
  cd hot-places
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


