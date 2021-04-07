from jnpr.junos import Device
from pprint import pprint
import json


with Device(host='dallas-fw0', user='automation', password='juniper123') as network_device:
    try:
        route_table = network_device.rpc.get_route_information({'format': 'json'})
    except:
        pass

pprint(route_table)