from forex_python.converter import CurrencyRates

def get_exchange_rate(base_currency, target_currency):
    currency_rates = CurrencyRates()
    return currency_rates.get_rate(base_currency, target_currency)

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    base_currency = input("Digite a moeda de origem (ex: USD, EUR, BRL): ").upper()
    target_currency = input("Digite a moeda de destino (ex: USD, EUR, BRL): ").upper()
    
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate is not None:
        try:
            amount = float(input(f"Digite o valor em {base_currency} que deseja converter para {target_currency}: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")
            return
        
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount:.2f} {base_currency} equivale a {converted_amount:.2f} {target_currency}")
    else:
        print("Não foi possível obter a taxa de câmbio.")

if __name__ == "__main__":
    main()
