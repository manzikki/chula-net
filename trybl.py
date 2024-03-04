import asyncio
from bleak import BleakScanner

async def run():
    devices = await BleakScanner.discover()
    foundhi = False
    for d in devices:
        if d.name:
            if "Holy" in d.name:
                print(d)
                foundhi = True
                
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
