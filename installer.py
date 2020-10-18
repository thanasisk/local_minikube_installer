#!/usr/bin/env python3

import os
import sys
import shutil
import requests

def safe_write(filename: str, content: bytes) -> None:
    if os.path.isfile(filename) or os.path.isdir(filename) or os.path.islink(filename):
        print("file exists or is dir or is link - aborting!")
        sys.exit(2)
    with open(filename, "wb") as ifile:
        ifile.write(content)


def safe_move(src: str, dst: str) -> None:
    if os.path.isdir(src) or os.path.islink(src):
        print("source file is not a file")
        sys.exit(2)
    shutil.copy(src,dst)

def get_minikube() -> None:
    # latest and greatest!
    latest_URL = "https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"
    r = requests.get(latest_URL)
    safe_write("minikube", r.content)
    safe_move("minikube", "/usr/local/bin/minikube")
    os.unlink("minikube")
    os.chown("/usr/local/bin/minikube",0,0)
    os.chmod("/usr/local/bin/minikube",755)

def get_kubectl():
    r = requests.get("https://storage.googleapis.com/kubernetes-release/release/stable.txt")
    latest = r.text
    final = "https://storage.googleapis.com/kubernetes-release/release/"+latest+"/bin/linux/amd64/kubectl"
    r = requests.get(final)
    safe_write("kubectl",r.content)
    safe_move("kubectl","/usr/local/bin/kubectl")
    os.unlink("kubectl")
    os.chown("/usr/local/bin/kubectl",0,0)
    os.chmod("/usr/local/bin/kubectl",755)

def are_we_root():
    if os.geteuid() != 0:
       print("This script must be run as root")
       sys.exit(1)

def are_we_on_linux():
    if not sys.platform.startswith("linux"):
        print("Only supported on Linux")
        sys.exit(1)

are_we_on_linux()
are_we_root()
get_kubectl()
get_minikube()
