import requests
from lxml import html
import json
from dicttoxml import dicttoxml
from pyfutebol.utils import is_hh_mm_time


site = 'https://www.placardefutebol.com.br/'


def jogos_de_hoje(format='dict'):
    url = site
    page = requests.get(url)
    tree = html.fromstring(page.content)
    
    campeonatos = tree.xpath('//*[@id="livescore"]/a/div/div/h3/text()')
    
    divisao_por_campeonato = tree.xpath('//*[@id="livescore"]/div')
    
    resultado = []
    
    for idx, div in enumerate(divisao_por_campeonato):
        campeonato = {}
        jogos = div.xpath('.//div[contains(@class, "row")]')
        jogos_hoje = []
        
        for jogo in jogos:
            status = jogo.xpath('.//span[contains(@class,"status-name")]/text()')[0]
            times = jogo.xpath('.//div[contains(@class,"team-name")]/h5/text()')
            
            info = {}
            if (status == 'AO VIVO' or ("MIN" in status) or status == 'INTERVALO' or status == 'ENCERRADO'):
                placar = jogo.xpath('.//div[contains(@class,"match-score")]/h4/span/text()')
                info['placar'] = {times[0]: placar[0], times[1]: placar[1]},
                info['placar_resumido'] = '{} x {}'.format(*placar)
            elif (is_hh_mm_time(status)):
                info['status'] = 'EM BREVE'
                info['hora_do_jogo'] = jogo.xpath('.//span[contains(@class,"status-name")]/text()')[0]
            
            informacoes = {
                'jogo': '{} x {}'.format(times[0], times[1]),
                'status': status,
            }
            
            informacoes.update(info)
            
            jogos_hoje.append(informacoes)
        
        campeonato[campeonatos[idx]] = jogos_hoje
        resultado.append(campeonato)
        
    if (format == 'json'):
        return json.dumps(resultado)
    elif (format == 'xml'):
        return dicttoxml(resultado)
    else:
        return resultado
    
    
def jogos_ao_vivo(format='dict'):
    url = site + 'jogos-em-andamento'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    
    campeonatos = tree.xpath('//*[@id="livescore"]/a/div/div/h3/text()')
    
    divisao_por_campeonato = tree.xpath('//*[@id="livescore"]/div')
    
    resultado = []
    
    for idx, div in enumerate(divisao_por_campeonato):
        campeonato = {}
        jogos = div.xpath('.//div[contains(@class, "row")]')
        jogos_hoje = []
        for jogo in jogos:
            times = jogo.xpath('.//div[contains(@class,"team-name")]/h5/text()')
            placar = jogo.xpath('.//div[contains(@class,"match-score")]/h4/span/text()')
            jogo = {
                'jogo': '{} x {}'.format(times[0], times[1]),
                'tempo': jogo.xpath('.//span[contains(@class,"status-name")]/text()')[0],
                'placar': {times[0]: placar[0], times[1]: placar[1]},
                'placar_resumido': '{} x {}'.format(*placar)
            }
            jogos_hoje.append(jogo)
        
        campeonato[campeonatos[idx]] = jogos_hoje
        resultado.append(campeonato)
        
    if (format == 'json'):
        return json.dumps(resultado)
    elif (format == 'xml'):
        return dicttoxml(resultado)
    else:
        return resultado