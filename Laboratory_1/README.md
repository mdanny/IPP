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
Let’s take a look at our file structure for our Node application. This will be simplified and we’ll be putting a lot of stuff into the `server.js` file.

#####File Structure
```
- app/
----- models/
---------- user.js
- config.js
- package.json
- server.js
```

#####Installing tools
`$ npm install express body-parser morgan mongoose jsonwebtoken --save`
```
*express is the popular Node framework
*mongoose is how we interact with our MongoDB database
*morgan will log requests to the console so we can see what is happening
*body-parser will let us get parameters from our POST requests
*jsonwebtoken is how we create and verify our JSON Web Tokens
```
The `--save` modifier will also save these packages to our `package.json` file. How convenient!

#####Starting the server
`$ node server.js`

**Tip:** Use nodemon to have your server restart on file changes. Install nodemon using `npm install -g nodemon`. Then start your server with `nodemon server.js`.

We should be able to go to our browser and see the message from the route we created. Go to *http://localhost:8080* and you’ll see:

![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/1.png "First image")

As a bonus, since we used morgan, we are able to see the request logged to our console, which helps with development.

![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/2.png "Second image")

Now let’s switch over to POSTman
Now we know our application is up and running! Let’s create a sample user using the model `user.js`
Go ahead and visit your application at `http://localhost:8080/register`. You should see the message ‘User saved successfully’ logged to your console and the JSON object with `{ success: true }` in your browser.
![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/4.png "Postman create user image")
![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/3.png "Terminal Create user image")

**Don't forget to save the user ID ( example: "user": "560124dfb6cf95320b55a0ae" ), you will need it later.**

Now we will login to gain our token for this user. For this in Postman we will gona choose POST method and in URL we will access `http://localhost:8080/api/login`. At this moment if we press send we will recive:
![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/5.png "Login user without password")






##Under construction
