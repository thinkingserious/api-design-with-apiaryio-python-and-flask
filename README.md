This code is not production ready. It is meant to help you rapidly create an API prototype. You can find interactive APIary.io documentation [here](http://docs.todo8.apiary.io). The Blueprint used to create this documenation can be found in docs-blueprint.md. Note that you will want to look at the raw document.

There is a [companion blog post](http://sendgrid.com/blog/quickly-prototype-apis-apiary/) at SendGrid's blog that will be available Wednesday (2/19/14) evening.

## Setup

* mkdir gtd-todo-api
* cd mkdir gtd-todo-api
* virtualenv flask
* flask/bin/pip install flask
* put app.py in gtd-todo-api, make it executable and run
* Go to http://127.0.0.1:5000/folder to see a list of the default folders

### Add a new folder

curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Exercise", "description":"A collection of projects related to Exercise", "parent": 1}' http://localhost:5000/folder

### Modify a folder

curl -i -H "Content-Type: application/json" -X PATCH -d '{"description":"Test"}' http://localhost:5000/folder/1

### Delete a folder

curl -i -H "Content-Type: application/json" -X DELETE -d http://localhost:5000/folder/1

## Info & Help

If you create something cool with this code, let us know so we can include you in the [SendGrid Developer Community](http://sendgrid.com/developers/developers).

Please let me know how I can improve this tutorial with a pull request or open an issue. Thanks! 
