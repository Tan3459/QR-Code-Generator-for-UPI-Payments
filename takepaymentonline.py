import qrcode
#Taking upi ID as a input
upi_id=input("Enter your UPI Id = ")

#upi://pay?pa=upi_id&pn=Name&am=Amount&cu=CURRENCY&tn=MESSAGE
#defining the payment url based on the upi id andthe payment app
phonepe_url=f'upi://pay?pa={upi_id}&pn=recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=recipient%20Name&mc=1234'
gpay_url=f'upi://pay?pa={upi_id}&pn=recipient%20Name&mc=1234'

#create QR code for each payment app

phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
gpay_qr=qrcode.make(gpay_url)

#save the qr code to image file(optional)

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

#display the qr codes(you may need to install PIL/Pillow)

phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()