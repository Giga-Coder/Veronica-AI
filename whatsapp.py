import webbrowser as web
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def whatsapp(number, message):
    numb = '+91' + number
    mess = message
    open_chat = f"https://wa.me/{numb}?text={message}"
    print(open_chat)
    web.open(open_chat)
    time.sleep(15)
    # Simulate keyboard interaction to send the message
    # Replace this part with Selenium code for reliable automation

def whatsapp_group(group_id, message):
    open_chat = f"https://web.whatsapp.com/invite/{group_id}"
    web.open(open_chat)
    time.sleep(9)
    # Use Selenium to interact with WhatsApp Web and send the message

# Example usage:
whatsapp("9805224056", "Hello, how are you?")
# whatsapp_group("group_id_here", "Hello, everyone!")
