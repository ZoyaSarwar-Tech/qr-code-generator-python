import qrcode
def generateQRCode():
    data=input("Enter text or link to generate QR code: ")
    #QR Code object
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    #Add Data
    qr.add_data(data)
    qr.make(fit=True)

    #Create Image
    img = qr.make_image(fill_color="black", back_color="white")
    #Save Image
    filename = "my_qr.png"
    img.save(filename)
    print(f"Your QR code has been generated successfully!  {filename}")
generateQRCode()
