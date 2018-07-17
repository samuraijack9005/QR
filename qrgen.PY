# Import QR Code library
import qrcode
import csv



  # Create qr code instance
#for i in your_list:
qr = qrcode.QRCode(
		version = 1,
		error_correction = qrcode.constants.ERROR_CORRECT_H,
		box_size = 10,
		border = 4,
	)
	
str=input('get it barcoded')
bar=input('enter file name')
	# The data that you want to store
data = str

	# Add data
qr.add_data(data)
qr.make(fit=True)

	# Create an image from the QR Code instance
img = qr.make_image()
fname=bar+".png"
	# Save it somewhere, change the extension as needed:
img.save(fname)
