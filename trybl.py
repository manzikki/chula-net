import asyncio
from bleak import BleakScanner

mydev = None

async def run():
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
        print(dir(mydev))
        #check https://getwavecake.com/blog/reading-your-phones-battery-level-over-bluetooth-ble-with-python-bleak/
        
        
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
