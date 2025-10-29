import cv2

def spoof_fingerprint(image_path):
    # In a real scenario, you would use a more sophisticated method
    img = cv2.imread(image_path)
    cv2.imshow("Fingerprint", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image_path = input("Enter path to fingerprint image: ")
    spoof_fingerprint(image_path)

if __name__ == "__main__":
    main()
