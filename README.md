# VesstoR PRO

Advanced Professional Directory Scanner

Version: 7.0.0

## Features

- Multi-threaded directory scanning
- SecLists auto-detection (Kali Linux)
- Quick / Default / Deep scan modes
- Automatic JSON + TXT result saving
- Professional CLI UI
- Ctrl+C safe autosave
- Windows & Kali compatible

## Installation

git clone https://github.com/TocsiVector/VesstoR.git
cd VesstoR
pip install -r requirements.txt

## Usage

python vesstor.py -u https://target.com

Quick scan:
python vesstor.py -u target.com --quick

Deep scan:
python vesstor.py -u target.com --deep

Custom threads:
python vesstor.py -u target.com -t 20

## Output

Results are automatically saved inside:

VesstoR_Results/

Formats:
- JSON (with metadata)
- TXT (raw URLs)

## Requirements

- Python 3.9+
- requests
- SecLists (Kali)

## License

MIT
