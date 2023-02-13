#!/usr/bin/env python

#Importing the Python Library for RabbitMQ and sys for exiting the program
import pika, sys, os

def main():

    #Creating a connection to RabbitMQ
    #Assuming RabbitMQ is running on localhost
    #If not, change the host to the IP address of the machine where RabbitMQ is running

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Creating a queue named hello

    channel.queue_declare(queue='task_queue')

    #Publishing a message to the queue
    #Receive messages from the queue named hello on the default exchange (an empty string)
    #Receving is complex and done by a callback function

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)