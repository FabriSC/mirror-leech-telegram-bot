heroku create $1
heroku git:remote -a $1
heroku stack:set container -a $1
heroku addons:create heroku-postgresql
git add .
git commit -m "first build"
git push heroku master --force
