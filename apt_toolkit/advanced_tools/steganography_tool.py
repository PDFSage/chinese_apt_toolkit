from PIL import Image

def hide_message(image_path, message):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if index < len(message):
                asc = ord(message[index])
                encoded.putpixel((col, row), (asc, g, b))
                index += 1
    encoded.save("encoded.png")
    print("Message hidden in encoded.png")

def main():
    image_path = input("Enter image path: ")
    message = input("Enter message to hide: ")
    hide_message(image_path, message)

if __name__ == "__main__":
    main()
