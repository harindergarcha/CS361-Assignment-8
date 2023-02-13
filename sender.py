#!/usr/bin/env python

#Importing the Python Library for RabbitMQ
import pika
import json
import requests

#Creating a connection to RabbitMQ
#Assuming RabbitMQ is running on localhost
#If not, change the host to the IP address of the machine where RabbitMQ is running

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Creating a queue named hello
#If the queue already exists, this method does nothing

channel.queue_declare(queue = 'task_queue')
message = {'id': 1, 'name': 'name1'}

#Publishing a message to the queue
#Json dumps is used to convert the message to a string
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=json.dumps(message),
                      properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)

#connection.close()
connection.close()
