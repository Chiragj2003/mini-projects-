# QR Code Generator

Generate QR codes from text or URLs.

## Features
- 📱 Generate QR codes from any text or URL
- 💾 Save QR codes as PNG images
- 🎨 Customizable size and border
- ⚡ Simple command-line interface

## Requirements
```bash
pip install qrcode pillow
```

## Usage
```bash
python qr_code_generator.py
```

Enter your text or URL when prompted, and a QR code will be saved as `qrcode.png`.

## Example
```
Enter text or URL to convert to QR code: https://github.com
QR code saved as qrcode.png
```

## Customization
You can modify the QR code settings in the code:
- `version` - Size (1-40, higher = bigger)
- `box_size` - Pixel size of each box
- `border` - Border width in boxes
- `fill` - QR code color
- `back_color` - Background color
