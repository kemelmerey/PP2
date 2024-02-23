import json
with open('json/sample-data.json', 'r') as file:
    data = json.load(file)
def format_interface(interface):
    dn = interface.get('attributes', {}).get('dn', '')
    description = interface.get('attributes', {}).get('descr', '')
    speed = interface.get('attributes', {}).get('speed', 'inherit')
    mtu = interface.get('attributes', {}).get('mtu', '')
    return f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}"
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
for interface in data.get('imdata', []):
    print(format_interface(interface.get('l1PhysIf', {})))