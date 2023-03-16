from vclog import Logger
import time


def main():
    # Instance logging
    logger: Logger = Logger('pacopepekatanas')

    print('%%%%%%%%%')
    logger.info('info')
    logger.debug('debug')
    logger.warning('warning')
    logger.error('error')
    print('%%%%%%%%%')
    
    # Static logging
    Logger.info('info')
    Logger.debug('debug')
    Logger.warning('warning')
    Logger.error('error')
    print('%%%%%%%%%')
    
    # Miscellaneous
    logger: Logger = Logger('cgp')
    logger.info('training model')
    
    logger: Logger = Logger('data_manager')
    logger.info('dataset generated')
    
    Logger.debug('12.0876')
    
    before: float = time.time()
    for i in range(100_000):
        Logger.info(i, flush=True)
    after: float = time.time()
    
    Logger.info(f'Time spent: {after-before:.2f}s')


if __name__ == '__main__':
    main()
