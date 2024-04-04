import cv2
from pyzbar.pyzbar import decode

def scan_qr_code():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Decode QR codes in the frame
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            # Draw a rectangle around the QR code
            x, y, w, h = obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Print the QR code data
            print("QR Code Data:", obj.data.decode("utf-8"))

            # Save the QR code data to a text file
            with open('scanned_url.txt', 'w') as file:
                file.write(obj.data.decode("utf-8"))

        # Display the resulting frame
        cv2.imshow('QR Code Scanner', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()
