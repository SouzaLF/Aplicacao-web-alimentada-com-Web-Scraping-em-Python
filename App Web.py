#Bibliotecas importadas
import streamlit as st
import json
import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from bokeh.plotting import figure, show, output_file

#Hora
import time
import datetime
import locale

#Imagens
from PIL import Image

#imagem
image1 = Image.open('Logo da página')
#Título/ Hora e Data / Logo
st.markdown("<h1 style='text-align: left; color: #033102;'><b>Indicadores operacionais</b></h1>", unsafe_allow_html=True)
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
st.text(time.strftime('%d %B %Y - %H:%M:%Sh', time.localtime()))
'\n'
st.image(image1, caption='Monitoramento de máquinas', use_column_width=True)
'\n'

#RELATÓRIO DE OPERAÇÕES GERAIS
#DADOS CADASTRADOS
Operaçõess = {'105': 'ADUBAÇÃO/PREPARO DE SOLO', '106': 'APLIC. DE ADUBO A LANÇO', '107': 'APLIC. SEMENTE A LANCO', '108': 'Aplicação de ureia', '109': 'Aplicacao de calcario', '110': 'Aplicação dirigida', '111': 'Aplicação de desfoliante', '112': 'Aplicacao de fosfato', '113': 'Aplicação de fungicida', '114': 'Aplicacao de gesso', '115': 'Aplicação de inseticida', '116': 'Aplicação de kcl', '117': 'Aplicação de micronutrientes', '118': 'APLICAÇÃO TERRESTRE', '120': 'ARAÇÃO AIVECA', '126': 'COLHEITA DE ALGODÃO', '129': 'COLHEITA DE FEIJÃO', '131': 'COLHEITA DE MILHETO', '132': 'COLHEITA DE MILHO', '133': 'Colheita de milho Semente', '134': 'COLHEITA DE SOJA', '135': 'Colheita de soja Semente', '136': 'Colheita de sorgo', '137': 'Colheita soja terceiro', '156': "Gradagem 26'", '158': "Gradagem 30'", '159': "Gradagem 32'", '160': 'Gradagem 34"', '162': 'GRADAGEM NIVELADORA', '163': 'GRADAGEM NIVELADORA LEVE', '176': 'PLANTIO DE ALGODÃO', '177': 'Plantio de crotalaria com adubo', '178': 'Plantio de crotalaria sem adubo', '179': 'Plantio de feijao com adubo', '180': 'PLANTIO DE FEIJÃO', 
'181':'Plantio de girassol com adubo', '182': 'Plantio de girassol sem adubo', '183': 'Plantio de milheto com adubo', '184': 'PLANTIO DE MILHETO SEM ADUBO', '185': 'Plantio de milho com adubo', '187': 'Plantio de milho Semente com adubo', '190': 'PLANTIO DE SOJA', '191': 'Plantio de soja semente', '192': 'PLANTIO DE SOJA SEMENTE', '199': 'Replantio de brachiaria', '201': 'Replantio de feijão', '202': 'Replantio de girassol', '203': 'Replantio de milheto', '205': 'Replantio de soja', '206': 'Replantio de sorgo', '209': 'SUBSOLAGEM', '210': 'SUBSOLAGEM 15 a 20CM', '211': 'Subsolagem  21 a 30cm', '212': 'Subsolagem  31 a 40cm', '213': 'Terra planagem', '196': 'Plantio soja terceiro sem adubo', '214': 'TERRACEAMENTO', '119': 'Aracao', '121': 'Bordadura', '130': 'Colheita de girassol', '150': 'Dessecação', '153': 'ESCARIFICAÇÃO', '154': 'GRADAGEM', '155': 'Gradagem 24"', '157': "Gradagem 28'", '161': 'Gradagem 36"', '164': 'Incorporacao com grade', '173': 'NIVELAMENTO DE SOLO', '174': 'PLANTIO DE ADUBO', '175': 'Plantio de algodão com adubo', '186': 'PLANTIO DE MILHO', '188': 'Plantio de milho Semente sem adubo', '189': 'Plantio de Soja', '193': 'Plantio de sorgo com adubo', '194': 'Plantio de sorgo sem adubo', '195': 'Plantio soja terceiro com adubo', '197': 'Preparo de solo', '204': 'Replantio de milho', '224': 'ARRANQUIO DE SOQUEIRA', '127': 'Colheita de brachiaria', '226': 'DESTRUIÇÂO DE ALGODAO'}

