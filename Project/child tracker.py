import json
import wiotp.sdk.device
import time
myconfig = {
        "identity": {
        "orgId":"46l0go",
        "typeId": "varshakumar",
        "deviceId":"270602"
        },
        "auth": {
            "token": "Varsha160712!"
            }
        }
client =wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connnect()

while True:
        name= "Smartbridge"
        #in area location

        #latitude=17.4225176
        #longitutde=78.5458842

        #out area location

        latiude =17.4219272
        longitude=78.5458843

        myData={'name': name, 'lat': latitude,'lon':longitude}
        client.publishEvent(evenId="status",msgformat="json",data=myData,qos=0, onPublish=None)
        print("Data published to IBM Iot platform:",myData)
        time.sleep(5)

client.disconnect()
                            

        
        
        
