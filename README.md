# Simple Socket Server and Client in Python

## Description

This project demonstrates the implementation of a simple socket server and client in Python from scratch, without using any pre-built modules like `socket`. The main purpose of this project is to learn and understand how sockets work and how to parse HTTP requests at a basic level.

**Note:** This implementation is for educational purposes only and should not be used in a production environment.

## Motivation

The motivation behind this project is to have fun while learning about the fundamentals of network programming, specifically sockets and HTTP protocol. This exercise helps in understanding the underlying mechanics of network communication which is often abstracted away by high-level libraries and frameworks.

## How to Use

### Running the Server

1. Navigate to the project directory.
2. Run the server script:

```sh

python server.py
```

The server will start and listen for incoming connections.

### Running the Client

1. Open another terminal window.
2. Navigate to the project directory.
3. Run the client script with a name argument:
```sh

python client.py name
```

The client will send the name to the server, and the server will respond with a greeting.
