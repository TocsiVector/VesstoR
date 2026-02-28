#!/usr/bin/env python3

import requests
import argparse
import os
import signal
import sys
import threading
import time
import random
import json
from datetime import datetime
from urllib.parse import urlparse, urljoin
import shutil

VERSION = "7.0.0"
TOOL_NAME = "VesstoR"

# ===================== COLOR SYSTEM ===================== #

COLORS = [
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m", "\033[96m"
]

RESET = "\033[0m"
BOLD = "\033[1m"
GRAY = "\033[90m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

def random_color():
    return random.choice(COLORS)

def separator():
    width = shutil.get_terminal_size().columns
    print(GRAY + "═" * width + RESET)

# ===================== PROFESSIONAL BANNER ===================== #

def banner():
    width = shutil.get_terminal_size().columns
    color = random_color()

    logo = [
        "██╗   ██╗███████╗███████╗███████╗████████╗ ██████╗ ██████╗",
        "██║   ██║██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗",
        "██║   ██║█████╗  ███████╗███████╗   ██║   ██║   ██║██████╔╝",
        "╚██╗ ██╔╝██╔══╝  ╚════██║╚════██║   ██║   ██║   ██║██╔══██╗",
        " ╚████╔╝ ███████╗███████║███████║   ██║   ╚██████╔╝██║  ██║",
        "  ╚═══╝  ╚══════╝╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝",
        "",
        f"{TOOL_NAME} PRO v{VERSION}",
        "Advanced Professional Directory Scanner"
    ]

    print("\n")
    for line in logo:
        print(f"{color}{BOLD}{line.center(width)}{RESET}")
    print("\n")

# ===================== WORDLIST SYSTEM ===================== #

SECLIST_BASE = "/usr/share/seclists/Discovery/Web-Content"

WORDLISTS = {
    "quick": ["common.txt", "raft-small-directories.txt"],
    "default": ["raft-medium-directories.txt", "directory-list-2.3-medium.txt"],
    "deep": ["raft-large-directories.txt", "directory-list-2.3-big.txt"]
}

def auto_detect_wordlist(mode):
    if not os.path.exists(SECLIST_BASE):
        print(RED + "[!] SecLists not installed." + RESET)
        sys.exit(1)

    for filename in WORDLISTS.get(mode, WORDLISTS["default"]):
        full_path = os.path.join(SECLIST_BASE, filename)
        if os.path.exists(full_path):
            print(GREEN + f"[+] Using wordlist: {filename}" + RESET)
            return full_path

    print(RED + "[!] Suitable wordlist not found." + RESET)
    sys.exit(1)

# ===================== SCANNER ===================== #

class VesstoRScanner:

    def __init__(self, base_url, mode, threads, delay):
        self.base_url = base_url
        self.mode = mode
        self.threads = threads
        self.delay = delay
        self.wordlist_path = auto_detect_wordlist(mode)
        self.entries = self.load_wordlist()
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": f"{TOOL_NAME}-Scanner"})
        self.found = []
        self.lock = threading.Lock()
        self.start_time = time.time()
        self.output_folder = "VesstoR_Results"
        os.makedirs(self.output_folder, exist_ok=True)

    def load_wordlist(self):
        with open(self.wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            return [line.strip() for line in f if line.strip()]

    def scan_entry(self, entry):
        url = urljoin(self.base_url, entry.strip("/") + "/")
        try:
            r = self.session.get(url, timeout=8, allow_redirects=True)
            if r.status_code == 200:
                with self.lock:
                    self.found.append(url)
                print(GREEN + "[200] ➜ " + RESET + url)
        except requests.RequestException:
            pass
        time.sleep(self.delay)

    # ===================== AUTO SAVE ===================== #

    def save_results(self):
        domain = urlparse(self.base_url).netloc
        json_file = os.path.join(self.output_folder, f"{TOOL_NAME}_{domain}.json")
        txt_file = os.path.join(self.output_folder, f"{TOOL_NAME}_{domain}.txt")

        data = {
            "tool": TOOL_NAME,
            "version": VERSION,
            "target": self.base_url,
            "mode": self.mode,
            "threads": self.threads,
            "delay": self.delay,
            "total_found": len(self.found),
            "results": self.found,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(json_file, "w") as jf:
            json.dump(data, jf, indent=4)

        with open(txt_file, "w") as tf:
            for url in self.found:
                tf.write(url + "\n")

        print(GREEN + f"\n[+] Results saved in folder: {self.output_folder}" + RESET)

    def run(self):
        separator()
        print(CYAN + f"Target   : {self.base_url}" + RESET)
        print(CYAN + f"Mode     : {self.mode}" + RESET)
        print(CYAN + f"Threads  : {self.threads}" + RESET)
        print(CYAN + f"Delay    : {self.delay}" + RESET)
        print(CYAN + f"Entries  : {len(self.entries)}" + RESET)
        separator()
        print(YELLOW + "\n[+] Scan Started...\n" + RESET)

        threads_list = []

        for entry in self.entries:
            t = threading.Thread(target=self.scan_entry, args=(entry,))
            t.start()
            threads_list.append(t)

            if len(threads_list) >= self.threads:
                for th in threads_list:
                    th.join()
                threads_list = []

        for th in threads_list:
            th.join()

        duration = round(time.time() - self.start_time, 2)

        separator()
        print(GREEN + f"[✔] Scan Completed in {duration} sec" + RESET)
        print(GREEN + f"[+] Total Found: {len(self.found)}" + RESET)
        separator()

        self.save_results()

# ===================== CTRL+C SAFE SAVE ===================== #

def handle_interrupt(sig, frame):
    print(RED + "\n[!] Scan interrupted. Saving results..." + RESET)
    try:
        scanner.save_results()
    except:
        pass
    sys.exit(0)

# ===================== MAIN ===================== #

def main():
    global scanner

    parser = argparse.ArgumentParser(description="VesstoR PRO - Directory Scanner")

    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--deep", action="store_true")
    parser.add_argument("-t", "--threads", type=int, default=10)
    parser.add_argument("--delay", type=float, default=0.1)
    parser.add_argument("-v", "--version", action="store_true")

    args = parser.parse_args()

    if args.version:
        print(f"{TOOL_NAME} Version {VERSION}")
        sys.exit(0)

    banner()

    if args.quick:
        mode = "quick"
    elif args.deep:
        mode = "deep"
    else:
        mode = "default"

    base_url = args.url
    if not urlparse(base_url).scheme:
        base_url = "http://" + base_url

    scanner = VesstoRScanner(
        base_url=base_url,
        mode=mode,
        threads=args.threads,
        delay=args.delay
    )

    signal.signal(signal.SIGINT, handle_interrupt)

    scanner.run()

if __name__ == "__main__":
    main()
