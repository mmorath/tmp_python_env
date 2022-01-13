#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# =============================================================================
__author__ = "Matthias Morath"
__copyright__ = "Copyright 2021"
__credits__ = ["Matthias Morath"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Matthias Morath"
__email__ = "matthias.morath@gmail.com"
__status__ = "Development"
# =============================================================================
"""
Basic example showing how to read and validate data from a file using Pydantic.
"""
import os
import json
import socket

MICROSERVICE_NAME = None
MICROSERVICE_VERSION = None
NTP_HOST_01 = None
NTP_HOST_02 = None
MODBUS_TCP_HOST = None
MODBUS_TCP_PORT = None
MODBUS_TCP_NAME = None
MODBUS_TCP_MANUFACTURER = None
MODBUS_TCP_DESCRIPTIPON = None
MODBUS_TCP_ORDER_NO = None
MQTT_HOST = None
MQTT_PORT = None
MQTT_ENABLE_SSL = None
MQTT_USER = None
MQTT_PASSWORD = None

#dictionary of eviroment variables inlcuding type
envVariables = {
        'MICROSERVICE_NAME' :"%s",
        'MICROSERVICE_VERSION' :"%s",
        'NTP_HOST_01' :"%s",
        'NTP_HOST_02' :"%s",
        'MODBUS_TCP_HOST' :"%s",
        'MODBUS_TCP_PORT' :"%i",
        'MODBUS_TCP_NAME' :"%s",
        'MODBUS_TCP_MANUFACTURER' :"%s",
        'MODBUS_TCP_DESCRIPTIPON' :"%s",
        'MODBUS_TCP_ORDER_NO' :"%s",
        'MQTT_HOST' :"%s",
        'MQTT_PORT' :"%i",
        'MQTT_ENABLE_SSL' :"%r",
        'MQTT_USER' :"%s",
        'MQTT_PASSWORD' :"%s",
}

###############################################################################################################
# Envrioment settings helper function
###############################################################################################################
def importEnviromentVariables(envDict):
    """ import enviroment variables ...enviroment variables are set in docker-compose file """
    #create a list which will hold missing env variables
    missingEnvVars = []
    #for each item in the envDict dictionary
    for item in envDict:
        #read the envrioment variable from operating system
        val = os.environ.get(item)
        #Check if read input is type none or has no entry
        if (val == None) or (val == ""):
            #if value is missing append it to the list
            missingEnvVars.append(item)
        else:
            #check for type string
            if (envDict[item] == "%s"):
                exec(("%s = "+envDict[item]) % (item, val),globals())
            #check for type int    
            elif(envDict[item] == "%i"):
                exec(("%s = "+envDict[item]) % (item, int(val)),globals())
            #check for type boolean
            elif(envDict[item] == "%r"):
                exec(("%s = "+envDict[item]) % (item, json.loads(val.lower())),globals())
            else:
                #unknown type not defined...
                print(f"Unknown type")
    #if list holds missing variables
    if len(missingEnvVars) > 0:
        #return false and the list of missing variables
        return False, missingEnvVars
    else:
        #return true with emtpy list
        return True, []


def get_microServiceInfo():
    """ get all enviroment infos"""
    print('Micro Service started')
    print(f"CONTAINER_NAME: {socket.gethostname()} CONTAINER_IP: {socket.gethostbyname(socket.gethostname())}")
    print('Service startet with the following enviroment variables')
    print(f"MICROSERVICE_NAME:{MICROSERVICE_NAME} MICROSERVICE_VERSION:{MICROSERVICE_VERSION}")
    print(f"MODBUS_TCP_HOST:{MODBUS_TCP_HOST} MODBUS_TCP_PORT:{MODBUS_TCP_PORT}")
    print(f"MODBUS_TCP_NAME:{MODBUS_TCP_NAME} MODBUS_TCP_MANUFACTURER:{MODBUS_TCP_MANUFACTURER}") 
    print(f"MODBUS_TCP_DESCRIPTIPON:{MODBUS_TCP_DESCRIPTIPON} MODBUS_TCP_ORDER_NO:{MODBUS_TCP_ORDER_NO}") 
    print(f"MQTT_HOST:{MQTT_HOST} MQTT_PORT:{MQTT_PORT}")
    print(f"MQTT_ENABLE_SSL:{MQTT_ENABLE_SSL} MQTT_USER:{MQTT_USER} MQTT_PASSWORD:{MQTT_PASSWORD}")

def main():
    """Main function."""
    importEnviromentVariables(envVariables)
    get_microServiceInfo()

if __name__ == "__main__":
    pass
    #main()