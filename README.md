<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00FF9C&size=35&center=true&vCenter=true&width=900&lines=VesstoR+PRO+v7.0.0;Advanced+Directory+Scanner;Fast+%7C+Accurate+%7C+Automated" />
</p>

<h1 align="center">🚀 VesstoR PRO</h1>

<p align="center">
Advanced Professional Directory Scanner for Web Reconnaissance & Security Testing
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue"/>
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-green"/>
  <img src="https://img.shields.io/badge/Version-7.0.0-red"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow"/>
</p>

---

## 🧠 Overview

VesstoR PRO is a **high-performance directory and endpoint discovery tool** designed for:

* Web reconnaissance
* Hidden path discovery
* Bug bounty workflows
* Security testing

It combines speed, automation, and structured output to streamline reconnaissance tasks.

---

## 🔥 Features

* ✔ Multi-threaded directory scanning
* ✔ SecLists auto-detection (Kali Linux)
* ✔ Quick / Default / Deep scan modes
* ✔ Automatic JSON + TXT result saving
* ✔ Clean CLI interface
* ✔ Ctrl+C safe autosave
* ✔ Cross-platform (Linux & Windows)

---

## ⚙️ Installation

```bash id="a1"
git clone https://github.com/TocsiVector/VesstoR.git
cd VesstoR
pip install -r requirements.txt
```

---

## ▶️ Usage

### Basic Scan

```bash id="a2"
python vesstor.py -u https://target.com
```

### Quick Scan

```bash id="a3"
python vesstor.py -u target.com --quick
```

### Deep Scan

```bash id="a4"
python vesstor.py -u target.com --deep
```

### Custom Threads

```bash id="a5"
python vesstor.py -u target.com -t 20
```

---

## 📊 Output

Results are automatically stored in:

```id="a6"
VesstoR_Results/
```

### Formats:

* JSON (structured metadata)
* TXT (raw discovered URLs)

---

## ⚠️ Requirements

* Python 3.9+
* `requests`
* SecLists (recommended for Kali users)

---

## 🛠️ Roadmap

* [ ] Subdomain integration
* [ ] Recursive scanning improvements
* [ ] Proxy support
* [ ] Rate limiting control

---

## 📜 License

MIT License

---

## 👤 Author

**TocsiVector**

---

## ⭐ Support

If you find this useful, give it a ⭐ on GitHub.

---

## ⚠️ Disclaimer

This tool is intended for **authorized security testing only**.
Do not use on systems without permission.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FF9C,100:007CF0&height=120&section=footer"/>
</p>
