import pika
import json

# Fonction de rappel pour traiter les résultats reçus
def callback(ch, method, properties, body):
    result = json.loads(body)
    print(f"[RESULT] Résultat reçu : {result['n1']} {result['op']} {result['n2']} = {result['result']}")

def main():
    # Connexion à RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()

    # Déclare la queue où les résultats sont envoyés
    channel.queue_declare(queue='results_queue')

    # Consommation des messages de la queue 'results_queue'
    channel.basic_consume(queue='results_queue', on_message_callback=callback, auto_ack=True)

    print("[*] Client en attente de résultats...")
    channel.start_consuming()  # Commence à consommer les messages de la queue

if __name__ == '__main__':
    main()
