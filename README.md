# CS361-Assignment-8


COMMUNICATION CONTRACT

We will communicate using Discord, and the expectation for responsiveness will be about 18 hours, we will make sure to finish the work at least 2 days before the deadline, the privacy of each one must be respected, the space must be given to each other for their suggestions, we will learn from each other instead of copying, and set a clear purpose, objective, and scope for our projects. 



RABBITMQ Microservice Implementation
--INSTALLATION--

Download and Install ErLang
Download and Install RabbitMq

--PYTHON LIBRARIES--

pip install requests
pip install pika
pip install mqRabbit

-- How to SEND DATA --

i) Sender.py
	In this file, we created a connection on LOCALHOST of MQRABBIT.
	It will maintain a queue containing our data, This data can either
	be a simple ARRAY or it can be an API CALL or from the DB.

(In our case, its a JSON object that has been sent to the Queue of MqRabbit's Local Server and this queue will retain even if the program closes)


ii) Receiver.py
	This program will open a connection and look for the queue that has been sent by us. It will wait for the server to respond back to the synchronus call.
Once the queue is matched, the data buffer will fill the Receiver's buffer and the results will be displayed to the Terminal.



---- RUNNING ----

Run python Receiver.py on a terminal
Run python Sender.py on a seperate terminal



![SENDERANDRECIEVER](https://user-images.githubusercontent.com/91502431/218622371-72186b27-12f9-4b87-beeb-5fc182c5eabe.jpeg)




