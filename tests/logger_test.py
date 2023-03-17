from vclog import Logger

def main():
    # Instance logging
    logger_pepe: Logger = Logger('pacopepekatanas')
    print(id(logger_pepe), type(id(logger_pepe)))

    print('%%%%%%%%%')
    logger_pepe.info('info')
    logger_pepe.debug('debug')
    logger_pepe.warning('warning')
    logger_pepe.error('error')
    print('%%%%%%%%%')
    
    # Static logging
    Logger.info('info')
    Logger.debug('debug')
    Logger.warning('warning')
    Logger.error('error')
    print('%%%%%%%%%')
    
    # Miscellaneous
    logger_cgp: Logger = Logger('cgp')
    logger_cgp.info('training model')
    
    logger_data: Logger = Logger('data_manager')
    logger_data.info('dataset generated')
    
    print('%%%%%%%%%')
    logger_pepe.error('pepe')
    logger_data.debug('data')
    logger_cgp.warning('cgp')
    
    Logger.debug(Logger.__qualname__)


if __name__ == '__main__':
    main()
