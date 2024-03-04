import asyncio
from bleak import BleakScanner, BleakClient

async def run():
    mydev = None
    myaddr = ""
    devices = await BleakScanner.discover()
    for d in devices:
        if d.name:
            if "Holy" in d.name:
                print(d)
                mydev = d
    if not mydev:
        print("Did not find the IoT device.")
    else:
        #get services
        #print(dir(mydev)) #address, details etc
        #check https://getwavecake.com/blog/reading-your-phones-battery-level-over-bluetooth-ble-with-python-bleak/
        print(mydev.address)
        myaddr = mydev.address
    if not myaddr:
        print("Could not get the address of the device.")
    else:
        async with BleakClient(myaddr) as client:
            svcs = client.services
            print("Services:")
            for service in svcs:
                print(service)
#00001800-0000-1000-8000-00805f9b34fb (Handle: 1): Generic Access Profile
#00001801-0000-1000-8000-00805f9b34fb (Handle: 10): Generic Attribute Profile
#6e400001-b5a3-f393-e0a9-e50e24dcca9e (Handle: 11): Nordic UART Service

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
