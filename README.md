# My Blog's proxy site on Heroku App

A [proxy site](http://zhengsuizhan-blogspot.herokuapp.com) of [my Google Blog](http://zhengsuizhan.blogspot.com), accessible inside the GFW.
And also my blog's descirption of this program:
[在Heroku为墙外博客搭建墙内可访的爬虫代理](http://zhengsuizhan.blogspot.com/2015/02/herokuproxy.html)

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

