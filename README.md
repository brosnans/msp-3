# Milestone Project - Incident Manager

*Developer: brosnans*

App available at https://incident-manager-flask-mongo.herokuapp.com/

 - Project Brief
 - Technologies
 - Workspace
 - Workflow
 - UXD
 - Wireframes
 - Testing
 - Heroku Deployment
 - How to Deploy Locally
 
## 1. Project Brief

In this project, you'll build a full-stack site that allows your users to manage a common dataset about a particular domain.

**CREATE AN APPLICATION WHICH CAN BE USED FOR THE REPORTING AND RECORDING OF WORKPLACE ACCIDENTS AND INCIDENTS**

Build a web application that allows users to record information about workplace accidents and incidents.

- The user is presented with a form to enter details about the accident or incident.
- Users enter accident/ incident details into a text area and submit their report using a form.
- Multiple players can play an instance of the game at the same time. Users are identified by a unique username.

## 2. Technologies

Backend

 - Python3
 - Flask

Frontend

 - HTML5
 - CSS3
 - Materialize v1.0.0
 - jQuery v3.3.1

Version Control

 - Git
 - Github

Database Management

 - MongoDB

## 3. Workspace

**Operating System** - [Windows 10](https://en.wikipedia.org/wiki/Windows_10)

**Editor** - [Visual Studio Code](https://gitpod.io)

**Language** - [Python3](https://www.python.org)

**Microframework** - [Flask](http://flask.pocoo.org)

**Testing**	- [Unittest](https://docs.python.org/3/library/unittest.html)

## 4. Workflow

-   Create project directory with readme
-   Create git repo
-   Work on UXD up to Skeleton plane
-   Create wireframes
-   Setup Gitpod for Python
-   Install pip3
-   Install flask
-   Create requirements.txt
-   Create app.py
-   Get Flask app up and running
-   Make it look nice - complete Surface plane of UXD
-   Deploy app to Heroku

## 5. UXD

#### Strategy

| Focus                                                       | User Needs                                                            | Business Objectives                             |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| _What are you aiming to achieve?_                           | Report accidents/ incidents                                           | Report accidents/ incidents                     |
|                                                             | Keep records of reports on database                                   | Keep records of accident/ incident reports      |
| _For whom?_                                                 | Categorise accidents/ incidents                                       |                                                 |
| _TARGET AUDIENCE:_                                          | Add due dates for accident/ incident investigations                   |                                                 |
| People who need to record workplace accidents/ incidents    |                                                                       |                                                 |
|                                                             |                                                                       |                                                 |

#### Scope

| Focus                                                       | Functional Specification                                              | Content Requirements                            |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| Which features?                                             | Choose accident type/ category from a list                            | Select category dropdown and button             |
| What’s on the table?                                        | Display accident/ incident records                                    | Report text                                     |
|                                                             | Enter an accident                                                     | Accident details input                          |
|                                                             | Return incorrect answer                                               | Submit report button                            |
|                                                             | Store accident/ incident report details                               |                                                 |
|                                                             | Show list of accident/ incident reports                               |                                                 |
|                                                             |                                                                       |                                                 |
|                                                             |                                                                       |                                                 |

#### Structure

| Focus                                                       | Interaction Design                                                           | Information Architecture                                                                |
|-------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| _How is the information structured?_                        | _Where am I? / How did I get here? / What can I do here? / Where can I go?_  | _Organizational / Navigational schemas (tree / nested list / hub and spoke / dashboard)_|
|                                                             | Incident Log > View incident details                                         | Tree structure                                                                          |
| _How is it logically grouped?_                              | Add New Incident > REport Details of Incident                                |                                                                                         |
|                                                             | Manage Categories > Add Incident Categories                                  |                                                                                         |
|                                                             | Mark Incident Closed > End                                                   |                                                                                         |
|                                                             |                                                                              |                                                                                         |

#### Skeleton

| Focus                                                         | Interface Design         | Navigational Design  | Information Design  |
|---------------------------------------------------------------|--------------------------|----------------------|---------------------|
| _How will the information be represented?_                    | See wireframes           |                      |                     |
| _How will the user navigate to the information and features?_ |                          |                      |                     |
|                                                               |                          |                      |                     |

#### Surface

| Focus                                                       | Visual Design                       |
|-------------------------------------------------------------|-------------------------------------|
| What will the finished product look like?                   |                                     |
| What colours, typography and design elements will be used?  |                                     |
|                                                             |                                     |

### 6 Wireframes

![Wireframes]()

### 7 Testing

I used the **Test Before** approach to Test Driven Development, using Python's **unittest** class.

I created a file called test_incident_manager.py and wrote the first test (below) which failed.  Then I wrote a function in run.py to make the test pass.  I continued in this way until I had all of the functionality required to build the game.

---

---

[**HTML Validator Results**](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhobbit-riddle-game.herokuapp.com%2F)

[**CSS Validator Results**](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fhobbit-riddle-game.herokuapp.com&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

### 8 Heroku Deployment

1. Create a new app 'incident-manager-flask-mongo' on heroku.com

2. Install [Heroku CLI](https://devcenter.heroku.com/categories/command-line)
    - $ brew install heroku/brew/heroku

3. Login to heroku with email abd password
    - $ heroku login

4. Check app is there
    - $ heroku apps

5. Add heroku remote
    - $ heroku git:remote -a incident-manager-flask-mongo

6. Add Procfile (this tells heroku what to do with the project)
    - $ echo web: python app.py > Procfile

7. Git commit and push to heroku remote
    - $ git add Procfile
    - $ git ci -m 'Add Profile for heroku deployment'
    - $ git push -u heroku master

8. Set up dynos
    - $ heroku ps:scale web=1

9. Setup config variables on heroku dashboard

    ![Config Variables](https://raw.githubusercontent.com/sarahloh/p3-riddle-game/master/static/images/readme/config-vars.png)

10. Restart dynos

    ![Restart Dynos](https://raw.githubusercontent.com/sarahloh/p3-riddle-game/master/static/images/readme/restart-dynos.png)

### 9 How To Deploy Locally

```console
$ git clone git@github.com/brosnans/msp-3
$ cd msp-3
$ pip3 install -r requirements.txt
$ python3 app.py
```