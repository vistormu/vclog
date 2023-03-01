from vclog import Logger


def main():
    # Static logging
    Logger.info('info')
    Logger.debug('debug')
    Logger.warning('warning')
    Logger.error('error')

    # Instance logging
    logger: Logger = Logger('test')

    logger.info('info')
    logger.debug('debug')
    logger.warning('warning')
    logger.error('error')


if __name__ == '__main__':
    main()
