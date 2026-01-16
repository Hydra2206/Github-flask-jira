Problem statement:-
QE/devs creates issues on github & some of the issues are genuine, so for the genuine issue, when devs comment /jira, it should create a jira ticket.

1) created a python script which will make a api call to jira & create a ticket
2) configure webhook for issue comments, so that when someone comment on issues a payload is sent to server where flask app is running.

Implemetation steps:
1) in this repo jira-flask-app.py is present update the api_token, email_add accordingly
2) create a ec2/azureVM & install python & flask.
3) create a file for jira-flask-app.py & run python file
3) configure webhook in the repo where issue are present
   Payload URL : http://server-public-ip:5000/CreateJIRA
   Content type : application/json
   Which events would you like to trigger this webhook? : select according on which event you want to trigger

4) Now when you comment anything expect /jira, no tickets will be created on jira portal
5) Only commenting /jira or anything contains /jira, tickets gonna create

