import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from datetime import datetime


def getting_data_using_bs_column():
    #getting page
    url = requests.get('http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados=&tiposAtosSelecionados=72&lblTiposAtosSelecionados=SC&tipoAtoFacet=&siglaOrgaoFacet=&anoAtoFacet=&termoBusca=&numero_ato=&tipoData=2&dt_inicio')
    soup = BeautifulSoup(url.text, "html.parser")

    print('starting using BS by_column')
    BS_start_by_column = datetime.now()

    #finding data
    grid_de_dados = soup.find_all(class_='linhaResultados')

    #getting data
    tipo_de_ato = [item.find_all('td')[0].get_text() for item in grid_de_dados]
    numero_do_ato = [item.find_all('td')[1].get_text() for item in grid_de_dados]
    orgao_unidade = [item.find_all('td')[2].get_text().replace("\n"," ") for item in grid_de_dados]
    publicacao = [item.find_all('td')[3].get_text() for item in grid_de_dados]
    ementa = [item.find_all('td')[4].get_text().replace("\n"," ") for item in grid_de_dados]

    BS_end_by_column = datetime.now()
    BS_time_by_column = BS_end_by_column - BS_start_by_column
    print('time_running_BS_by_column: ', BS_time_by_column)

    #creating DataFrame
    df_rfb_data = pd.DataFrame(
        {'tipo_de_ato': tipo_de_ato,
         'numero_do_ato': numero_do_ato,
         'orgao_unidade': orgao_unidade,
         'publicacao': publicacao,
         'ementa': ementa
        })

    #saving data as csv
    df_rfb_data.to_csv('rfb_data.csv', encoding='utf-8-sig')

def getting_data_using_bs_row():
    #getting page
    url = requests.get('http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados=&tiposAtosSelecionados=72&lblTiposAtosSelecionados=SC&tipoAtoFacet=&siglaOrgaoFacet=&anoAtoFacet=&termoBusca=&numero_ato=&tipoData=2&dt_inicio')
    soup = BeautifulSoup(url.text, "html.parser")

    print('starting using BS by_row')
    BS_start_by_row = datetime.now()

    #finding data
    grid_de_dados = soup.find_all(class_='linhaResultados')

    #getting data
    for item in grid_de_dados:
        tipo_de_ato = [item.find_all('td')[0].get_text()]
        numero_do_ato = [item.find_all('td')[1].get_text()]
        orgao_unidade = [item.find_all('td')[2].get_text().replace("\n"," ")]
        publicacao = [item.find_all('td')[3].get_text()]
        ementa = [item.find_all('td')[4].get_text().replace("\n"," ")]

    BS_end_by_row = datetime.now()
    BS_time_by_row = BS_end_by_row - BS_start_by_row
    print('time_running_BS_by_row: ', BS_time_by_row)

    #creating DataFrame
    df_rfb_data = pd.DataFrame(
        {'tipo_de_ato': tipo_de_ato,
         'numero_do_ato': numero_do_ato,
         'orgao_unidade': orgao_unidade,
         'publicacao': publicacao,
         'ementa': ementa
        })

    #saving data as csv
    df_rfb_data.to_csv('rfb_data.csv', encoding='utf-8-sig')

def getting_data_using_selenium_by_column():
    # getting_data_by_selenium()
    url = 'http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados=&tiposAtosSelecionados=72&lblTiposAtosSelecionados=SC&tipoAtoFacet=&siglaOrgaoFacet=&anoAtoFacet=&termoBusca=&numero_ato=&tipoData=2&dt_inicio'
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)

    #finding data (table) and defining number of rows in that table
    grid_de_dados = driver.find_elements_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr')
    trs_of_table = len(grid_de_dados)

    # getting data, column by column:
    print('starting selenium scraping by column')
    by_columns_start = datetime.now()

    tipo_de_ato = [driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[1]').text for
                     tr in range(1, trs_of_table)]
    numero_do_ato = [driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[2]').text for
                     tr in range(1, trs_of_table)]
    orgao_unidade = [driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[3]').text for
                     tr in range(1, trs_of_table)]
    publicacao = [driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[4]').text for
                     tr in range(1, trs_of_table)]
    ementa = [driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[5]').text for
                     tr in range(1, trs_of_table)]

    by_columns_end = datetime.now()
    time_by_columns = by_columns_end-by_columns_start
    print('time_running_selenium_by_column: ', time_by_columns)

    #creating DataFrame
    df_rfb_data = pd.DataFrame(
        {'tipo_de_ato': tipo_de_ato,
         'numero_do_ato': numero_do_ato,
         'orgao_unidade': orgao_unidade,
         'publicacao': publicacao,
         'ementa': ementa
        })

    #saving data as csv
    df_rfb_data.to_csv('rfb_data.csv', encoding='utf-8-sig')

def getting_data_using_selenium_by_row():
    # getting_data_by_selenium()
    url = 'http://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?facetsExistentes=&orgaosSelecionados=&tiposAtosSelecionados=72&lblTiposAtosSelecionados=SC&tipoAtoFacet=&siglaOrgaoFacet=&anoAtoFacet=&termoBusca=&numero_ato=&tipoData=2&dt_inicio'
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)

    #finding data (table) and defining number of rows in that table
    grid_de_dados = driver.find_elements_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr')
    trs_of_table = len(grid_de_dados)

    # getting data, row by row
    tipo_de_ato = []
    numero_do_ato = []
    orgao_unidade = []
    publicacao = []
    ementa = []

    #accessing table row (tr)
    print('starting selenium scraping by row')
    by_row_start = datetime.now()

    for tr in range(1, trs_of_table):
        # counting number of data cell (td) in each table row (tr)
        tipo_de_ato.append(driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[1]').text)
        numero_do_ato.append(driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[2]').text)
        orgao_unidade.append(driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[3]').text)
        publicacao.append(driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[4]').text)
        ementa.append(driver.find_element_by_xpath('//*[@id="tabelaAtos"]/tbody[1]/tr[' + str(tr) + ']/td[5]').text)

    by_row_end = datetime.now()
    time_by_row = by_row_end-by_row_start
    print('time_running_selenium_by_row: ',time_by_row)

    #creating DataFrame
    df_rfb_data = pd.DataFrame(
        {'tipo_de_ato': tipo_de_ato,
         'numero_do_ato': numero_do_ato,
         'orgao_unidade': orgao_unidade,
         'publicacao': publicacao,
         'ementa': ementa
        })

    #saving data as csv
    df_rfb_data.to_csv('rfb_data.csv', encoding='utf-8-sig')

def main():
    options = input("Options:"
                    "\n ------------------------------------------------------------"
                    "\n 01: For running BeautifulSoup (BS) scraping column by column"
                    "\n 02: For running BeautifulSoup (BS) scraping row by row"
                    "\n 03: For running Selenium scraping column by column"
                    "\n 04: For running Selenium scraping row by row"
                    "\n 05: For running all possibilities"
                    "\n ------------------------------------------------------------"
                    "\n For choose, write a number and press enter >>>: ")

    if options == '01':
        getting_data_using_bs_column()
    elif options == '02':
        getting_data_using_bs_row()
    elif options == '03':
        getting_data_using_selenium_by_column()
    elif options == '04':
        getting_data_using_selenium_by_row()
    elif options == '05':
        getting_data_using_bs_column()
        getting_data_using_bs_row()
        getting_data_using_selenium_by_column()
        getting_data_using_selenium_by_row()

if __name__ == '__main__':
    main()




