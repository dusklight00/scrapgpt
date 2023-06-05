from webscapy import Webscapy
import time

class ChatGPTWrapper:
    def __init__(self):
        self.chatbox_xpath = '/html/body/div[1]/div[2]/div/div/main/div[2]/form/div/div/textarea'
        self.next_btn_xpath = '/html/body/div[3]/div/div/div/div[2]/div/div[2]/button'
        self.next_btn_2_xpath = '/html/body/div[3]/div/div/div/div[2]/div/div[2]/button[2]'
        self.done_btn_xpath = '/html/body/div[3]/div/div/div/div[2]/div/div[2]/button[2]'
        self.submit_btn_xpath = '/html/body/div[1]/div[2]/div/div/main/div[2]/form/div/div/button'
        self.response_xpath = '/html/body/div[1]/div[2]/div/div/main/div[1]/div/div'

        self.driver = Webscapy(
            headless=False,
            undetected=True
        )
        self.load_chatgpt()
            
    def load_chatgpt(self):
        self.driver.get("https://chat.openai.com/")
        
        # Complete agreements
        self.driver.load_wait(self.next_btn_xpath)
        next_btn = self.driver.load_element(self.next_btn_xpath)
        next_btn.click()
        self.driver.load_wait(self.next_btn_2_xpath)
        next_btn_2 = self.driver.load_element(self.next_btn_2_xpath)
        next_btn_2.click()
        self.driver.load_wait(self.done_btn_xpath)
        done_btn = self.driver.load_element(self.done_btn_xpath)
        done_btn.click()

        # Wait for chatbox to laod
        self.driver.load_wait(self.chatbox_xpath)
    
    def ask(self, query):
        MAX_CONFIRMATION = 3
        CHECK_DELAY_DURATION = 2
        
        # Write in the text box
        chatbox = self.driver.load_element(self.chatbox_xpath)
        chatbox.click()
        chatbox.send_keys(query)
        
        # Submit the query
        self.driver.load_wait(self.submit_btn_xpath)
        submit_btn = self.driver.load_element(self.submit_btn_xpath)
        submit_btn.click()
        
        # Load response element
        self.driver.load_wait(self.response_xpath)
        response_elem = self.driver.load_element(self.response_xpath)
        
        # Extract response
        prev_response = ""
        confirmation = 0
        while True:
            response = response_elem.text.split(query)[-1].strip()
            if prev_response == response:
                confirmation += 1
            if confirmation == MAX_CONFIRMATION:
                break
            prev_response = response
            time.sleep(CHECK_DELAY_DURATION)
        
        return prev_response

    def close(self):
        self.driver.close()

