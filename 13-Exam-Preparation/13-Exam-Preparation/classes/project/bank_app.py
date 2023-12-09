from typing import List

from project.clients.adult import Adult
from project.clients.student import Student
from project.clients.base_client import BaseClient
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_STUDENT_TYPES = {"Student": Student, "Adult": Adult}
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    # VALID_CLIENT_LOAN_PAIR = {"Student": StudentLoan, "Adult": MortgageLoan}
    # VALID_LOAN_CLIENT_PAIR = {"StudentLoan": Student, "MortgageLoan": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")
        loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_STUDENT_TYPES:
            raise Exception("Invalid client type!")
        if self.capacity == len(self.clients):
            return "Not enough bank capacity."

        client = self.VALID_STUDENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = next((l for l in self.loans if loan_type == l.__class__.__name__), None)
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if (loan_type == "StudentLoan" and client.__class__.__name__ == "Student") or (
                loan_type == "MortgageLoan" and client.__class__.__name__ == "Adult"):
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")


    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client not in self.clients:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                counter += 1
        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        c_counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                c_counter += 1
        return f"Number of clients affected: {c_counter}."

    def get_statistics(self):
        if len(self.clients) == 0:
            avg_interest_rate = 0
        else:
            avg_interest_rate = (sum([c.interest for c in self.clients]) / len(self.clients))

        result = f"Active Clients: {len(self.clients)}\n"
        result += f"Total Income: {sum([c.income for c in self.clients]):.2f}\n"
        result += (f"Granted Loans: {sum([len(c.loans) for c in self.clients])},"
                   f" Total Sum: {sum([l.amount for c in self.clients for l in c.loans]):.2f}\n")
        result += f"Available Loans: {len(self.loans)}, Total Sum: {sum([l.amount for l in self.loans]):.2f}\n"
        result += f"Average Client Interest Rate: {avg_interest_rate:.2f}"
        return result

