'''Server'''
import encoder
import pika
import os

class Server:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config

    def publish_test_message(self, test_file):
        '''publish message to queue'''
        conn_params = pika.ConnectionParameters(self.config["rabbitmq_server"])
        with pika.BlockingConnection(conn_params) as connection:
            file_path = test_file
            channel = connection.channel()
            queue_name = 'video-encoding'
            channel.queue_declare(queue=queue_name)
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body=file_path)
            self.logger.info("Test file sent to queue: {}".format(file_path))

    def start_listening(self):
        '''receive function'''
        conn_params = pika.ConnectionParameters(self.config["rabbitmq_server"])
        with pika.BlockingConnection(conn_params) as conn:
            channel = conn.channel()
            queue_name = 'video-encoding'
            channel.queue_declare(queue=queue_name)
            channel.basic_consume(self._callback,
                                  queue=queue_name,
                                  no_ack=True)
            try:
                channel.start_consuming()
            except KeyboardInterrupt:
                self.logger.info("Quitting by keyboard interrupt")

    def _callback(self, channel, method, properties, body):
        '''callback'''
        self.logger.info("Received message from queue: %r" % body)

        file_path = body.decode("utf-8")

        if not os.path.isfile(file_path):
            self.logger.error("File does not exist: %r" % file_path)
            return

        _, file_name = os.path.split(file_path)

        out_file_path = os.path.join(os.path.dirname(os.path.realpath(file_path)),
                                     "out-" + file_name)

        encoder_instance = encoder.Encoder(self.config["ffmpeg"]["path"], self.logger)

        for result in encoder_instance.process(self.config["ffmpeg"]["command_args"],
                                               file_path, out_file_path):
            self.logger.debug("Passed time: {0} Total Time: {1}".format(result[0], result[1]))
        self.logger.debug("Completed -> %r" % out_file_path)
