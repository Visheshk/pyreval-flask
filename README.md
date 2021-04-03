##Installation

You just need to install [flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)! If you have python 3, you just need to run `pip install flask` or use `pip3`, depending on your setup.

##Run

Following flask's [basic tutorial](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application), run 
```
export FLASK_APP=hello.py
flask run
```

##Requests

An easy tool to make different kinds of test  requests is [Postman](https://www.postman.com/downloads/). Here's what the request configuration looks like for the current flask code setup `<<inserting image here>>`. 
A simpler way to test the current setup is to use curl: 
```
curl -X POST -F "question=test question" -F "answer=ans ans" http://localhost:5000/test
```

##How it works
Currently, the server checks for POST on /test, and tries to parse it as a form data. It passes the answer field of the form data to the imported script test.py's function. testfn from test.py checks that it was given a string, then concatenates ttt at the ending and prints it to the console.

##Attaching to pyreval
My imagined expectation is that instead of import test, the server script will import pyreval, and given specific POST requests (for instance, to /getBulkScore, or to /getIndividualScore), will call specific functions in the pyreval script. The getIndividualScore corresponding function will take the answer string (and possibly even question ID or question-category-ID, if different sets of questions are measured against different pyramids), and return the corresponding score related info. This return can be any python object and doesn't need to be a string. The notebook will handle the rest~