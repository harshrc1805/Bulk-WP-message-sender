import pandas as pd
import pywhatkit as kit
import time

# Function to send WhatsApp image
def send_whatsapp_image(name, phone_number,image_path):
    
    # Send WhatsApp image with caption (instant send)
    try:
        kit.sendwhats_image(f"+{phone_number}", image_path, tab_close=True)
        print(f"Image sent to {name} at {phone_number}")
        time.sleep(8)  # wait to avoid rate limits
    except Exception as e:
        print(f"Failed to send image to {name} at {phone_number}: {e}")

# Read the Excel file and send images
def send_marks_with_image(file_path, image_path):
    data = pd.read_excel(file_path)

    for index, row in data.iterrows():
        name = row['Name']
        phone_number = str(row['Number'])
                
        send_whatsapp_image(name, phone_number, image_path)

if __name__ == "__main__":
    excel_file_path = 'Book1.xlsx'# Your excel path here
    
    image_file_path = 'image.jpg'  # Your image path here
    
    send_marks_with_image(excel_file_path, image_file_path)
