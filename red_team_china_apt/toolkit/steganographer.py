from PIL import Image

class Steganographer:
    def _int_to_bin(self, rgb):
        r, g, b = rgb
        return (f'{r:08b}', f'{g:08b}', f'{b:08b}')

    def _bin_to_int(self, rgb):
        r, g, b = rgb
        return (int(r, 2), int(g, 2), int(b, 2))

    def encode(self, image_path, data, output_path):
        img = Image.open(image_path)
        width, height = img.size
        
        data_binary = ''.join(format(ord(char), '08b') for char in data)
        data_len = len(data_binary)
        
        if data_len > width * height * 3:
            raise ValueError("Data is too large to hide in the image.")

        data_binary += "1111111111111110" # Delimiter

        img_data = img.load()
        data_index = 0
        
        for y in range(height):
            for x in range(width):
                r, g, b = self._int_to_bin(img_data[x, y])
                
                if data_index < data_len:
                    r = r[:-1] + data_binary[data_index]
                    data_index += 1
                if data_index < data_len:
                    g = g[:-1] + data_binary[data_index]
                    data_index += 1
                if data_index < data_len:
                    b = b[:-1] + data_binary[data_index]
                    data_index += 1
                
                img_data[x, y] = self._bin_to_int((r, g, b))
                
                if data_index >= data_len:
                    break
            if data_index >= data_len:
                break
        
        img.save(output_path)

    def decode(self, image_path):
        img = Image.open(image_path)
        width, height = img.size
        img_data = img.load()
        
        binary_data = ""
        
        for y in range(height):
            for x in range(width):
                r, g, b = self._int_to_bin(img_data[x, y])
                binary_data += r[-1]
                binary_data += g[-1]
                binary_data += b[-1]

        delimiter_index = binary_data.find("1111111111111110")
        if delimiter_index != -1:
            binary_data = binary_data[:delimiter_index]
        
        data = ""
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            if len(byte) == 8:
                data += chr(int(byte, 2))
                
        return data

if __name__ == '__main__':
    steg = Steganographer()
    # steg.encode("input.png", "This is a secret message.", "output.png")
    # message = steg.decode("output.png")
    # print(message)