Estadoss = {'1': 'PARADA', '2': 'PARADA', '3': 'PARADA', '4': 'PARADA', '7': 'PARADA', '8': 'PARADA', '9': 'PARADA', '10': 'PARADA', '15': 'PARADA', '16': 'PARADA', '17': 'PARADA', '18': 'PARADA', '21': 'PARADA', '24': 'PARADA', '25': 'PARADA', '27': 'PARADA', '31': 'PARADA', '39': 'PARADA', '40': 'PARADA', '41': 'PARADA', '42': 'PARADA', '43': 'PARADA', '46': 'PARADA', '48': 'PARADA', '105': 'TRABALHANDO', '106': 'TRABALHANDO', '107': 'TRABALHANDO', '108': 'TRABALHANDO', '109': 'TRABALHANDO', '110': 'TRABALHANDO', '111': 'TRABALHANDO', '112': 'TRABALHANDO', '113': 'TRABALHANDO', '114': 'TRABALHANDO', '115': 'TRABALHANDO', '116': 'TRABALHANDO', '117': 'TRABALHANDO', '118': 'TRABALHANDO', '120': 'TRABALHANDO', '125': 'TRABALHANDO', '126': 'TRABALHANDO', '129': 'TRABALHANDO', '131': 'TRABALHANDO', '132': 'TRABALHANDO', '133': 'TRABALHANDO', 
'134': 'TRABALHANDO', '135': 'TRABALHANDO', '136': 'TRABALHANDO', '137': 'TRABALHANDO', '138': 'TRABALHANDO', '139': 'TRABALHANDO', '140': 'TRABALHANDO', '141': 'TRABALHANDO', '142': 'TRABALHANDO', '143': 'DESCARREGANDO', '144': 'DESCARREGANDO', '145': 'DESCARREGANDO', '146': 'DESCARREGANDO', '149': 'DESLOC P/ REAB', '151': 'TRABALHANDO', '152': 'TRABALHANDO', '156': 'TRABALHANDO', '158': 'TRABALHANDO', '159': 'TRABALHANDO', '160': 'TRABALHANDO', '162': 'TRABALHANDO', '163': 'TRABALHANDO', '166': 'TRABALHANDO', '168': 'TRABALHANDO', '170': 'TRABALHANDO', '172': 'TRABALHANDO', '176': 'TRABALHANDO', '177': 'TRABALHANDO', '178': 'TRABALHANDO', '179': 'TRABALHANDO', '180': 'TRABALHANDO', 
'181': 'TRABALHANDO', '182': 'TRABALHANDO', '183': 'TRABALHANDO', '184': 'TRABALHANDO', '185': 'TRABALHANDO', '187': 'TRABALHANDO', '190': 'TRABALHANDO', '191': 'TRABALHANDO', '192': 'TRABALHANDO', '199': 'TRABALHANDO', '201': 'TRABALHANDO', '202': 'TRABALHANDO', '203': 'TRABALHANDO', '205': 'TRABALHANDO', '206': 'TRABALHANDO', '207': 'TRABALHANDO', '209': 'TRABALHANDO', '210': 'TRABALHANDO', '211': 'TRABALHANDO', '212': 'TRABALHANDO', '213': 'TRABALHANDO', '33': 'PARADA', '196': 'TRABALHANDO', '214': 'TRABALHANDO', '215': 'TRABALHANDO', '49': 'PARADA', 
'225': 'PARADA', '102': 'PARADA', '219': 'DESLOC P/ DESC', '220': 'MANOBRA', '5': 'PARADA', '6': 'PARADA', '11': 'PARADA', '12': 'PARADA', '13': 'PARADA', '14': 'PARADA', '19': 'PARADA', '20': 'PARADA', '22': 'PARADA', '23': 'PARADA', '26': 'PARADA', '28': 'PARADA', '29': 'PARADA', '30': 'PARADA', '32': 'PARADA', '36': 'PARADA', '44': 'PARADA', '45': 'PARADA', '47': 'PARADA', '101': 'TRABALHANDO', '103': 'TRABALHANDO', '104': 'TRABALHANDO', '119': 'TRABALHANDO', '121': 'TRABALHANDO', '122': 'TRABALHANDO', '123': 'TRABALHANDO', '124': 'TRABALHANDO', '128': 'TRABALHANDO', '130': 'TRABALHANDO', '147': 'TRABALHANDO', '148': 'DESLOC P/ DESC', '150': 'TRABALHANDO', '153': 'TRABALHANDO', '154': 'TRABALHANDO', '155': 'TRABALHANDO', '157': 'TRABALHANDO', '161': 'TRABALHANDO', '164': 'TRABALHANDO', '165': 'TRABALHANDO', '169': 'TRABALHANDO', '171': 'TRABALHANDO', '173': 'TRABALHANDO', '174': 'TRABALHANDO', '175': 'TRABALHANDO', '186': 'TRABALHANDO', '188': 'TRABALHANDO', '189': 'TRABALHANDO', '193': 'TRABALHANDO', '194': 'TRABALHANDO', '195': 'TRABALHANDO', '197': 'TRABALHANDO', '198': 'TRABALHANDO', '200': 'TRABALHANDO', '204': 'TRABALHANDO', '208': 'TRABALHANDO', '216': 'TRABALHANDO', '223': 'PARADA', '224': 'TRABALHANDO', '221': 'PARADA', '34': 'PARADA', '35': 'PARADA', '37': 'PARADA', '38': 'PARADA', '127': 'TRABALHANDO', '222': 'DESLOCAMENTO', '217': 'PARADA', '218': 'PARADA', '226': 'TRABALHANDO', '230': 'PARADA', '231': 'PARADA', '240': 'TRABALHANDO', '50': 'PARADA', '51': 'PARADA', '402': 'TRABALHANDO', '300': 'PARADA', '241': 'TRABALHANDO', '1234': 'EFETIVO', '228': 'TRABALHANDO'}

