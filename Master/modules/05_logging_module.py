# logging is used to track or trace the information or exception i.e. it helps in debugging
from logging import *

# basiConfig(filename, filemode, level, format, datefmt, style)
# level - NOTSET(0), DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)

form = '%(lineno)d *** %(name)s *** %(asctime)s *** %(message)s '

basicConfig(filename='logged.log', level=10, filemode='w', format=form)

debug('This is debug')
info('This is info')
warning('This is warning')
error('This is error')
critical('This is critical')


textformat = '%(lineno)d | %(name)s | %(asctime)s | %(message)s'

basicConfig(filename='debug.txt', level=20, filemode='w', format=textformat)

debug('This line needs to be debug')
info('This is info')
warning('This is warning')
error('This is error')
critical('This is critical')
