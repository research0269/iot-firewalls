# the list of device configs are from our own lab
# one should change it accordingly for their devices

DEVICE_CONFIGS = {
    'wyze_cam': {
        "mac": "2c:aa:8e:9a:64:b7", 
        "ip": "192.168.143.252", 
        "name": "Wyze Cam", 
        "product": "wyze_camera", 
        "feature": "hostname", 
        "thresh": 1
    },
    'belkin_switch': {
        "mac": "c4:41:1e:5b:18:a5", 
        "ip": "192.168.143.251", 
        "name": "Belkin Switch", 
        "product": "belkin_switch", 
        "feature": "hostname", 
        "thresh": 1
    },
    'ring_cam': {
        "mac": "54:e0:19:3c:7c:14", 
        "ip": "192.168.143.253", 
        "name": "Ring Cam", 
        "product": "ring_camera", 
        "feature": "hostname", 
        "thresh": 1
    },
    'philips_hue': {
        "mac": "00:17:88:72:7b:50", 
        "ip": "192.168.143.249", 
        "name": "Philips Hue Lightbulb", 
        "product": "philips_hue", 
        "feature": "hostname", 
        "thresh": 1
    },
    'sonos_one': {
        "mac": "48:a6:b8:fb:b1:66", 
        "ip": "192.168.143.248", 
        "name": "Sonos One", 
        "product": "sonos_speaker", 
        "feature": "hostname", 
        "thresh": 1
    },
    'amazon_echo_dot': {
        "mac": "1c:4d:66:fc:13:79",
        "ip": "192.168.143.250",
        "name": "Amazon Echo Dot",
        "product": "amazon_echo",
        "feature": "hostname",
        "thresh": 1
    },
    'tplink_switch': {
        "mac": "50:c7:bf:09:f3:4c",
        "ip": "192.168.143.80",
        "name": "TP-Link Kasa Smart WiFi Plug",
        "product": "tplink_switch",
        "feature": "hostname",
        "thresh": 1
    },
    'amazon_fire': {
        "mac": "f0:f0:a4:f8:e5:fc",
        "ip": "192.168.143.118",
        "name": "Amazon Fire TV Stick",
        "product": "amazon_fire",
        "feature": "hostname",
        "thresh": 1
    },
    'google_home': {
        "mac": "a4:77:33:2f:e0:6e",
        "ip": "192.168.143.20",
        "name": "Google Home Assistant",
        "product": "google_google-home",
        "feature": "hostname",
        "thresh": 1
    },
    'google_chromecast': {
        "mac": "f0:72:ea:e3:88:c2",
        "ip": "192.168.143.123",
        "name": "Google Chromecast TV",
        "product": "google_chromecast",
        "feature": "hostname",
        "thresh": 1
    },
}

ALLOWLIST_DIR = "./data/allowlists"
LOG_DIR = "./data/logs"