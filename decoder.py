from PIL import Image

def decode_image(encoded_image_filename):
    # First Open encoded image and convert to RGB format
    encoded_img = Image.open(encoded_image_filename).convert('RGB')
    width, height = encoded_img.size

    binary_message = ''  #answer message

    pixel_index = 0      #initialize pixel index to 0
    while True:
        x = pixel_index % width
        y = pixel_index // width
        r, g, b = encoded_img.getpixel((x, y))
        if r & 0b00000001 == 0:
            # Least significant bit is 0, add 0 to binary message
            binary_message += '0'
        else:
            # Least significant bit is 1, add 1 to binary message
            binary_message += '1'
        pixel_index += 1
        # Check for delimiter at end of message
        if binary_message[-8:] == '00000000':
            break

    # Now Convert binary message to string
    message = ''
    for i in range(0, len(binary_message)-8, 8):
        message += chr(int(binary_message[i:i+8], 2))

    return message

#taking encoded image as an input
encoded_image_filename = input("Enter image path: ")

#caling decoding function
message = decode_image(encoded_image_filename)

#print output message 
print(f'Decoded message: {message}')