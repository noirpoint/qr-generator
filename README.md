# QR Code Generator

## Installation

  1. Clone the repository:
  git clone https://github.com/YOUR-USERNAME/qr-generator.git

  2. Install dependencies:
  pip install qrcode[pil] validators

## Usage

  Run the script:
  python qr_generator.py

  Input examples:
  Enter a link (example: https://example.com): https://google.com
  Enter file name and format: my_qr.png

## Features

  - Supported formats: PNG, JPEG
  - URL validation
  - Filename checks:
    - Blocked characters: \ / : * ? " < > |
    - Auto-extension correction
  - Dependencies:
    - qrcode[pil] >=7.4
    - validators >=0.20.0
    - Python 3.8+


## Limitations
  No GUI interface

  Basic error handling

  JPEG requires Pillow

  No color customization

## License
  MIT License.
