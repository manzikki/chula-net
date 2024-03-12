import asyncio
from bleak import BleakScanner, BleakClient

uart_service_uuid = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
uart_write_characteristic_uuid = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
uart_read_characteristic_uuid = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
data_to_write = bytearray([0xf3, 0x13, 0xf3])

async def run():
    mydev = None
    myaddr = ""
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
        if d.name:
            if "Holy" in d.name:
                print(d)
                mydev = d
    if not mydev:
        print("Did not find the IoT device.")
    else:
        #CB:23:11:E1:A4:CD: Holy-IOT
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
                print("Characteristics:")
                chars = service.characteristics
                for char in chars:
                    print(" ",char)
            #try sending data to the uart service
            print("sending")
            await client.write_gatt_char(uart_write_characteristic_uuid, data_to_write)
            print("Data written to the device")
            #reading
            await asyncio.sleep(1)  # Adjust the sleep time as needed
            # Read the response from the UART read characteristic
            response = await client.read_gatt_char(uart_read_characteristic_uuid)
            print(f"Response from the device: {response}")

#00001800-0000-1000-8000-00805f9b34fb (Handle: 1): Generic Access Profile
#Characteristics:
#  00002a00-0000-1000-8000-00805f9b34fb (Handle: 2): Device Name
#  00002a01-0000-1000-8000-00805f9b34fb (Handle: 4): Appearance
#  00002a04-0000-1000-8000-00805f9b34fb (Handle: 6): Peripheral Preferred Connection Parameters
#  00002aa6-0000-1000-8000-00805f9b34fb (Handle: 8): Central Address Resolution
#00001801-0000-1000-8000-00805f9b34fb (Handle: 10): Generic Attribute Profile
#Characteristics:
#6e400001-b5a3-f393-e0a9-e50e24dcca9e (Handle: 11): Nordic UART Service
#Characteristics:
#  6e400002-b5a3-f393-e0a9-e50e24dcca9e (Handle: 12): Nordic UART RX
#  6e400003-b5a3-f393-e0a9-e50e24dcca9e (Handle: 14): Nordic UART TX

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
