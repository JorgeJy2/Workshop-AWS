import logging


class Logger:
    @staticmethod
    def get_logger(local: bool) -> logging:
        """
        Obtiene el logger formateado
        @param local: Indicador de ejecución de la lambda:
            True: Ejecución local
            False: Ejecución en Lambda
        @type local: bool
        @return: logger formateado
        @rtype: object
        """
        if local:
            logging.basicConfig(
                format='%(asctime)s.%(msecs)d, %(levelname)-4s in %(filename)s line %(lineno)d: %(message)s',
                datefmt='%Y-%m-%d:%H:%M:%S',
                level=logging.INFO)
            return logging.getLogger(__name__)
        else:
            logger = logging.getLogger()
            handler = logger.handlers[0]
            handler.setFormatter(
                logging.Formatter("%(asctime)s.%(msecs)d, %(levelname)-4s in %(filename)s line %(lineno)d: %(message)s",
                                  "%Y-%m-%d:%H:%M:%S"))
            logger.setLevel(logging.INFO)
            return logger