Operações_todas = {'1': '1 - Final de expediente', '2': '2 - Refeição', '3': '3 - Manutencao inicial/Check List', '4': '4 - Manutencao mecanica', '7': '7 - Implemento quebrado', '8': '8 - Lavagem/Descontaminação de tanque', '9': '9 - Lavagem equipamento', '10': '10 - Regulagem de maquina ', 
'15': '15 - Falta de semente', '16': '16 - Falta defensivo', '17': '17 - Desembuchamento de máquina', '18': '18 - Aguardando manutenção', '21': '21 - Aguardando dessecacao', '24': '24 - Aguardando areas', '25': '25 - Aguardando abastecimento', '27': '27 - Problemas hidraulicos', 
'31': '31 - Bombeiro parado para plantao/incendio', '39': '39 - Condicoes climaticas chuva', '40': '40 - Condicoes climaticas ', '41': '41 - Atualização/Manutenção/Teste de Software', '42': '42 - Condicoes climaticas temperatura', '43': '43 - Solo úmido', 
'46': '46 - Apoio a campo com equipamento parado', '48': '48 - Treinamento', '105': '105 - APLICAÇÃO DE CALCARIO', '106': '106 - APLIC. DE ADUBO A LANÇO', '107': '107 - APLIC. SEMENTE A LANCO', '108': '108 - Aplicação de ureia', '109': '109 - Aplicacao de calcario', '110': '110 - Aplicação dirigida', '111': '111 - Aplicação de desfoliante', '112': '112 - Aplicacao de fosfato', '113': '113 - Aplicação de fungicida', '114': '114 - Aplicacao de gesso', '115': '115 - Aplicação de inseticida', '116': '116 - Aplicação de kcl', '117': '117 - Aplicação de micronutrientes', '118': '118 - APLICAÇÃO TERRESTRE', '120': '120 - ARAÇÃO AIVECA', '125': '125 - COLHEITA - BAZUCA', '126': '126 - COLHEITA DE ALGODÃO', '129': '129 - COLHEITA DE FEIJÃO', '131': '131 - COLHEITA DE MILHETO', '132': '132 - COLHEITA DE MILHO', '133': '133 - Colheita de milho Semente', '134': '134 - COLHEITA DE SOJA', '135': '135 - Colheita de soja Semente', '136': '136 - Colheita de sorgo', '137': '137 - Colheita soja terceiro', '138': '138 - Combate a incendio', '139': '139 - Compactacao estrada com rolo compactador', '140': '140 - Construcao de carreadores', 
'141': '141 - Construcao de curvas de niveis', '142': '142 - Desbrota', '143': '143 - Descarga graneleiro - Colheita', '144': '144 - Descarregamento de adubo', '145': '145 - Descarregamento de grãos', '146': '146 - Descarregamento de semente plantio', '149': '149 - DESLOCAMENTO P/ REABASTECIMENTO INSUMO', '151': '151 - Emblocamento de sementes', '152': '152 - Enleiramento', '156': "156 - Gradagem 26'", '158': "158 - Gradagem 30'", '159': "159 - Gradagem 32'", '160': '160 - Gradagem 34"', '162': '162 - GRADAGEM NIVELADORA', '163': '163 - GRADAGEM NIVELADORA LEVE', '166': '166 - Limpeza de sede', '168': '168 - Manut de carreadores', '170': '170 - TRANSPORTE DE GRÃOS', '172': '172 - NIVELAMENTO COM CORRENTÃO', '176': '176 - PLANTIO DE ALGODÃO', '177': '177 - Plantio de crotalaria com adubo', '178': '178 - Plantio de crotalaria sem adubo', '179': '179 - Plantio de feijao com adubo', '180': '180 - PLANTIO DE FEIJÃO', '181': '181 - Plantio de girassol com adubo', 
'182': '182 - Plantio de girassol sem adubo', '183': '183 - Plantio de milheto com adubo', '184': '184 - PLANTIO DE MILHETO SEM ADUBO', '185': '185 - Plantio de milho com adubo', '187': '187 - Plantio de milho Semente com adubo', '190': '190 - PLANTIO DE SOJA', '191': '191 - Plantio de soja semente', 
'192': '192 - PLANTIO DE SOJA SEMENTE', '199': '199 - Replantio de brachiaria', '201': '201 - Replantio de feijão', 
'202': '202 - Replantio de girassol', '203': '203 - Replantio de milheto', '205': '205 - Replantio de soja', '206': '206 - Replantio de sorgo', '207': '207 - Roçadeira', '209': '209 - SUBSOLAGEM', '210': '210 - SUBSOLAGEM 15 a 20CM', '211': '211 - Subsolagem  21 a 30cm', '212': '212 - Subsolagem  31 a 40cm', '213': '213 - Terra planagem', '33': '33 - Abastecimento de insumos', '196': '196 - Plantio soja terceiro sem adubo', '214': '214 - TERRACEAMENTO', '215': '215 - Teste equipamento/implemento em movimento', '49': '49 - Banheiro', '225': '225 - Descarregamento graneleiro colheita', '102': '102 - Abastecimento / Lubrificação', '219': '219 - DESLOCAMENTO P/ DESCARGA COLHEITA', '220': '220 - Manobra', '5': '5 - Manutencao terceirizada', '6': '6 - Equipamento quebrado', '11': '11 - Regulagem de implemento', '12': '12 - Falta de combustivel/lubrificante', '13': '13 - Falta de insumo', '14': '14 - Falta de agua', '19': '19 - Aguardando ponto de maturação', '20': '20 - Aguardando apoio', 
'22': '22 - Aguardando troca de implemento', '23': '23 - Aguardando ordens', '26': '26 - Problemas elétricos ', '28': '28 - Problemas no abastecedor', '29': '29 - Atolamento', '30': '30 - Falta de sinal do piloto', '32': '32 - Abastecimento de combustivel', '36': '36 - Troca de faca picador', '44': '44 - Troca do kit de plantio', '45': '45 - Falta de caminhão', '47': '47 - Finalização da colheita para inicio de plantio', '101': '101 - Abast de agua area de vivencia', '103': '103 - Abertura de estradas / quebra de monte cascalho', '104': '104 - Aceiro mecanizado', '119': '119 - Aracao', '121': '121 - Bordadura', '122': '122 - Carregamento de adubo', '123': '123 - Carregamento de equip. E pecas', '124': '124 - Coleta de lixo', '128': '128 - Colheita de crotalaria', '130': '130 - Colheita de girassol', '147': '147 - Desembarque de bag', 
'148': '148 - DESLOCAMENTO P/ DESCARGA COLHEITA', '150': '150 - Dessecação', '153': '153 - ESCARIFICAÇÃO', '154': '154 - GRADAGEM', '155': '155 - Gradagem 24"', '157': "157 - Gradagem 28'", '161': '161 - Gradagem 36"', '164': '164 - Incorporacao com grade', 
'165': '165 - Limpeza de retiro', '169': '169 - Molhagem de patio/estr./terrapla', '171': '171 - Movimentacao de terra/ cascalho', '173': '173 - NIVELAMENTO DE SOLO', '174': '174 - PLANTIO DE ADUBO', '175': '175 - Plantio de algodão com adubo', '186': '186 - PLANTIO DE MILHO', '188': '188 - Plantio de milho Semente sem adubo', '189': '189 - Plantio de Soja', '193': '193 - Plantio de sorgo com adubo', '194': '194 - Plantio de sorgo sem adubo', '195': '195 - Plantio soja terceiro com adubo', '197': '197 - Preparo de solo', '198': '198 - Reforma de curva de nivel', '200': '200 - Replantio de crotalaria', '204': '204 - Replantio de milho', '208': '208 - Rocagem patio', '216': '216 - Transporte de cascalho', '223': '223 - CB Desligado', '224': '224 - ARRANQUIO DE SOQUEIRA', '221': '221 - Parada P/ Abastec Insumos', '34': '34 - Abastecimento de sementes', 
'35': '35 - Troca de faca com base', '37': '37 - Limpeza de Discos/Botinhas', '38': '38 - Limpeza de Pontas', '127': '127 - Colheita de brachiaria', '222': '222 - DESLOCAMENTO', '217': '217 - Sem Apontamento', '218': '218 - Indeterminado', '226': '226 - DESTRUIÇÂO DE ALGODAO', '230': '230 - Abertura/fechamento de barras', '231': '231 - Manutenção', '240': '240 - BOMBEIRO', '50': '50 - Aguardando Colhedora', '51': '51 - Abastecimento de Água', '402': '402 - APOIO / ABASTECIMENTO', '300': '300 - Manutenção', '241': '241 - TRANSPORTE DE ALGODÃO', '1234': '1234 - 1234', '228': '228 - TRITURAMENTO '}

Equipamentoss = {1:'Lista atualizada dos equipamentos'}

Funcionarioss = {1:'Lista atualizada dos funcionários'}

Operações_todas = pd.DataFrame(list(Operações_todas.items()),
                columns=['CD_OPERACAO', 'Operações_gerais'])
Estadoss = pd.DataFrame(list(Estadoss.items()),
                columns=['CD_OPERACAO', 'Estado'])
Operaçõess = pd.DataFrame(list(Operaçõess.items()),
                columns=['CD_OPERACAO', 'Nome_Operação'])
Equipamentoss = pd.DataFrame(list(Equipamentoss.items()),
                columns=['CD_EQUIPAMENTO', 'Nome_Equipamento'])
Funcionarioss = pd.DataFrame(list(Funcionarioss.items()),
                columns=['CD_OPERADOR', 'Nome_Operador'])
Funcionarioss[['CD_OPERADOR']] = Funcionarioss[['CD_OPERADOR']].apply(pd.to_numeric)

#Menu
st.sidebar.markdown("<h1 style='text-align: center; color: #011901;'>Menu</h1>", unsafe_allow_html=True)

#Filtros datas
'\n'
today = datetime.date.today()
d3 = st.date_input('Informe o período para análise. Ex: (Ano/ mês/ dia)', [today, today])
intervalo = d3[0] + datetime.timedelta(days = 7)

#Condição de erro para data
if d3[0]>today or d3[1]>today :
    st.error('Erro: Dados para datas futuras ainda serão gerados')
elif d3[1] > intervalo:
    st.error('Erro: Intervalo máximo permitido é de 7 dias.\n\n Faça um novo filtro para data')

