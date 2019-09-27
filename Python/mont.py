import re

NOME_ARQUIVO = "/home/dayane/Downloads/web/Python/prod.txt"
LISTA_PRODUTOS = []
PROD_PARA_LISTAR = []

def exibe_carrinho(carrinho):
    print("\n")
    soma = 0
    for i in carrinho:
        print("%s - %s" % (i.get_nome(), i.get_valor()))
        soma += i.get_valor()
    print("\n\tTOTAL: %.2f" % (soma))

class Produto:
    def __init__(self, nome, valor, id):
        self.nome = nome
        self.valor = valor
        self.id = id
    
    def get_nome(self): return self.nome
    def get_valor(self): return self.valor
    def get_id(self): return self.id

def perguntar(pergunta):
    try:
        if int(input(pergunta + ": 1 - SIM \t 2 - NAO:\t")) == 1: return True
        else: return False
    except:
        return False

def pergunta_com_resposta(pergunta):
    return input(pergunta + "\t")
    

def carregar_produtos():
    file = open(NOME_ARQUIVO, 'r')
    for i in file.readlines():
        try:
            prod = re.split(",", i)
            id = prod[0]
            nome = prod[1]
            valor = float(prod[2])
            if nome is None or valor is None: continue
            
            LISTA_PRODUTOS.append(Produto(nome, valor, id))
            pass
        except:
            pass

def procurar_produto():
    PROD_PARA_LISTAR = []
    
    nome = input("Qual produto deseja procurar?\t")
    nome = nome.lower()
    nome = re.findall("[a-z ]+", nome)
    
    for i in nome:
        if i == "de" and len(nome) > 1: continue
        for j in LISTA_PRODUTOS:
            
            # print(re.search(i, j.get_nome()) is not None and not PROD_PARA_LISTAR.__contains__(j))
            if re.search(i, j.get_nome()) is not None and not PROD_PARA_LISTAR.__contains__(j):
            
                PROD_PARA_LISTAR.append(j)
                
    return PROD_PARA_LISTAR

def listar_produtos():
    if len(PROD_PARA_LISTAR) == 0: 
        print("Sem Produtos para listar")
        return False

    print("\tVALOR - PRODUTO\n")
    for i in range(len(PROD_PARA_LISTAR)):
        prod = PROD_PARA_LISTAR[i]
        if i+1 < 10: print("0%s: %s . . . . . . . . . . %.2f"%(i+1 , prod.get_nome(),prod.get_valor()))
        else: print("%s: %s . . . . . . . . . . %.2f"%(i+1 , prod.get_nome(),prod.get_valor()))
    return True

print("\n\n============    Programa para simular uma compra    ============\n\n")
carregar_produtos()

se_finalizar = False
carrinho = []
while(not se_finalizar):
    se_finalizar = True
    se_procurar = True
    while se_procurar:
        PROD_PARA_LISTAR = procurar_produto()
        if len(PROD_PARA_LISTAR) == 0: 
            print("\nNenhum produto encontrado\n")
            continue
        se_procurar = False
        se_listar = True
        while se_listar:
            se_listar = False
            listar_produtos()
            if perguntar("\nAdicionar um produto ao carrinho?"):
                resp = pergunta_com_resposta("\nQual o codigo do produto que voce gostaria de adicionar?")
                se_listar = True
                try:
                    resp = int(resp)
                    carrinho.append(PROD_PARA_LISTAR[resp-1])
                    print("\n\n========================================")
                    print("\n%s adicionado ao carrinho" % (PROD_PARA_LISTAR[resp-1].get_nome()))
                    print("\n========================================\n\n")
                except :
                    print("\nCodigo do produto invalido")

            

        se_procurar = perguntar("\nProcurar mais produtos?")
    
    exibe_carrinho(carrinho)

    se_finalizar = perguntar("\nFinalizar compra?")

    