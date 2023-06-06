from webscapy import Webscapy
import time

class ScrapGPT:
    def __init__(self, email, password):
        # Login interface xpaths
        self.login_btn_xpath = '/html/body/div[1]/div[1]/div[1]/div[4]/button[1]'
        self.email_field_xpath = '/html/body/div/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input'
        self.password_field_xpath = '/html/body/div/main/section/div/div/div/form/div[1]/div/div[2]/div/input'
        self.continue_btn_xpath = '/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button'
        self.continue_btn_2_xpath = '/html/body/div/main/section/div/div/div/form/div[3]/button'

        # Chat interface xpaths
        self.chatbox_xpath = '/html/body/div[1]/div[2]/div/div/main/div[3]/form/div/div/textarea'
        self.next_btn_xpath = '/html/body/div[3]/div/div/div/div[2]/div/div[2]/button'
        self.next_btn_2_xpath = '/html/body/div[3]/div/div/div/div[2]/div/div[2]/button[2]'
        self.done_btn_xpath = '/html/body/div[3]/div/div/div/div[2]/div/div[2]/button[2]'
        self.submit_btn_xpath = '/html/body/div[1]/div[2]/div[2]/div/main/div[3]/form/div/div/button'
        self.response_xpath = '/html/body/div[1]/div[2]/div/div/main/div[2]/div/div/div'

        self.driver = Webscapy(
            headless=False,
            undetected=True
        )
        self.load_chatgpt()
        self.login(email, password)
        self.complete_agreement()

    def complete_agreement(self):
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
    
    def load_chatgpt(self):
        self.driver.get("https://chat.openai.com/")
        self.driver.load_wait(self.login_btn_xpath)

    def login(self, email, password):
        self.driver.load_wait(self.login_btn_xpath)
        login_btn = self.driver.load_element(self.login_btn_xpath)
        login_btn.click()

        self.driver.load_wait(self.email_field_xpath)
        email_field = self.driver.load_element(self.email_field_xpath)
        email_field.send_keys(email)

        self.driver.load_wait(self.continue_btn_xpath)
        continue_btn = self.driver.load_element(self.continue_btn_xpath)
        continue_btn.click()

        self.driver.load_wait(self.password_field_xpath)
        password_field = self.driver.load_element(self.password_field_xpath)
        password_field.send_keys(password)

        self.driver.load_wait(self.continue_btn_2_xpath)
        continue_btn_2 = self.driver.load_element(self.continue_btn_2_xpath)
        continue_btn_2.click()

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

