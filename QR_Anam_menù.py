import qrcode

# contenuto qr.
    # Genera i nostri 5 oggetti casuali
def generate_and_save_qr_code():
    Menù = "https://drive.google.com/file/d/1tRy66famQndBxHlQVLHW7NLRoZqjPZQU/view?usp=sharing"
    print(Menù)

    # Genera il QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(Menù)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"Menù_anam.png")

# genera e salva il nostro qr code
generate_and_save_qr_code()

