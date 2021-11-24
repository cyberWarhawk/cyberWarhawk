Solutions to the Sainya Ranakshetram CTF Competition

The Tickle Pickle challenge is prone to Insecure Object Deserialization and the same is exploited by passing an os.system command to the vulnerable server.
The above method was simulated to replicate the attack on server.py file. 

When the server.py file tried to fetch the users.json file . It executes the os.system command passed without proper validation and filtering in turn exposing sensitive data. 

Solution is to encode the information passed to the users.json file and again decode the encrypted text and then pass it to Pickle for deserialization. 


![TicklePickle](https://user-images.githubusercontent.com/37340966/143296631-b7f73af9-6bba-452c-8279-b73bedd536d4.png)
