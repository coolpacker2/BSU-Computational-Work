import asyncio
from bleak import BleakClient, BleakScanner
uuid_unknown_service = '0000180F-0000-1000-8000-00805F9B34FB'
uuid_unknown_characteristic = '00002A19-0000-1000-8000-00805F9B34FB'

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d.address, d.name)
        if d.address == "D8:4D:72:C3:B7:4B":           #D4:FB:85:4B:B7:67 is kamigami
            print("Found")
            async with BleakClient(d, timeout=22.0) as client:
                print("Services:")   
                for service in client.services:
                    print(service)
                    unknown = await client.read_gatt_char(uuid_unknown_characteristic)
                    print(int.from_bytes(unknown,byteorder='big'))
                


asyncio.run(main())