import pika
import json
import time
import random

def callback(ch, method, properties, body):
    data = json.loads(body)

    if data.get('op') == 'div':
        n1, n2 = data['n1'], data['n2']
        if n2 == 0:
            result_value = "Erreur: division par zéro"
        else:
            result_value = n1 / n2

        time.sleep(random.randint(5, 15))
        result = {
            'n1': n1,
            'n2': n2,
            'op': 'div',
            'result': result_value
        }
        ch.basic_publish(exchange='', routing_key='results_queue', body=json.dumps(result))
        print(f"[DIV] Résultat envoyé : {result}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='requests_queue')
    channel.queue_declare(queue='results_queue')
    channel.basic_consume(queue='requests_queue', on_message_callback=callback, auto_ack=True)
    print("[*] Worker DIV en attente de messages...")
    channel.start_consuming()

if __name__ == '__main__':
    main()
