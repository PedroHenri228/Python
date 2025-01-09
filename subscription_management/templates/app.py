import __init__
from views.view import SubscriptionService
from models.database import engine
from models.model import Subscription
from datetime import datetime
from decimal import Decimal
class UI:
    
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)
        
    def start(self):
        
        while True:
            
            print('''
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [5] -> Sair
            ''')
            
            choice = int(input('Escolha uma opção: '))
            
            if choice == 1:
                self.add_subscription()
                
            elif choice == 2:
                self.delete_subscription()
                
            elif choice == 3:
                self.total_value()
                
            elif choice == 4:
                 self.subscription_service.gen_chart()
                 
            else:
                break
    
    def add_subscription(self):
        empresa = input("Empresa: ")
        site = input("Site: ")
        data_assinatura = datetime.strftime(input("Data de Assinatura: ", "%Y-%m-%d"))
        valor = Decimal(input("Valor: "))
        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor)
        self.subscription_service.create(subscription)
    
    
    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        
        print("Escolha a assinatura para cancelar: ")
        
        for i in subscriptions:
            print(f"{i.id} => {i.empresa}")
            
            choice = int(input("Assinatura: "))
            
            sucesso = self.subscription_service.delete(choice)
            
            if sucesso:
                print(print("Assinatura cancelada com sucesso."))
            else:
                print("Erro ao cancelar a assinatura. Verifique se informou o a assinatura correta!")
                
    def total_value(self):
        print(f'Mensalidade Total das Assinaturas: {self.subscription_service.total_value()}')

        
if __name__ == "__main__":
    template = UI()
    
    template.start()