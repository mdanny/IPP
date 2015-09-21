####Task: Develop an oAuth service which will represent an API with requests:

The main workflow of this is that we will:

Have unprotected and protected routes
```
1.A user will authenticate by passing in a name and a password and get back a token.
2.The user will store this token on their client-side and send it for every request.
3.We will validate this token, and if all is good, pass back information in JSON format.
```
Our API will be built with:
```
1.normal routes (not authenticated).
2.route middleware to authenticate the token.
3.route to authenticate a user and password and get a token.
4.authenticated routes to get all users.
```
Tools Needed
```
*node and npm
*POSTman
```
#####Getting Started
Let’s take a look at our file structure for our Node application. This will be simplified and we’ll be putting a lot of stuff into the server.js file.
