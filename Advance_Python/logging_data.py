from logging import *

#config logging file.
#basicConfig(filename='logfile.log', level=DEBUG, filemode='w', format='%(asctime)s -- %(message)s') #create log file and formate change level and change mode jisse bar ba rfile append na ho.
#formate uper phle se hi define kar dete hia jisse line bdi na ho ek tarika uper hai

#LOG_FORMATE = '%(asctime)s // %(message)s // %(lineno)d'
LOG_FORMATE = '{lineno} // {asctime} // {message} // {name}' #styling the formate

basicConfig(filename='logfile.log', level=DEBUG, filemode='w', format=LOG_FORMATE, style='{')

#change logger name
logger = getLogger('Madhu')

logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")