<h1 align="center">
<p align="center"><a href="#" target="_blank"><img src="doc/logo.svg" width="400"></a></p>
  <p align="center">
  <img src="https://img.shields.io/badge/Metronic-1.0-red">
  <img src="https://img.shields.io/badge/Aiohttp-3.8.10-green">
  <img src="https://img.shields.io/badge/jwt-1.3.1-purple">
</h1>

## About the Project

Meck and the API responsible for storing the files on the servers
It is also responsible for authenticating and validating new users.

## Expectations

Dealing with data sharing system where a user cannot see what other users store

-  Space management Each user has approximately 50GB of space within the server and this amount cannot be exceeded.

-  deal with, user management where it will not be possible to spy on what other users or who the other users are

-  cause users in collective not to reach the limit allowed on the server

## Websocket
**Host**  = "0.0.0.0"
**Port**  = 8080

websocket will be responsible for making the communications between the client and the server where the data will be stored.

- when the user logs in for the first time, the system automatically creates a location for him, where he will store his data within the system and based on this location it is possible to know how much space the user is spending

 - Inside the dictionary will have some keys where only the server can access it, preventing these data without the necessary credentials from being exposed

##Rotes
```
end Point: /api/create/
Args: eamil and name password HASH
Response: return id item removed 
```

```
end Point: /api/login/
Args: JWT Token
Response: return JWT Token 
```

```
end Point: /api/auth/
Args: Email and Password
Response: verify your JWT token
```

```
end Point: /api/upload/
Args: JWT Token
Response: return id item upload 
```

```
end Point: /api/remove/
Args: JWT Token and id item
Response: return id item removed 
```

## Token (JWT) 
token will be used as user registration within the dictionary so after login the user will receive a safe token and with the parameters inside the token and it is possible to identify the user

- will have a routine that checks the last access and after 48H it deletes the dictionary item.

- All other information is optional, and this is where the magic happens. We can inform anything in it and based on that information that authentication systems are able to identify the user. The most common is to inform the user ID.

- The purpose of JWT is to ensure that information was generated by you, even if others can read the information, it is not possible to change it.

Only those who have the keys that generated this token can validate it and even generate other valid tokens.

## Database (PostgreSQL)
we will only have a table with the following fields
ID, EMAIL, USERNAME, PASSWORD, SPACE, CREATE, ACCESS

- Access and where we check if the person is part of the select group of website administrators