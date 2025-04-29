import pika
import json
import random
import time

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='requests_queue')

    operations = ['add', 'sub', 'mul', 'div']
    
    while True:
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        op = random.choice(operations)
        
        message = {
            'n1': n1,
            'n2': n2,
            'op': op
        }

        message_json = json.dumps(message)

        channel.basic_publish(
            exchange='',
            routing_key='requests_queue',
            body=message_json
        )

        print(f"Envoyé : {message}")

        time.sleep(5 + random.uniform(-1, 1))

if __name__ == '__main__':
    main()
