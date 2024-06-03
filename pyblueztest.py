import bluetooth

def discover_devices():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=True)
    if nearby_devices:
        print("Found %d devices:" % len(nearby_devices))
        for addr, name, _ in nearby_devices:
            #if addr == "D8:0F:99:43:06:A0":
                print("Device Name:", name)
                print("Device Address:", addr)
                print("Services:")
                services = bluetooth.find_service(address=addr)
                if services:
                    for svc in services:
                        print("  Service Name:", svc["name"])
                        print("    Host:", svc["host"])
                        print("    Description:", svc["description"])
                        print("    Protocol:", svc["protocol"])
                        print("    Provider:", svc["provider"])
                else:
                    print("  No services found.")
                print()
    else:
        print("No devices found.")

if __name__ == "__main__":
    discover_devices()
