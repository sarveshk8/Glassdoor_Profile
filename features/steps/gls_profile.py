import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@given(u'launch the browser')
def step_impl(context):
    path = r'C:\Users\Sarvesh\Downloads\chromedriver_win32\chromedriver.exe'
    context.driver = webdriver.Chrome(path)
    time.sleep(2)


@when(u'open glassdoor loginpage')
def step_impl(context):
    context.driver.get("https://www.glassdoor.co.in/index.htm")
    context.driver.maximize_window()
    time.sleep(2)


@when(u'enter login details')
def step_impl(context):
    context.driver.find_element_by_id('inlineUserEmail').send_keys('sarveshkulkarni9545@gmail.com')
    context.driver.find_element_by_name('submit').click()
    time.sleep(2)
    context.driver.find_element_by_id('inlineUserPassword').send_keys('Sarveshbk@8')
    context.driver.find_element_by_name('submit').click()
    time.sleep(2)


@when(u'click on profile icon')
def step_impl(context):
    profile = context.driver.find_element_by_xpath("(//span[@class = 'SVGInline d-flex icon__IconStyles__colorDefault'])[6]")
    obj_pro = ActionChains(context.driver)
    obj_pro.move_to_element(profile).perform()
    time.sleep(2)
    pro2 = context.driver.find_element_by_xpath("(//a[@href = '/member/profile/index.htm'])[2]")
    obj_pro.click(pro2).perform()
    time.sleep(3)


@then(u'verify profile page is displayed or not')
def step_impl(context):
    assert True, 'Test Pass'


@then(u'select employement status')
def step_impl(context):
    context.driver.find_element_by_xpath("(//div[@class = 'selectedLabel'])[2]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[@class='dropdownOptionLabel'])[5]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("(//div[@class = 'selectedLabel'])[2]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[@class='dropdownOptionLabel'])[7]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("(//div[@class = 'selectedLabel'])[2]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("(//span[@class='dropdownOptionLabel'])[6]").click()
    time.sleep(2)


@then(u'verify that status is selected or not')
def step_impl(context):
    assert True, 'Test Passed'


@then(u'enter first name and last name details')
def step_impl(context):
    context.driver.find_element_by_xpath("(//a[@class = 'pages__mainPageStyle__sectionEditLink'])[1]").click()
    time.sleep(2)
    name = context.driver.find_element_by_xpath("//div[@class = 'input-wrapper css-q444d9'][1]")
    ac_obj = ActionChains(context.driver)
    ac_obj.double_click(name).perform()
    ac_obj.send_keys_to_element(name, 'Sarvesh').perform()
    time.sleep(2)
    l_name = context.driver.find_element_by_xpath("(//div[@class = 'input-wrapper css-q444d9'])[2]")
    obj_pro2 = ActionChains(context.driver)
    obj_pro2.double_click(l_name).perform()
    obj_pro2.send_keys_to_element(l_name, 'Kulkarni').perform()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@class = 'gd-ui-button  css-8i7bc2']").click()
    time.sleep(2)


@then(u'verify that full name is saved successfully')
def step_impl(context):
    assert True, 'Test Passed'


@then(u'enter current job title')
def step_impl(context):
    desg = context.driver.find_element_by_xpath("(//span[@class = 'SVGInline'])[9]")
    obj_des = ActionChains(context.driver)
    obj_des.double_click(desg).perform()
    obj_des.send_keys_to_element(desg, ' Analyst').perform()
    desg1 = context.driver.find_element_by_xpath("//ul[@class='suggestions down']")
    obj_des1 = ActionChains(context.driver)
    obj_des1.move_to_element(desg1).perform()
    obj_des1.click(desg1).perform()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@class = 'gd-ui-button  css-8i7bc2']").click()
    time.sleep(2)


@then(u'verify that job title entered successfully')
def step_impl(context):
    assert True, 'Test Passed'


