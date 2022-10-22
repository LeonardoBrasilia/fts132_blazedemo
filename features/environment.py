from selenium import webdriver

# inicio
def before_all(context):   #antes de tudo
    # declarar o selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('drivers/chrome/103/chromedriver.exe')

    # maximizar a janela do navegador
    context.driver.maximize_window()

    # define uma espera máxima para todos os elementos do script
    context.driver.implicitly_wait(30)

    print("Passo A - Antes de Tudo")

# fim
def after_all(context):  #depois de tudo

    #desligar/destruir o objeto do selenium
    context.driver.quit()

    print("Passo Z - Depois de tudo")

# Bloco executado ao final de cada passo
def after_step(context,step):
    print()
