# 🚀 VesstoR PRO

![Python](https://img.shields.io/badge/Language-Python-blue)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-green)
![Version](https://img.shields.io/badge/Version-7.0.0-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

> ⚡ Advanced Professional Directory Scanner for Security Testing

---

## 🧠 Overview

VesstoR PRO is a **high-performance directory and endpoint discovery tool** built for:

* Web reconnaissance
* Hidden path discovery
* Security testing
* Bug bounty workflows

It supports multiple scan modes, automation, and structured output for faster analysis.

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

```bash id="ves1"
git clone https://github.com/TocsiVector/VesstoR.git
cd VesstoR
pip install -r requirements.txt
```

---

## ▶️ Usage

### Basic Scan

```bash id="ves2"
python vesstor.py -u https://target.com
```

### Quick Scan

```bash id="ves3"
python vesstor.py -u target.com --quick
```

### Deep Scan

```bash id="ves4"
python vesstor.py -u target.com --deep
```

### Custom Threads

```bash id="ves5"
python vesstor.py -u target.com -t 20
```

---

## 📊 Output

Results are automatically saved in:

```
VesstoR_Results/
```

### Formats:

* JSON (structured data with metadata)
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