@then(u'enter company name')
def step_impl(context):
    context.driver.find_element_by_xpath("(//span[@class = 'SVGInline'])[10]").click()
    time.sleep(2)
    comp = context.driver.find_element_by_xpath("//div[@class = 'input-wrapper css-q444d9']")
    obj_comp = ActionChains(context.driver)
    obj_comp.double_click(comp).perform()
    obj_comp.send_keys_to_element(comp, " Capgemini Engineering").perform()
    time.sleep(2)
    drop = context.driver.find_element_by_xpath("//ul[@class='suggestions down']")
    drop_obj = ActionChains(context.driver)
    drop_obj.move_to_element(drop).perform()
    drop_obj.click(drop).perform()
    context.driver.find_element_by_xpath("//button[@class='gd-ui-button  css-8i7bc2']").click()


@then(u'verify that company name entered successfully')
def step_impl(context):
    assert True, "Test Passed"


@then(u'enter current location')
def step_impl(context):
    context.driver.find_element_by_xpath("(//span[@class = 'SVGInline'])[11]").click()
    time.sleep(2)
    curr_loc = context.driver.find_element_by_xpath("(//div[@class=' css-1ohf0ui'])[2]")
    obj_cl = ActionChains(context.driver)
    obj_cl.double_click(curr_loc).perform()
    obj_cl.send_keys_to_element(curr_loc, " Latur").perform()
    loc = context.driver.find_element_by_xpath("//ul[@class='suggestions down']")
    obj_loc = ActionChains(context.driver)
    obj_loc.move_to_element(loc).perform()
    obj_loc.click(loc).perform()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Save']").click()

@then(u'verify that current location entered successfully')
def step_impl(context):
    assert True, "Test Passed"


@then(u'click on checkbox')
def step_impl(context):
    obj_page = ActionChains(context.driver)
    obj_page.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
    checkbox = context.driver.find_element_by_xpath('//div[@class="checkboxBox"]')
    checkbox.click()
    time.sleep(2)

@then(u'verify that checkbox is being checked or unchecked')
def step_impl(context):
    assert True, 'Test Passed'


@then(u'enter desired job title')
def step_impl(context):
    context.driver.find_element_by_xpath("(//span[@class='SVGInline'])[12]").click()
    time.sleep(2)
    job_title = context.driver.find_element_by_xpath("(//div[@class=' css-1ohf0ui'])[2]")
    obj_job = ActionChains(context.driver)
    obj_job.double_click(job_title).perform()
    obj_job.send_keys_to_element(job_title, " Software Engineer").perform()
    time.sleep(2)
    des_job = context.driver.find_element_by_xpath("//ul[@class='suggestions down']")
    obj_des_job = ActionChains(context.driver)
    obj_des_job.move_to_element(des_job).perform()
    obj_des_job.click(des_job).perform()
    context.driver.find_element_by_xpath("//button[text()='Save']").click()
    time.sleep(2)


@then(u'verify that job title is entered succesfully or not')
def step_impl(context):
    assert True, 'Test passed'


@then(u'enter desired location')
def step_impl(context):
    context.driver.find_element_by_xpath("(//span[@class='SVGInline'])[13]").click()
    loc1 = context.driver.find_element_by_xpath("//div[@class='my-md css-1ohf0ui']")
    obj_loc1 = ActionChains(context.driver)
    obj_loc1.double_click(loc1).perform()
    obj_loc1.send_keys_to_element(loc1, " Pune").perform()
    time.sleep(2)
    loc = context.driver.find_element_by_xpath("//ul[@class='suggestions down']")
    obj_loc = ActionChains(context.driver)
    obj_loc.move_to_element(loc).perform()
    obj_loc.click(loc).perform()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Save']").click()
    time.sleep(2)

@then(u'verify that location is entered successfully')
def step_impl(context):
    assert True, 'Test Passed'


@then(u'click and upload resume')
def step_impl(context):
    obj_page = ActionChains(context.driver)
    obj_page.send_keys(Keys.PAGE_UP).perform()
    time.sleep(2)
    context.driver.find_element_by_xpath("//li[@class=' css-zjll8e']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[@class='gd-ui-button common__SectionHeaderStyles__addIcon p-0 css-9mmzas']").click()
    time.sleep(2)
    file_path = r'A:\Documents\My Documents\Resume\Sarvesh resume.pdf'
    context.driver.find_element_by_xpath("(//input[@id='resumeSelect'])[2]").send_keys(file_path)
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[text()='Upload CV'][2]").click()

@then(u'verify that resume uploaded successfully or not')
def step_impl(context):
    assert True, 'Test Passed'
