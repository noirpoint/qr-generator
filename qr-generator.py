import qrcode
import os
import validators

correct_filename = (".png", ".jpeg")
wrong_filename = ('\\', '/', ':', '*', '?', '"', '<', '>', '|')
example_url = "Incorrect URL. Example: https://example.com"

while True:  
    link = input("Enter a link (example: https://example.com): ").strip()


    if not validators.url(link):
        print("Incorrect URL.")
        continue

    file_name = input("Enter the file name and format (e.g. qrcode.png or qrcode.jpeg): ").strip()
    
    if any(char in file_name for char in wrong_filename):
        print("File name contains prohibited characters: \\, /, :, *, ?, \", <, >, |")
        continue
        
    base, ext = os.path.splitext(file_name)
    if not ext:
        file_name += ".png"
    elif ext.lower() not in correct_filename:
        file_name = base + ".png"

    img = qrcode.make(link)
    img.save(file_name)
    print ("QR-код создан!")
    break