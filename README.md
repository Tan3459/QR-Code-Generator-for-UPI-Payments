#QR Code Generator for UPI Payments

This repository contains a Python script that generates QR codes for UPI payment links compatible with popular payment apps such as PhonePe, Paytm, and Google Pay. The script dynamically creates and displays QR codes based on user-provided UPI ID.

---

## Features

- **User Input:** Accepts a UPI ID as input.
- **Dynamic UPI URLs:** Creates UPI payment URLs for:
  - PhonePe
  - Paytm
  - Google Pay
- **QR Code Generation:** Generates QR codes using the `qrcode` library.
- **Save QR Codes:** Saves the generated QR codes as PNG image files.
- **Display QR Codes:** Displays QR codes on the screen (requires `Pillow` library).

---

## Requirements

- Python 3.x
- Libraries:
  - `qrcode`
  - `Pillow` (optional, for displaying QR codes)

Install the required libraries using pip:
```bash
pip install qrcode[pil]
```

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/qrcode-upi-generator.git
   cd qrcode-upi-generator
   ```

2. Run the script:
   ```bash
   python generate_qr.py
   ```

3. Enter your UPI ID when prompted:
   ```
   Enter your UPI Id = your_upi_id@bank
   ```

4. The script will:
   - Generate UPI QR codes for PhonePe, Paytm, and Google Pay.
   - Save the QR codes as image files:
     - `phonepe_qr.png`
     - `paytm_qr.png`
     - `gpay_qr.png`
   - Display the QR codes for scanning.

---

## Example Output

**Input:**
```
Enter your UPI Id = your_upi_id@bank
```

**Output:**
- QR codes displayed on the screen.
- PNG files saved in the current directory:
  - `phonepe_qr.png`
  - `paytm_qr.png`
  - `gpay_qr.png`

---

## Customization

The payment URLs in the script can be customized to include additional parameters such as:
- **`am` (amount):** Specify a fixed payment amount.
- **`tn` (transaction note):** Add a note for the payment.
- **`mc` (merchant code):** Modify the merchant code as needed.

Example URL customization:
```python
phonepe_url = f'upi://pay?pa={upi_id}&pn=Your%20Name&am=100&cu=INR&tn=Payment%20Note'
```

---

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. All contributions are welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [qrcode Library](https://pypi.org/project/qrcode/): For generating QR codes.
- [Pillow Library](https://pillow.readthedocs.io/): For handling QR code display.

---

## Disclaimer

This script is intended for educational and personal use. Ensure that your UPI ID is correctly entered to avoid errors during payment processing.

