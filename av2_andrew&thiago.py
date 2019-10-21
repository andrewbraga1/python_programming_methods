class Bem(object):
    def __init__(self, nome):
        self.nome = nome
        
    def iniciar(self):
        raise NotImplementedError(
            "Subclasses precisam implementar o metodo abstrato"
        )
    def caracteristica_bem(self):
        print('Esta caracterisitica é UNICA de um BEM')

    def valor(self):
        print('valor do bem é R$ bbb,bb')    

class Produto(Bem):
    def iniciar(self):
        #print(self)
        print('Este produto acaba de iniciar')

    def adicionar_produto(self):
        print("Mais um produto foi adicionado")

    def caracteristica_produto(self):
        print('Esta caracterisitica é UNICA de um PRODUTO')

    def valor(self):
        print('valor do produto é R$ pp,pp')         
   
    def faturar(self):
        print("Nota finalizada, favor buscar seus produtos com a sua nota em mãos.") 

class Servico(Bem):
    def iniciar(self):
        print('Este serviço acaba de ser iniciado')

    def adicionar_servico(self):
        print("Este serviço foi adicionado ao contrato")  

    def caracteristica_servico(self):
        print('Esta caracterisitica é UNICA de um SERVIÇO')

    def valor(self):
        print('valor do serviço é R$ sss,ss')         
   
    def fechar_contrato(self):
        print("Contrato de serviço finalizado")  

if __name__ == '__main__':        
    k = {}
    bem = Bem(k)
    print('#######################')
    print('#######################')
    bem.valor()
    print('#######################')
    produto = Produto(bem);
    servico = Servico(bem);
    produto.iniciar()
    servico.iniciar()
    print('#######################')
    produto.valor()
    servico.valor()
    print('#######################')
    produto.adicionar_produto()
    servico.adicionar_servico()
    print('#######################')
    produto.faturar()
    servico.fechar_contrato()
    print('#######################')
    bem.caracteristica_bem()
    produto.caracteristica_produto()
    servico.caracteristica_servico()
    print('#######################')