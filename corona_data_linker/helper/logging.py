import logging

def logging_config():
    # config logging
    logger = logging.getLogger('corona_data_linker_logger')
    logger.setLevel(logging.DEBUG)

    # config logging handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # config logging format
    _format = logging.Formatter('%(asctime)s：[%(levelname)s] %(message)s')
    stream_handler.setFormatter(_format)
    logger.addHandler(stream_handler)