elif d3[0] <= d3[1] and d3[1] <= intervalo:
    data1 = (d3[0].strftime("%d/%m/%Y"))
    d1 = data1+" "+"00:00:00"
    data2 = (d3[1].strftime("%d/%m/%Y"))
    d2 = data2+" "+"23:59:59"
    st.success('Data inicial: `%s`\n\nData final: `%s`' % (d1, d2))

    #CONSUMINDO API
    url = 'Url API'
    payload = {"cliente": "Cliente", "password": "Password"}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    #print(r.status_code)
    token = (r.json())['token']
    headers_token = {'X-Auth-Token': token,
                    'Content-Type':'application/json'}
    Body = { "id": 22
            , "page" : 0
            , "parameters" : { "dataini" : d1
            , "datafim" : d2
            , "unidade" : ""
            , "equipamento" : ""
            , "operacao" : ""
            , "operador" : ""
            , "talhao" : ""
            , "ordemservico" : "" }
            }
    response = requests.post('Url integração', 
                            data=json.dumps(Body), headers=headers_token)
    novo_token = (json.loads(response.content))['token']
    resposta = (json.loads(response.content))['resultado']
    size = int(resposta['size'])
    dados_req = (pd.DataFrame(resposta['content'])) #tabela com dados
    cont=0
    while size<=1000:
        if size>0 and size<=1000:
                cont+=1
                headers_token = {'X-Auth-Token': novo_token,
                        'Content-Type':'application/json'}

                Body = {"id": 22
                        , "page" : cont
                        , "parameters" : { "dataini" : d1
                        , "datafim" : d2
                        , "unidade" : ""
                        , "equipamento" : ""
                        , "operacao" : ""
                        , "operador" : ""
                        , "talhao" : ""
                        , "ordemservico" : ""}
                        }
                response1 = requests.post('Url integração', 
                                data=json.dumps(Body), headers=headers_token)
                novo_token = (json.loads(response1.content))['token']
                resposta1 = (json.loads(response1.content))['resultado']
                size = int(resposta1['size'])
                tabela2 = pd.DataFrame(resposta1['content'])
                dados_req = (dados_req.append(tabela2)).fillna(0)
        elif size==0:
                cont=0
                break

    #Tratamento dos dados    
    dados_req['VL_CONSUMO']= (dados_req['VL_CONSUMO'].replace([-1],0))
    dados_req['Rendimento (ha/h)'] = (dados_req['VL_AREA_HECTARES_EQUIPAMENTO']/(dados_req['VL_TEMPO_PRODUTIVO']/3600)).replace([np.inf, -np.inf], np.nan)
    dados_req['Consumo (L/Ha)'] = (dados_req['VL_CONSUMO']/dados_req['VL_AREA_HECTARES_EQUIPAMENTO']).replace([np.inf, -np.inf], np.nan)
    dados_req['Tempo efetivo (h)'] = (dados_req['VL_TEMPO_EFETIVO']/3600)
    dados_req = dados_req.join(Funcionarioss.set_index('CD_OPERADOR'), on='CD_OPERADOR', how='left')
    dados_req = dados_req.join(Operaçõess.set_index('CD_OPERACAO'), on='CD_OPERACAO', how='left')
    dados_req = dados_req.join(Estadoss.set_index('CD_OPERACAO'), on='CD_OPERACAO', how='left')
    dados_req = dados_req.join(Operações_todas.set_index('CD_OPERACAO'), on='CD_OPERACAO', how='left')
    dados_req = dados_req.join(Equipamentoss.set_index('CD_EQUIPAMENTO'), on='CD_EQUIPAMENTO', how='left')
    dados_req = dados_req.fillna(0)
    dados_req = dados_req.reset_index(drop=True)
    '\n'
    '\n'

    if st.checkbox('Exibir dados'):
        dados_req

    #Funtions/ gráficos
    def fazenda(filter10, filter11, y, x):   
        fig=plt.figure(figsize = None)
        plt.style.use("ggplot")
        #Retirando valores nulos
        cont=0
        index = []
        for i in filter10:
            if i<1:
                index.append(cont)
            cont+=1
        Área_trabalhada1 = np.delete(filter10, index)
        Operação1 = np.delete(filter11, index)
        plt.barh(Operação1, Área_trabalhada1, alpha=1, align='center', color='orangered')
        plt.xlabel(x, size = 14, color='black', alpha=1)
        plt.ylabel(y, size = 14, color='black', alpha=1)
        for i, v in enumerate(Área_trabalhada1):
            plt.text(v + 0.1, i, str(v), color='black', va='center', fontweight='bold', alpha=1)
        fig.tight_layout()
        return st.pyplot(fig)
    def operacao(filter1, filter2, y, x):   
        fig=plt.figure(figsize = None)
        plt.style.use("ggplot")
        #Retirando valores nulos
        cont=0
        index = []
        for i in filter1:
            if i<1:
                index.append(cont)
            cont+=1
        Área_trabalhada1 = np.delete(filter1, index)
        Operação1 = np.delete(filter2, index)
        plt.barh(Operação1, Área_trabalhada1, alpha=1, align='center', color='orangered')
        plt.xlabel(x, size = 14, color='black', alpha=1)
        plt.ylabel(y, size = 14, color='black', alpha=1)
        for i, v in enumerate(Área_trabalhada1):
            plt.text(v + 0.1, i, str(v), color='black', va='center', fontweight='bold', alpha=1)
        fig.tight_layout()
        return st.pyplot(fig)
    def equipamento(filter3, filter4, y, x):
        fig1=plt.figure(figsize = None)
        plt.style.use("ggplot")
        #Retirando valores nulos
        cont=0
        index = []
        for i in filter3:
            if i<1:
                index.append(cont)
            cont+=1
        Área_trabalhada1 = np.delete(filter3, index)
        Equipamento1 = np.delete(filter4, index)
        plt.barh(Equipamento1, Área_trabalhada1, color="lightseagreen", alpha=1, align='center')
        plt.xlabel(x, size = 14, color='black', alpha=1)
        plt.ylabel(y, size = 14, color='black', alpha=1)
        for i, v in enumerate(Área_trabalhada1):
            plt.text(v + 0.1, i, str(v), color='black', va='center', fontweight='bold', alpha=1)
        fig1.tight_layout()
        return st.pyplot(fig1)
    def talhao(filter5, filter6, y, x):
        fig2=plt.figure(figsize = None)
        plt.style.use("ggplot")
        #Retirando valores nulos
        cont=0
        index = []
        for i in filter5:
            if i<1:
                index.append(cont)
            cont+=1
        Área_trabalhada1 = np.delete(filter5, index)
        Talhão1 = np.delete(filter6, index)
        plt.barh(Talhão1, Área_trabalhada1, color="crimson", alpha=1, align='center')
        plt.xlabel(x, size = 14, color='black', alpha=1) #Título do eixo x
        plt.ylabel(y, size = 14, color='black', alpha=1) #Título do eixo y
        for i, v in enumerate(Área_trabalhada1):
            plt.text(v + 0.1, i, str(v), color='black', va='center', fontweight='bold', alpha=1)
        fig2.tight_layout()
        return st.pyplot(fig2)
    def operador(filter7, filter8, y, x):
        fig3=plt.figure(figsize = None)
        plt.style.use("ggplot")
        #Retirando valores nulos
        cont=0
        index = []
        for i in filter7:
            if i<1:
                index.append(cont)
            cont+=1
        Área_trabalhada1 = np.delete(filter7, index)
        Operador1 = np.delete(filter8, index)
        plt.barh(Operador1, Área_trabalhada1, color="orange", alpha=1, align='center')
        plt.xlabel(x, size = 14, color='black', alpha=1)
        plt.ylabel(y, size = 14, color='black', alpha=1)
        for i, v in enumerate(Área_trabalhada1):
            plt.text(v + 0.1, i, str(v), color='black', va='center', fontweight='bold', alpha=1)
        fig3.tight_layout()
        return st.pyplot(fig3)

    #Filtros pizza
    trabalhando = dados_req['Estado']=="TRABALHANDO"
    dados_trab = dados_req[trabalhando].reset_index(drop=True)
    parada = dados_req['Estado']=="PARADA"
    dados_parada = dados_req[parada].reset_index(drop=True)
    manobra = dados_req['Estado']=="MANOBRA"
    dados_manobra = dados_req[manobra].reset_index(drop=True)
    deslocamento = dados_req['Estado']=="DESLOCAMENTO"
    dados_desloc = dados_req[deslocamento].reset_index(drop=True)
    deslocamento_rea = dados_req['Estado']=="DESLOC P/ REAB"
    dados_deslocRE = dados_req[deslocamento_rea].reset_index(drop=True)
    deslocamento_de = dados_req['Estado']=="DESLOC P/ DESC"
    dados_deslocDE = dados_req[deslocamento_de].reset_index(drop=True)
    descarregamento = dados_req['Estado']=="DESCARREGANDO"
    descargarregar = dados_req[descarregamento].reset_index(drop=True)
    
    #Pizza 1
    total_motor_ligado = (dados_req['VL_TEMPO_MOTOR_LIGADO'].sum().round(2))/3600
    perc_trab = (((dados_trab['VL_TEMPO_MOTOR_LIGADO'].sum())/3600/total_motor_ligado)*100).round(1)
    perc_parada = (((dados_parada['VL_TEMPO_MOTOR_LIGADO'].sum())/3600/total_motor_ligado)*100).round(1)
    perc_manobra = (((dados_manobra['VL_TEMPO_MOTOR_LIGADO'].sum())/3600/total_motor_ligado)*100).round(1)
    perc_desloc = (((dados_desloc['VL_TEMPO_MOTOR_LIGADO'].sum())/3600/total_motor_ligado)*100).round(1)
    perc_deslocre = (((dados_deslocRE['VL_TEMPO_MOTOR_LIGADO'].sum())/3600/total_motor_ligado)*100).round(1)
    perc_deslocde = (((dados_deslocDE['VL_TEMPO_MOTOR_LIGADO'].sum())/3600/total_motor_ligado)*100).round(1)
    descarregamento = (((descargarregar['VL_TEMPO_MOTOR_LIGADO'].sum())/3600/total_motor_ligado)*100).round(1)

    #Title graf pizza
    titulo_pizza = st.markdown("<h2 style='text-align: center; color: #033102;'><b>Tempo de motor ligado de toda a frota</b></h2>", unsafe_allow_html=True)
    ocultar = st.empty()
    ocultar0 = st.empty()
    ocultar1 = st.empty()
    ocultar2 = st.empty()
    ocultar3 = st.empty()
    
    #Gráfico de pizza
    labels = ["TRABALHANDO", 'DESLOC P/ REAB', 'PARADA', 'MANOBRA', 'DESLOCAMENTO', 'DESLOC P/ DESC', 'DESCARREGANDO']
    lista_tempo = [perc_trab, perc_deslocre, perc_parada, perc_manobra, perc_desloc, perc_deslocde, descarregamento]
    explode = [0.15, 0, 0, 0, 0, 0, 0]
    cont11=0
    index_nulo = []
    for i in lista_tempo:
        if i==0:
            index_nulo.append(cont11)
        cont11+=1
    labels = np.delete(labels, index_nulo)
    percentagem = np.delete(lista_tempo, index_nulo)
    explode = np.delete(explode, index_nulo)
    c = ['#006400', '#4169E1', '#FF0000', '#90EE90', '#FFFF00', '#FF4500', '#00CED1']
    fig159, ax1 = plt.subplots(figsize=(None))
    ax1.pie(percentagem, explode=explode, autopct='%1.1f%%',
            shadow=True, startangle=45, colors=c, pctdistance=0.6, radius=2.5)
    ax1.legend(labels,
            loc="center left",
            title="Estado operacional",
            bbox_to_anchor=(0.88,0,0.5,1))
    ax1.axis('equal')
    ocultar.pyplot(fig159)
    
    #Tempo motor ligado por estado operacional
    titulo_pizza1 = ocultar0.markdown("<h2 style='text-align: center; color: #033102;'><b>Tempo de motor ligado por equipamento</b></h2>", unsafe_allow_html=True)
    horas_ligadas = dados_req.groupby('Nome_Equipamento')['VL_TEMPO_MOTOR_LIGADO'].sum().reset_index()
    horas_ligadas['VL_TEMPO_MOTOR_LIGADO'] = horas_ligadas['VL_TEMPO_MOTOR_LIGADO']/3600
    ret_zero = horas_ligadas[horas_ligadas['VL_TEMPO_MOTOR_LIGADO'] == 0].index
    horas_ligadas.drop(ret_zero, inplace=True)
    '\n'
    sidebar1_title = ocultar1.markdown("<h5 style='text-align: left; color: #033102;'><b>Selecione o equipamento</b></h5>", unsafe_allow_html=True)
    Filtragem_equipamento = horas_ligadas
    Equipamentos_encontrado = Filtragem_equipamento['Nome_Equipamento'].unique()
    filtro_equipamento = Equipamentos_encontrado!=0
    Equipamentos_encontrado = Equipamentos_encontrado[filtro_equipamento]
    Select_equipamentos = ocultar2.selectbox("", [*list(Equipamentos_encontrado)])
    
    if horas_ligadas.empty==False:
        valor_total = float(horas_ligadas.loc[horas_ligadas['Nome_Equipamento'] == Select_equipamentos, 'VL_TEMPO_MOTOR_LIGADO'].item())
    elif horas_ligadas.empty==True:
        st.write('Não há dados para motor ligado.')

    trabalhando1 = dados_trab.groupby('Nome_Equipamento')['VL_TEMPO_MOTOR_LIGADO'].sum().reset_index()
    trabalhando1['VL_TEMPO_MOTOR_LIGADO'] = trabalhando1['VL_TEMPO_MOTOR_LIGADO']/3600
    ret_zero1 = trabalhando1[trabalhando1['VL_TEMPO_MOTOR_LIGADO'] == 0].index
    trabalhando1.drop(ret_zero1, inplace=True)
    x1=""
    for i in trabalhando1['Nome_Equipamento']:
        if i==Select_equipamentos:
            x1 = "ok"
    if trabalhando1.empty==False and x1=="ok":
        valor_trabalhando = float(trabalhando1.loc[trabalhando1['Nome_Equipamento'] == Select_equipamentos, 'VL_TEMPO_MOTOR_LIGADO'].item())
        valor_trabalhando = (valor_trabalhando/valor_total)*100
    elif trabalhando1.empty==True or x1!="ok":
        valor_trabalhando = 0

    parada1 = dados_parada.groupby('Nome_Equipamento')['VL_TEMPO_MOTOR_LIGADO'].sum().reset_index()
    parada1['VL_TEMPO_MOTOR_LIGADO'] = parada1['VL_TEMPO_MOTOR_LIGADO']/3600
    ret_zero2 = parada1[parada1['VL_TEMPO_MOTOR_LIGADO'] == 0].index
    parada1.drop(ret_zero2, inplace=True)
    x2=""
    for i in parada1['Nome_Equipamento']:
        if i==Select_equipamentos:
            x2 = "ok"
    if parada1.empty==False and x2=="ok":
        valor_parada = float(parada1.loc[parada1['Nome_Equipamento'] == Select_equipamentos, 'VL_TEMPO_MOTOR_LIGADO'].item())
        valor_parada = (valor_parada/valor_total)*100
    elif parada1.empty==True or x2!="ok":
        valor_parada = 0

    manobra1 = dados_manobra.groupby('Nome_Equipamento')['VL_TEMPO_MOTOR_LIGADO'].sum().reset_index()
    manobra1['VL_TEMPO_MOTOR_LIGADO'] = manobra1['VL_TEMPO_MOTOR_LIGADO']/3600
    ret_zero3 = manobra1[manobra1['VL_TEMPO_MOTOR_LIGADO'] == 0].index
    manobra1.drop(ret_zero3, inplace=True)
    x3=""
    for i in manobra1['Nome_Equipamento']:
        if i==Select_equipamentos:
            x3 = "ok"
    if manobra1.empty==False and x3=="ok":
        valor_manobra = float(manobra1.loc[manobra1['Nome_Equipamento'] == Select_equipamentos, 'VL_TEMPO_MOTOR_LIGADO'].item())
        valor_manobra = (valor_manobra/valor_total)*100
    elif manobra1.empty==True or x3!="ok":
        valor_manobra = 0

    deslocamento1 = dados_desloc.groupby('Nome_Equipamento')['VL_TEMPO_MOTOR_LIGADO'].sum().reset_index()
    deslocamento1['VL_TEMPO_MOTOR_LIGADO'] = deslocamento1['VL_TEMPO_MOTOR_LIGADO']/3600
    ret_zero4 = deslocamento1[deslocamento1['VL_TEMPO_MOTOR_LIGADO'] == 0].index
    deslocamento1.drop(ret_zero4, inplace=True)
    x4=""
    for i in deslocamento1['Nome_Equipamento']:
        if i==Select_equipamentos:
            x4 = "ok"
    if deslocamento1.empty==False and x4=="ok":
        valor_deslocamento = float(deslocamento1.loc[deslocamento1['Nome_Equipamento'] == Select_equipamentos, 'VL_TEMPO_MOTOR_LIGADO'].item())
        valor_deslocamento = (valor_deslocamento/valor_total)*100
    elif deslocamento1.empty==True or x4!="ok":
        valor_deslocamento = 0

    deslocamentore1 = dados_deslocRE.groupby('Nome_Equipamento')['VL_TEMPO_MOTOR_LIGADO'].sum().reset_index()
    deslocamentore1['VL_TEMPO_MOTOR_LIGADO'] = deslocamentore1['VL_TEMPO_MOTOR_LIGADO']/3600
    ret_zero5 = deslocamentore1[deslocamentore1['VL_TEMPO_MOTOR_LIGADO'] == 0].index
    deslocamentore1.drop(ret_zero5, inplace=True)
    x5=""
    for i in deslocamentore1['Nome_Equipamento']:
        if i==Select_equipamentos:
            x5 = "ok"
    if deslocamentore1.empty==False and x5=="ok":
        valor_deslocamentore = float(deslocamentore1.loc[deslocamentore1['Nome_Equipamento'] == Select_equipamentos, 'VL_TEMPO_MOTOR_LIGADO'].item())
        valor_deslocamentore = (valor_deslocamentore/valor_total)*100
    elif deslocamentore1.empty==True or x5!="ok":
        valor_deslocamentore = 0

    deslocamentode1 = dados_deslocDE.groupby('Nome_Equipamento')['VL_TEMPO_MOTOR_LIGADO'].sum().reset_index()
    deslocamentode1['VL_TEMPO_MOTOR_LIGADO'] = deslocamentode1['VL_TEMPO_MOTOR_LIGADO']/3600
    ret_zero6 = deslocamentode1[deslocamentode1['VL_TEMPO_MOTOR_LIGADO'] == 0].index
    deslocamentode1.drop(ret_zero6, inplace=True)
    x6=""
    for i in deslocamentode1['Nome_Equipamento']:
        if i==Select_equipamentos:
            x6 = "ok"
    if deslocamentode1.empty==False and x6=="ok":
        valor_deslocamentode1 = float(deslocamentode1.loc[deslocamentode1['Nome_Equipamento'] == Select_equipamentos, 'VL_TEMPO_MOTOR_LIGADO'].item())
        valor_deslocamentode1 = (valor_deslocamentode1/valor_total)*100
    elif deslocamentode1.empty==True or x6!="ok":
        valor_deslocamentode1 = 0

    descargarregar1 = descargarregar.groupby('Nome_Equipamento')['VL_TEMPO_MOTOR_LIGADO'].sum().reset_index()
    descargarregar1['VL_TEMPO_MOTOR_LIGADO'] = descargarregar1['VL_TEMPO_MOTOR_LIGADO']/3600
    ret_zero7 = descargarregar1[descargarregar1['VL_TEMPO_MOTOR_LIGADO'] == 0].index
    descargarregar1.drop(ret_zero7, inplace=True)
    x7=""
    for i in descargarregar1['Nome_Equipamento']:
        if i==Select_equipamentos:
            x7 = "ok"
    if descargarregar1.empty==False and x7=="ok":
        valor_descargarregar = float(descargarregar1.loc[descargarregar1['Nome_Equipamento'] == Select_equipamentos, 'VL_TEMPO_MOTOR_LIGADO'].item())
        valor_descargarregar = (valor_descargarregar/valor_total)*100
    elif descargarregar1.empty==True or x7!="ok":
        valor_descargarregar = 0

    #Gráfico de pizza
    labels1 = ["TRABALHANDO", 'DESLOC P/ REAB', 'PARADA', 'MANOBRA', 'DESLOCAMENTO', 'DESLOC P/ DESC', 'DESCARREGANDO']
    lista_tempo1 = [valor_trabalhando, valor_deslocamentore, valor_parada, valor_manobra, valor_deslocamento, valor_deslocamentode1, valor_descargarregar]
    explode1 = [0.15, 0, 0, 0, 0, 0, 0]
    cont11=0
    index_nulo1 = []
    for i in lista_tempo1:
        if i==0:
            index_nulo1.append(cont11)
        cont11+=1
    labels1 = np.delete(labels1, index_nulo1)
    percentagem1 = np.delete(lista_tempo1, index_nulo1)
    explode1 = np.delete(explode1, index_nulo1)
    c = ['#006400', '#4169E1', '#FF0000', '#90EE90', '#FFFF00', '#FF4500', '#00CED1']
    fig1598, ax2 = plt.subplots(figsize=(None))
    ax2.pie(percentagem1, explode=explode1, autopct='%1.1f%%',
            shadow=True, startangle=45, colors=c, pctdistance=0.6, radius=2.5)
    ax2.legend(labels1,
            loc="center left",
            title="Estado operacional",
            bbox_to_anchor=(0.88,0,0.5,1))
    ax2.axis('equal')
    ocultar3.pyplot(fig1598)

    #Filtro estado
    estado_escolher = dados_req['Estado'].unique()
    filtro_estado = estado_escolher!=0
    estado_escolher = list(estado_escolher[filtro_estado])
    estado_escolher.append("TODOS")
    options = st.sidebar.radio("Estado operacional", estado_escolher)
    if options!="TODOS":
        Filtragem = [str(options)]
        dados = dados_req[dados_req.Estado.isin(Filtragem)].reset_index(drop=True)
    if options=="TODOS":
        dados = dados_req

    #FILTROS
    if dados.empty==False and options!="TODOS":
        #Filtro operações acontecendo
        Filtragem_filtro = dados
        Operações_acontecendo = Filtragem_filtro['Operações_gerais'].unique()
        filtro = Operações_acontecendo!=0
        Operações_acontecendo = Operações_acontecendo[filtro]
        Select_operações = st.sidebar.selectbox("Operações",[*list(Operações_acontecendo)])
    if dados.empty==False and options=="TODOS":
        #Filtro operações acontecendo
        Select_operações = st.sidebar.selectbox("Operações",["TODAS OPERAÇÕES"])

    if Select_operações=="TODAS OPERAÇÕES":
        dados = dados
    if Select_operações!="TODAS OPERAÇÕES":
        Filtro_op = dados['Operações_gerais']==str(Select_operações)
        dados = dados[Filtro_op].reset_index(drop=True)

    if dados.empty==False:
        #Filtro informações
        página_selecionada = st.sidebar.selectbox("Informação desejada",["-", "Apontamentos", "Área trabalhada", "Tempo efetivo", "Rendimento médio", "Consumo geral", "Consumo médio"])
        if página_selecionada!="-":
            titulo_pizza.empty()
            ocultar.empty()
            ocultar0.empty()
            ocultar1.empty()
            ocultar2.empty()
            ocultar3.empty()
            #Desenrolo
            if página_selecionada=="Área trabalhada":
                '\n'
                '\n'
                st.markdown("<h2 style='text-align: center; color: #033102;'><b>Área trabalhada</b></h2>", unsafe_allow_html=True)
                #Fazenda
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por fazenda</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                date0 = dados.groupby('DESC_FAZENDA')['VL_AREA_HECTARES_EQUIPAMENTO'].sum().reset_index().round(2)
                filter10 = np.array(date0['VL_AREA_HECTARES_EQUIPAMENTO'])
                filter11 = np.array(date0['DESC_FAZENDA'].astype(str))
                fazenda(filter10, filter11, 'Fazenda', 'Área trabalhada (ha)')
                #TALHÃO    
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por talhão</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date3 = dados.groupby('DESC_TALHAO')['VL_AREA_HECTARES_EQUIPAMENTO'].sum().reset_index().round(2)
                filter5 = np.array(date3['VL_AREA_HECTARES_EQUIPAMENTO'])
                filter6 = np.array(date3['DESC_TALHAO'].astype(str))
                talhao(filter5, filter6, 'Talhão', 'Área trabalhada (ha)')
                #OPERACAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operação</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date1 = dados.groupby('Operações_gerais')['VL_AREA_HECTARES_EQUIPAMENTO'].sum().reset_index ().round(2)
                filter1 = np.array(date1['VL_AREA_HECTARES_EQUIPAMENTO'])
                filter2 = np.array(date1['Operações_gerais'].astype(str))
                operacao(filter1, filter2, 'Operação', 'Área trabalhada (ha)')
                #EQUIPAMENTO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por equipamento</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date2 = dados.groupby('Nome_Equipamento')['VL_AREA_HECTARES_EQUIPAMENTO'].sum().reset_index().round(2)
                filter3 = np.array(date2['VL_AREA_HECTARES_EQUIPAMENTO'])
                filter4 = np.array(date2['Nome_Equipamento'].astype(str))
                equipamento(filter3, filter4, 'Equipamento', 'Área trabalhada (ha)')
                #OPERADOR
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operador</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date4 = dados.groupby('Nome_Operador')['VL_AREA_HECTARES_EQUIPAMENTO'].sum().reset_index().round(2)
                filter7 = np.array(date4['VL_AREA_HECTARES_EQUIPAMENTO'])
                filter8 = np.array(date4[['Nome_Operador']].astype(str))
                operador(filter7, filter8, 'Operador', 'Área trabalhada (ha)')
            elif página_selecionada=="Rendimento médio":
                '\n'
                '\n'
                st.markdown("<h2 style='text-align: center; color: #033102;'><b>Rendimento médio</b></h2>", unsafe_allow_html=True)
                #Fazenda
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por fazenda</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                date0 = dados.groupby('DESC_FAZENDA')['Rendimento (ha/h)'].mean().reset_index().round(2)
                filter10 = np.array(date0['Rendimento (ha/h)'])
                filter11 = np.array(date0['DESC_FAZENDA'].astype(str))
                fazenda(filter10, filter11, 'Fazenda', 'Rendimento (ha/h)')
                #TALHAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por talhão</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date3 = dados.groupby('DESC_TALHAO')['Rendimento (ha/h)'].mean().reset_index().round(2)
                filter5 = np.array(date3['Rendimento (ha/h)'])
                filter6 = np.array(date3['DESC_TALHAO'].astype(str))
                talhao(filter5, filter6, 'Talhão', 'Rendimento (ha/h)')
                #OPERACAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operação</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date1 = dados.groupby('Operações_gerais')['Rendimento (ha/h)'].mean().reset_index ().round(2)
                filter1 = np.array(date1['Rendimento (ha/h)'])
                filter2 = np.array(date1['Operações_gerais'].astype(str))
                operacao(filter1, filter2, 'Operação', 'Rendimento (ha/h)')
                #EQUIPAMENTO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por equipamento</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date2 = dados.groupby('Nome_Equipamento')['Rendimento (ha/h)'].mean().reset_index().round(2)
                filter3 = np.array(date2['Rendimento (ha/h)'])
                filter4 = np.array(date2['Nome_Equipamento'].astype(str))
                equipamento(filter3, filter4, 'Equipamento', 'Rendimento (ha/h)')
                #OPERADOR
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operador</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date4 = dados.groupby('Nome_Operador')['Rendimento (ha/h)'].mean().reset_index().round(2)
                filter7 = np.array(date4['Rendimento (ha/h)'])
                filter8 = np.array(date4['Nome_Operador'].astype(str))
                operador(filter7, filter8, 'Operador', 'Rendimento (ha/h)')
            elif página_selecionada=="Consumo geral":
                '\n'
                '\n'
                st.markdown("<h2 style='text-align: center; color: #033102;'><b>Consumo geral</b></h2>", unsafe_allow_html=True)
                #Fazenda
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por fazenda</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                date0 = dados.groupby('DESC_FAZENDA')['VL_CONSUMO'].sum().reset_index().round(2)
                filter10 = np.array(date0['VL_CONSUMO'])
                filter11 = np.array(date0['DESC_FAZENDA'].astype(str))
                fazenda(filter10, filter11, 'Fazenda', 'Consumo (l)')
                #TALHAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por talhão</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date3 = dados.groupby('DESC_TALHAO')['VL_CONSUMO'].sum().reset_index().round(2)
                filter5 = np.array(date3['VL_CONSUMO'])
                filter6 = np.array(date3['DESC_TALHAO'].astype(str))
                talhao(filter5, filter6, 'Talhão', 'Consumo (l)')
                #OPERACAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operação</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                date1 = dados.groupby('Operações_gerais')['VL_CONSUMO'].sum().reset_index ().round(2)
                filter1 = np.array(date1['VL_CONSUMO'])
                filter2 = np.array(date1['Operações_gerais'].astype(str))
                operacao(filter1, filter2, 'Operação', 'Consumo (l)')
                #EQUIPAMENTO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por equipamento</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date2 = dados.groupby('Nome_Equipamento')['VL_CONSUMO'].sum().reset_index().round(2)
                filter3 = np.array(date2['VL_CONSUMO'])
                filter4 = np.array(date2['Nome_Equipamento'].astype(str))
                equipamento(filter3,filter4, 'Equipamento', 'Consumo (l)')
                #OPERADOR
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operador</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date4 = dados.groupby('Nome_Operador')['VL_CONSUMO'].sum().reset_index().round(2)
                filter7 = np.array(date4['VL_CONSUMO'])
                filter8 = np.array(date4['Nome_Operador'].astype(str))
                operador(filter7, filter8, 'Operador', 'Consumo (l)')
            elif página_selecionada=="Consumo médio":
                '\n'
                '\n'
                st.markdown("<h2 style='text-align: center; color: #033102;'><b>Consumo médio</b></h2>", unsafe_allow_html=True)
                #Fazenda
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por fazenda</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                date0 = dados.groupby('DESC_FAZENDA')['Consumo (L/Ha)'].mean().reset_index().round(2)
                filter10 = np.array(date0['Consumo (L/Ha)'])
                filter11 = np.array(date0['DESC_FAZENDA'].astype(str))
                fazenda(filter10, filter11, 'Fazenda', 'Consumo (l/ha)')
                #TALHAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por talhão</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date3 = dados.groupby('DESC_TALHAO')['Consumo (L/Ha)'].mean().reset_index().round(2)
                filter5 = np.array(date3['Consumo (L/Ha)'])
                filter6 = np.array(date3['DESC_TALHAO'].astype(str))
                talhao(filter5, filter6, 'Talhão', 'Consumo (l/ha)')
                #OPERACAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operação</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date1 = dados.groupby('Operações_gerais')['Consumo (L/Ha)'].mean().reset_index ().round(2)
                filter1 = np.array(date1['Consumo (L/Ha)'])
                filter2 = np.array(date1['Operações_gerais'].astype(str))
                operacao(filter1, filter2, 'Operação', 'Consumo (l/ha)')
                #EQUIPAMENTO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por equipamento</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date2 = dados.groupby('Nome_Equipamento')['Consumo (L/Ha)'].mean().reset_index().round(2)
                filter3 = np.array(date2['Consumo (L/Ha)'])
                filter4 = np.array(date2['Nome_Equipamento'].astype(str))
                equipamento(filter3,filter4, 'Equipamento', 'Consumo (l/ha)')
                #OPERADOR
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operador</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date4 = dados.groupby('Nome_Operador')['Consumo (L/Ha)'].mean().reset_index().round(2)
                filter7 = np.array(date4['Consumo (L/Ha)'])
                filter8 = np.array(date4['Nome_Operador'].astype(str))
                operador(filter7, filter8, 'Operador', 'Consumo (l/ha)')
            elif página_selecionada=="Tempo efetivo":
                '\n'
                '\n'
                st.markdown("<h2 style='text-align: center; color: #033102;'><b>Tempo Operacional</b></h2>", unsafe_allow_html=True)
                #Fazenda
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por fazenda</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                date0 = dados.groupby('DESC_FAZENDA')['Tempo efetivo (h)'].sum().reset_index().round(2)
                filter10 = np.array(date0['Tempo efetivo (h)'])
                filter11 = np.array(date0['DESC_FAZENDA'].astype(str))
                fazenda(filter10, filter11, 'Fazenda', 'Tempo efetivo (h)')
                #TALHAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por talhão</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date3 = dados.groupby('DESC_TALHAO')['Tempo efetivo (h)'].sum().reset_index().round(2)
                filter5 = np.array(date3['Tempo efetivo (h)'])
                filter6 = np.array(date3['DESC_TALHAO'].astype(str))
                talhao(filter5, filter6, 'Talhão', 'Tempo efetivo (h)')
                #OPERACAO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operação</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date1 = dados.groupby('Operações_gerais')['Tempo efetivo (h)'].sum().reset_index ().round(2)
                filter1 = np.array(date1['Tempo efetivo (h)'])
                filter2 = np.array(date1['Operações_gerais'].astype(str))
                operacao(filter1, filter2, 'Operação', 'Tempo efetivo (h)')
                #EQUIPAMENTO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por equipamento</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date2 = dados.groupby('Nome_Equipamento')['Tempo efetivo (h)'].sum().reset_index().round(2)
                filter3 = np.array(date2['Tempo efetivo (h)'])
                filter4 = np.array(date2['Nome_Equipamento'].astype(str))
                equipamento(filter3, filter4, 'Equipamento', 'Tempo efetivo (h)')
                #OPERADOR
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operador</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                date4 = dados.groupby('Nome_Operador')['Tempo efetivo (h)'].sum().reset_index().round(2)
                filter7 = np.array(date4['Tempo efetivo (h)'])
                filter8 = np.array(date4[['Nome_Operador']].astype(str))
                operador(filter7, filter8, 'Operador', 'Tempo efetivo (h)')
            elif página_selecionada=="Apontamentos":
                '\n'
                '\n'
                st.markdown("<h2 style='text-align: center; color: #033102;'><b>Apontamentos</b></h2>", unsafe_allow_html=True)
                #Fazenda
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por fazenda</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                contagem_fazenda = (dados['DESC_FAZENDA'].value_counts()).reset_index()
                contagem_fazenda.columns = ['Fazenda', 'Apontamentos']
                indexNames = contagem_fazenda[contagem_fazenda['Fazenda']==0].index
                contagem_fazenda.drop(indexNames , inplace=True)
                filter10 = np.array(contagem_fazenda['Apontamentos'])
                filter11 = np.array(contagem_fazenda['Fazenda'].astype(str))
                fazenda(filter10, filter11, 'Fazenda', 'Apontamentos')
                #EQUIPAMENTO
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por equipamento</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                contagem_equip = (dados['Nome_Equipamento'].value_counts()).reset_index()
                contagem_equip.columns = ['Equipamento', 'Apontamentos']
                indexNames = contagem_equip[contagem_equip['Equipamento']==0].index
                contagem_equip.drop(indexNames , inplace=True)
                filter3 = np.array(contagem_equip['Apontamentos'])
                filter4 = np.array(contagem_equip['Equipamento'].astype(str))
                equipamento(filter3,filter4, 'Equipamento', 'Apontamentos')
                #OPERADOR
                '\n'
                st.markdown("<h3 style='text-align: left; color: #033102;'><b>Por operador</b></h3>", unsafe_allow_html=True)
                '\n'
                st.text("Gráfico")
                #Gerando gráfico
                contagem_oper = (dados['Nome_Operador'].value_counts()).reset_index()
                contagem_oper.columns = ['Operador', 'Apontamentos']
                indexNames = contagem_oper[contagem_oper['Operador']==0].index
                contagem_oper.drop(indexNames , inplace=True)
                filter7 = np.array(contagem_oper['Apontamentos'])
                filter8 = np.array(contagem_oper['Operador'].astype(str))
                operador(filter7, filter8, 'Operador', 'Apontamentos')