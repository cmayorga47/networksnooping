import random

#for creating mock date that gets printed to file bandwidth.snmprec, which is what is called in api and displayed on UI

def generate_snmprec(filename='bandwidth.snmprec', interfaces=[1, 2], steps=10, base_in=1_000_000, base_out=1_500_000):
    with open(filename, 'w') as f:
        # Static system info
        f.write('# Static System Info\n')
        f.write('1.3.6.1.2.1.1.1.0|4|Linux SNMP Simulator\n')              # sysDescr
        f.write('1.3.6.1.2.1.1.4.0|4|admin@example.com\n')                # sysContact
        f.write('1.3.6.1.2.1.1.5.0|4|test-host\n')                         # sysName
        f.write('1.3.6.1.2.1.1.6.0|4|Data Center 1\n')                     # sysLocation
        f.write('1.3.6.1.2.1.1.2.0|6|1.3.6.1.4.1.8072.3.2.10\n')           # sysObjectID

        for step in range(65, 65 + steps):  # simulate time
            f.write(f'1.3.6.1.2.1.1.3.0|2|{step * 10000}\n')  # sysUpTime in timeticks

            for iface in interfaces:
                in_octets = base_in + random.randint(0, 500000) + (step - 65) * 500000
                out_octets = base_out + random.randint(0, 500000) + (step - 65) * 500000

                f.write(f'1.3.6.1.2.1.2.2.1.10.{iface}|2|{in_octets}\n')  # ifInOctets
                f.write(f'1.3.6.1.2.1.2.2.1.16.{iface}|2|{out_octets}\n')  # ifOutOctets

if __name__ == '__main__':
    generate_snmprec()
