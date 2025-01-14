import __init__
import matplotlib.pyplot as plt
from models.database import engine
from models.model import Subscription, Payments
from sqlmodel import Session, select
from datetime import date, datetime


class SubscriptionService:

    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription

    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            result = session.exec(statement).all()
        return result

    def delete(self, id):
        with Session(self.engine) as session:
            statement = select(Subscription).where(Subscription.id == id)
            result = session.exec(statement).one()
            session.delete(result)
            session.commit()

    def _has_pay(self, results):
        for result in results:
            if result.date.month == date.today().month:
                return True
        return False

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            # Verifica se já existe um pagamento para este mês
            statement = (
                select(Payments)
                .where(Payments.subscription_id == subscription.id)
                .where(Payments.date.between(date.today().replace(day=1), date.today()))
            )
            existing_payment = session.exec(statement).first()

            if existing_payment:
                question = input(
                    "Essa conta já foi paga este mês. Deseja pagar novamente? (Y/N): "
                )
                if question.strip().upper() != "Y":
                    return False

            # Registra o pagamento
            new_payment = Payments(subscription_id=subscription.id, date=date.today())
            session.add(new_payment)
            session.commit()
            print(f"Pagamento registrado para a assinatura: {subscription.empresa}")
            return True


    def total_value(self):
        with Session(self.engine) as session:
            statament = select(Subscription)
            results = session.exec(statament).all()

            total = 0

            for result in results:
                total += result.valor

            return float(total)

    def _get_last_12_months_native(self):
        today = datetime.now()

        year = today.year

        month = today.month

        last_12_month = []

        for _ in range(12):
            last_12_month.append((month, year))

            month -= 1

            if month == 0:
                month = 12
                year -= 1

        return last_12_month[::-1]

    def _get_values_for_months(self, last_12_month):
        with Session(self.engine) as session:
            statement = select(Payments)
            results = session.exec(statement).all()

            value_for_months = []

            for i in last_12_month:
                value = 0
                for result in results:
                    if result.date.month == i[0] and result.date.year == i[1]:
                        value += float(result.subscription.valor)
                value_for_months.append(value)

            return value_for_months

    def gen_chart(self):
        last_12_months = self._get_last_12_months_native()
        values_for_months = self._get_values_for_months(last_12_months)

        plt.plot([1, 2], [5, 6])
        plt.show()

