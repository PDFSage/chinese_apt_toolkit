from PIL import Image

def encode_image(image_path, data, output_path):
    """Encodes data into an image."""
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    data_index = 0
    data_len = len(data)
    
    # Add a delimiter to the data
    data += "DELIMITER"

    for row in range(height):
        for col in range(width):
            if data_index < data_len:
                pixel = list(img.getpixel((col, row)))
                for n in range(3): # R, G, B
                    if data_index < data_len:
                        pixel[n] = pixel[n] & ~1 | int(data[data_index])
                        data_index += 1
                encoded.putpixel((col, row), tuple(pixel))
            else:
                break
        if data_index >= data_len:
            break
            
    encoded.save(output_path)

def decode_image(image_path):
    """Decodes data from an image."""
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for n in range(3): # R, G, B
                binary_data += str(pixel[n] & 1)

    # Split by delimiter
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-9:] == "DELIMITER":
            return decoded_data[:-9]
            
    return ""

if __name__ == "__main__":
    # Example usage
    data_to_hide = "This is a secret message."
    binary_data_to_hide = ''.join(format(ord(i), '08b') for i in data_to_hide)
    
    encode_image("input.png", binary_data_to_hide, "output.png")
    
    decoded_message = decode_image("output.png")
    print(f"Decoded message: {decoded_message}")
