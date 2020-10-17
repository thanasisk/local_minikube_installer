#!/usr/bin/env python3

import os
import sys
import requests

def safe_write(filename: str, content: bytes):
    pass

def get_minikube():
    # latest and greatest!
    latest_URL = "https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"
    try:
        r = requests.get(latest_URL)
        safe_write("kubectl", r.content)
    except: # TODO: specific error
    #sudo install minikube-linux-amd64 /usr/local/bin/minikube
    pass

def get_kubectl():
    #curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
    #chmod +x ./kubectl
    #sudo mv ./kubectl /usr/local/bin/kubectl
    pass

def are_we_root():
    if os.geteuid() != 0:
       print("This script must be run as root")
       sys.exit(1)

def are_we_on_linux():
    pass
