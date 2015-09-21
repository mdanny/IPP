#Task:
Develop an oAuth service which will represent an API with requests:

The main workflow of this is that we will:

Have unprotected and protected routes
>A user will authenticate by passing in a name and a password and get back a token
>The user will store this token on their client-side and send it for every request
>We will validate this token, and if all is good, pass back information in JSON format

Our API will be built with:
>normal routes (not authenticated)
>route middleware to authenticate the token
>route to authenticate a user and password and get a token
>authenticated routes to get all users
