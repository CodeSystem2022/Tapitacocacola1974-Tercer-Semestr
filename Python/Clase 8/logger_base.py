import logging as log



log.basicConfig(level=log.DEBUG,
                    format='%(asctime)s:%(levelname)s[%(filename)s:%(lineno)s]%(message)s',
                    datefmt='%I:%M:%S %p',
                    handlers=[
                        log.FileHandler('capa_datos.log'),
                        log.StreamHandler()
                    ])

if __name__== '__main__':
    log.debug('mensaje nivel debu')
    log.info('mensaje nivel info')
    log.warning('mensaje nivel warning')
    log.error('mensaje nivel error')
    log.critical('mensaje nivel critical')


