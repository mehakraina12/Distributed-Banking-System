# Distributed-Banking-System

# Problem Statement: Distributed banking – Part I
Consider multiple clients and a server. Each client should have a GUI that enables 
users to invoke the four operations listed below and see the results of their execution;
* Deposit( acnt, amt , ser_number ): Increment the amount in ‘acnt’
* Withdraw( acnt, amt , ser_number ):Decremenr the amount in ‘acnt’
* Query( acnt , ser_number ): Return the balance of account number acnt.
* Transfer( src_acnt, dest_acnt, amt , ser_number ): Add money in dest_acnt and decrement in src_acnt
The GUI client should collect information from a user, format that into a message, send that message to the corresponding branch server, and then wait for a response before accepting the next inputs from the user.
The branch server stores account balances and performs operations.

# Implementation
* The coding language used to implement the code is Python
* Database used to store Client information is MongoDB Atlas Database
* Lamport algorithm is used to implement mutual exclusion in distributed banking system
* It uses Python sockets to create communication channel between Server and client
* Each client is managed by a separate thread created by the Server
  
# Server side Code and Logic
* The Server code runs the Banking server logic and interacts with the client to interpret the message and execute accordingly
* Through an infinite loop, the server continuously listens for any incoming client and then creates a separate thread for each client

# Bank Server class consists of 
* Request queue to store incoming requests with their timestamps
* Grant queue to store processed requests
* Lamport Clock
* Total clients list and current client processed by the server
  
# Implementation of Bank functions: 
* Deposit: This functions loads the data of account number entered by the 
client and add the amount specified. It then updates the balance in 
database and then notifies the user of the updated balance.
* Withdraw: This functions loads the data of account number entered by 
the client and subtracts the amount specified. However, the bank keeps 
a minimum balance of 2000 and sends a warning message if the resulted 
amount drops below it. It then updates the balance in database and then 
notifies the user of the updated balance.
* Query: Query function returns the current balance of the account 
number entered by the user.
* Transfer: Transfer function subtracts the amount from the source 
account and deposits it in the destination account as specified by the 
user. This function also make sure that the minimum balance in the 
source account remains 2000. After updating in the database, it returns 
the current balance of source and destination account numbers

# Handle Client:
* The server sends a feedback message of connection to the client
* The client initially sends a request message, upon receiving, the server 
updates its own clock and add the request to the queue.
* The server waits till the request is at the head of queue or there is no 
client using the bank server currently, after which it sends a access 
granted message to the client and removes it Request queue
* After granting access, an infinite loop handle communication till the 
client sends a release message

# Client side Code and Logic

* The Client code runs the Client logic wishing to access server and interacts 
with the Server to send the formatted message and execute accordingly
* Client class consists of 
o Account number of client which should be presented in the database
o Clock to send timestamps
o Variable to indicate state of Client, that are, Waiting and Holding
o Queue to store all sent requests
* Deposit, Withdraw, Query and Transfer functions take account number and 
amount accordingly and create a query into predefined format to send to user
* Exit option in the client menu sends the release message to server 
* Request function increments the client clock by one, sends the request and 
timestamp to the server and wait till the confirmation to proceed further
* Client object is created with the account number and runs in an infinite loop 
to communicate to the server

# Lamport Algorithm:
The Lamport algorithm is chosen in this project as it is a simple and efficient algorithm that only requires time stamping of requests. It works well when there are 
only a few processes contending for the shared resource, and the communication delay between the processes is relatively small, which is the case in our project.
Lamport algorithm does ensure that mutual exclusion is enforced in a fair and orderly manner and even though the algorithm does not explicitly prevent deadlock, it 
ensures that there is no starvation, that is, a situation in which a process is perpetually denied access to a shared resource in our distributed system implementation.


