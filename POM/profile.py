from Data import reading_object
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
gls_object = reading_object.read_locators()


class Profile:

    def __init__(self,driver):
        self.driver = driver

# Entering username
    def enter_username(self,data_):
        self.driver.find_element(*gls_object['txt_username']).send_keys(data_[0])

# clicking on next button
    def click_next(self):
        self.driver.find_element(*gls_object['button_next']).click()

# Entering password
    def enter_pass(self,data_):
        self.driver.find_element(*gls_object['txt_password']).send_keys(data_[1])

# Clicking on login
    def click_login(self):
        self.driver.find_element(*gls_object['button_sub']).click()

# Entering into profile section
    def profile_icon(self):
        prof_icn = self.driver.find_element(*gls_object['prof_icon'])
        obj_prof = ActionChains(self.driver)
        obj_prof.move_to_element(prof_icn).perform()
        prof = self.driver.find_element(*gls_object['profil_option'])
        obj_prof1 = ActionChains(self.driver)
        obj_prof1.click(prof).perform()

# Select job status
    def job_status(self):
        self.driver.find_element(*gls_object['job_status_dropdown']).click()
        self.driver.find_element(*gls_object['job_stat']).click()
        self.driver.find_element(*gls_object['job_status_dropdown']).click()
        self.driver.find_element(*gls_object['job_status1']).click()
        self.driver.find_element(*gls_object['job_status_dropdown']).click()
        self.driver.find_element(*gls_object['job_status']).click()

# Enter first name and last name
    def name(self,data_):
        self.driver.find_element(*gls_object['name_edit']).click()
        firstname = self.driver.find_element(*gls_object['fname_txt'])
        obj_firstname = ActionChains(self.driver)
        obj_firstname.double_click(firstname).perform()
        obj_firstname.send_keys_to_element(firstname,data_[2]).perform()
        lastname = self.driver.find_element(*gls_object['lname_txt'])
        obj_lastname = ActionChains(self.driver)
        obj_lastname.double_click(lastname).perform()
        obj_lastname.send_keys_to_element(lastname,data_[3]).perform()
        self.driver.find_element(*gls_object['save_btn']).click()

# Enter current job role
    def job_role(self,data_):
        self.driver.find_element(*gls_object['job_role_current']).click()
        job_role = self.driver.find_element(*gls_object['curr_job'])
        obj_job_role = ActionChains(self.driver)
        obj_job_role.double_click(job_role).perform()
        obj_job_role.send_keys_to_element(job_role,data_[4]).perform()
        sugg = self.driver.find_element(*gls_object['sugg_list'])
        obj_sugg = ActionChains(self.driver)
        obj_sugg.click(sugg).perform()
        self.driver.find_element(*gls_object['save_btn1']).click()

# Enter your current company details
    def company(self,data_):
        self.driver.find_element(*gls_object['curr_company']).click()
        curr_com = self.driver.find_element(*gls_object['company_name'])
        obj_curr_com = ActionChains(self.driver)
        obj_curr_com.double_click(curr_com).perform()
        obj_curr_com.send_keys_to_element(curr_com,data_[5]).perform()
        sugg_comp = self.driver.find_element(*gls_object['sugg_list1'])
        obj_sug_comp = ActionChains(self.driver)
        obj_sug_comp.click(sugg_comp).perform()
        self.driver.find_element(*gls_object['save_btn2']).click()

# Enter current location details
    def current_location(self,data_):
        self.driver.find_element(*gls_object['curr_loc']).click()
        curr_loca = self.driver.find_element(*gls_object['curr_loca'])
        obj_curr_loc = ActionChains(self.driver)
        obj_curr_loc.double_click(curr_loca).perform()
        obj_curr_loc.send_keys_to_element(curr_loca,data_[6]).perform()
        sugg_loc = self.driver.find_element(*gls_object['sugg_list2'])
        obj_sugg_loc = ActionChains(self.driver)
        obj_sugg_loc.move_to_element(sugg_loc).perform()
        obj_sugg_loc.click(sugg_loc).perform()
        self.driver.find_element(*gls_object['save_btn3']).click()

# Checkbox for open to remote work
    def checkbox(self):
        obj_page = ActionChains(self.driver)
        obj_page.send_keys(Keys.PAGE_DOWN).perform()
        checkbox = self.driver.find_element(*gls_object['checkbox'])
        obj_checkbox = ActionChains(self.driver)
        obj_checkbox.click(checkbox).perform()

# Enter desired job profile
    def des_job(self, data_):
        self.driver.find_element(*gls_object['des_job_title']).click()
        job_t = self.driver.find_element(*gls_object['des_job'])
        obj_job_t = ActionChains(self.driver)
        obj_job_t.double_click(job_t).perform()
        obj_job_t.send_keys_to_element(job_t,data_[7]).perform()
        sugg_des_job = self.driver.find_element(*gls_object['sugg_list3'])
        obj_sugg = ActionChains(self.driver)
        obj_sugg.move_to_element(sugg_des_job).perform()
        obj_sugg.click(sugg_des_job).perform()
        self.driver.find_element(*gls_object['save_btn4']).click()

# Enter desired location
    def des_loc(self, data_):
        self.driver.find_element(*gls_object['des_loc_edit']).click()
        des_loca = self.driver.find_element(*gls_object['des_loc'])
        obj_de_loc = ActionChains(self.driver)
        obj_de_loc.double_click(des_loca).perform()
        obj_de_loc.send_keys_to_element(des_loca, data_[8]).perform()
        sugg_loc = self.driver.find_element(*gls_object['sugg_list4'])
        obj_sgg = ActionChains(self.driver)
        obj_sgg.move_to_element(sugg_loc).perform()
        obj_sgg.click(sugg_loc).perform()
        self.driver.find_element(*gls_object['save_btn5']).click()

# Upload resume
    def cvs(self, data_):
        self.driver.find_element(*gls_object['cvs']).click()
        resume = self.driver.find_element(*gls_object['add']).click()
        obj_resume = ActionChains(self.driver)
        obj_resume.send_keys_to_element(resume,data_[9]).perform()
        self.driver.find_element(*gls_object['upload']).click()


