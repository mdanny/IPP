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

Now we will login to gain our token for this user. For this in Postman we will choose POST method and in URL we will access `http://localhost:8080/api/login`. At this moment if we press send we will receive:
![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/5.png "Login user without credentials")

We got `{  "success": false,  "message": "Authentication failed. Wrong email or password or app-id."}` because we didn't input our credentials correctly, as in our case (name_surname, password, _id, email) tuple is required. We can find the credentials in our `server.js` in the `app.get(/register)` function. There we put manually our credentials which we prefer before creating the user. The _id(which corresponds to the user id) is not in the tuple because it is generated automatically when a new user registers and that's why it is required for us to save it `"user": "560124dfb6cf95320b55a0ae"`.
Now we have all the information and we can input our credentials. For this, in Postman we will choose the `Body` section, and from there we will pin the `x-www-form-urlencoded`. Afterwards, in the `Key` section we will write `name_surname` and, at its `value` our username that we can find in our `server.js` file. The same we will do with the other `Key's` as in this image below.
![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/6.png "Login user with the correct credentials")

Now after login we got our token that is valid for 24 hours as it is set up. (We can change our validation period for the token in the `server.js` file in the `// create a token` section.

You can see that in our response, we are given our token! It is recommended to save that token, because we will need it for later use in the application.
Testing Our Middleware:
We have built our middleware that our Node application will run through before it gets to the routes that we want authenticated. We did that using the help of the express library in nodejs. So we got an instance of the router for api routes. This will be useful at a later point, when, for instance there will be some functionalities that may require some permissions based on the ownership of the token (as get users, retrieve user based on token, etc.).
Let’s go into POSTman again and try to access both routes without passing a token.
This is our route without the token, i.e just accessing the base api route of `http://localhost:8080/api`:
![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/7.png "accesing api without token")
Now let’s pass in the token that was created before in our HTTP header as `x-access-token` accessing the users list at `http://localhost:8080/api/users`:
![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/8.png "accesing api with token")
We can also pass it in as a URL parameter by going to: `http://localhost:8080/api/users?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1NWZmOTgwYTA0Y2I0OTQyMDI1NzVjN2QiLCJlbWFpbCI6ImV4ZW1wbGUxLmNhcnRvZmVhbnVAZ21haWwuY29tIiwibmFtZV9zdXJuYW1lIjoiQ3Jpc3RpYW4gQ2FydG9mZWFudSIsInBhc3N3b3JkIjoicXdlcnR5IiwiYWRtaW4iOnRydWUsImxhc3RfbG9naW4iOiI4OjQyOjMyIEFNIiwidG9rZW4iOiIwIiwiX192IjowfQ.IMvPP40gm6bBwD4inzeDWCkV1pVQO_d1W-ey6NyABJI`
![alt tag](https://raw.githubusercontent.com/CristianChris/IPP/master/Laboratory_1/Images/9.png "accesing api with token from browser URL")

#####Conclusion
We have built this app using the tools specified in the Installing Tools section at the beginning part of the document. Our model data resides in the mongoDB database which interacts with the Google's POSTman application, which is an app that makes easier to simulate/inspect different requests and their responses. 

#####Future difficulties in design and implementation of this app:
* to simulate how the service registers the user to different applications and to track which app uses a specific token and to grant access to each separate app based on a particular token info
* to change the database schema, where all the info about the users is stored, because not only the info about particular users will get lost, but also the model(in our case the mongoose model). So, it won't be so easy to migrate to another database

#####Is this application useful and if not, how can I make it so?

I think this application is quite useful, because, although in a very simple manner, it demonstrates how a basic, oAUTH-like service interacts. It simulates how the genuine service behaves like, for instance it sens the client data to a secure server where their data get hashed and as a result they receive a token. Then the client sends that token to request some permissions on the server and after the validation of the identity, the client may perform some functionalities. Of course, the communication protocol used in the service is HTTP, so we have limitations in our simulation of oAUTH.


#####Technical tasks implemented 
* User data is saved in mongodb database, based on the mongoose model defined in the User.js file
* We've defined several routes, such as normal routes, which are not authenticated and the other ones specified in the API section of the document, using `apiRoutes` which is an instance of the router using the express library
* Using `'express'` and `'body-parser'` modules enables us to use body parser so we can get info from POST and/or URL parameters
*   


##Under construction
