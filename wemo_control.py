import sys
import pywemo
from argparse import ArgumentParser

def do_discovery():
    print('Discovering devices...')
    devices = pywemo.discover_devices()
    print('{0:20} {1}'.format('Name','MAC'))
    for device in devices:
        print('{0:20} {1}'.format(device.name, device.mac))


def set_power(mac, state):
    print('Turning device at MAC {} {}'.format(mac, 'on' if state else 'off'))
    devices = pywemo.discover_devices()
    for device in devices:
        if device.mac == mac:
            device.set_state(state)
            break

def get_state(mac):
    devices = pywemo.discover_devices()
    for device in devices:
        if device.mac == mac:
            state = device.get_state()
            print('{} is {}.'.format(mac, 'on' if state else 'off'))
            break


if __name__ == '__main__':
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--on', help='Set the device at MAC address to on',
            metavar='MAC')
    group.add_argument('--off', help='Set the device at MAC address to off',
            metavar='MAC')
    group.add_argument('--discover', help='Discover devices on the network',
            action='store_true')
    group.add_argument('--state', help='Return state of the device at MAC',
            metavar='MAC')
    args = parser.parse_args()

    if args.discover:
        do_discovery()
    elif args.state:
        get_state(args.state)
    elif args.off:
        set_power(args.off, False)
    elif args.on:
        set_power(args.on, True)
    else:
        parser.print_help()
