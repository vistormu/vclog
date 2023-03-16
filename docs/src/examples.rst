Examples
========

Using the logger as a static class:

.. code-block:: Python

    Logger.info('message to log')
    Logger.info('message', 'to', 'log')
    Logger.debug('Result: ', 42)

Using the logger as an instance:

.. code-block:: Python

    logger: Logger = Logger('name')
    logger.info('message to log')
    logger.info('message', 'to', 'log')
    logger.debug('Result: ', 42)