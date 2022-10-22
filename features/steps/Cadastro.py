from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico em Register')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Register').click()


@then(u'vejo o formulario de cadastro')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Register'

@when(u'preencho "<nome>" "<empresa>" "<email>" "<senha>"')
def step_impl(context):
    context.driver.find_element(By.ID, 'name').send_keys('Ze Zin')
    context.driver.find_element(By.ID, 'company').send_keys('Telecom')
    context.driver.find_element(By.ID, 'email').send_keys('ze@zim.com')
    context.driver.find_element(By.ID, 'password').send_keys('1234')
    context.driver.find_element(By.ID, 'password-confirm').send_keys('1234')

@when(u'clico no botao Register')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

@then(u'exibe a confirmacao do cadastro')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'