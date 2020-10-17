#!/usr/bin/env python3

import os
import sys
import shutil
import requests

def safe_write(filename: str, content: bytes):
    if os.path.isfile(filename) or os.path.isdir(filename) or os.path.islink(filename):
        print("file exists or is dir or is link - aborting!")
        sys.exit(2)
    with open(filename, "wb") as ifile:
        ifile.write(content)


def safe_move(src: str, dst: str):
    if os.path.isdir(src) or os.path.islink(src):
        print("source file is not a file")
        sys.exit(2)
    shutil.copy(src,dst)

def get_minikube():
    # latest and greatest!
    latest_URL = "https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"
    try:
        r = requests.get(latest_URL)
        safe_write("minikube", r.content)
    except e: # TODO: specific error
        print(e)
    safe_move("kubectl", "/usr/local/bin/minikube")
    os.chown("/usr/local/bin/minikube",0,0)
    os.chmod("/usr/local/bin/minikube",0755)

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
    if not sys.platform.startswith("linux"):
        print("Only supported on Linux")
        sys.exit(1)
