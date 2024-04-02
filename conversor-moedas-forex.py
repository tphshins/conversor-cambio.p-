from forex_python.converter import CurrencyRates

def main():
    c = CurrencyRates()
    
    print("Escolha a moeda de origem:")
    print("1. Dólar (USD)")
    print("2. Euro (EUR)")
    print("3. Real (BRL)")
    print("4. Rupias Indianas (INR)")
    choice_from = int(input("Digite o número da moeda de origem: "))
    
    print("Escolha a moeda de destino:")
    print("1. Dólar (USD)")
    print("2. Euro (EUR)")
    print("3. Real (BRL)")
    print("4. Rupias Indianas (INR)")
    choice_to = int(input("Digite o número da moeda de destino: "))
    
    amount = float(input("Digite o valor a ser convertido: "))
    
    currencies = ['USD', 'EUR', 'BRL', 'INR']
    base_currency = currencies[choice_from - 1]
    target_currency = currencies[choice_to - 1]
    
    exchange_rate = c.get_rate(base_currency, target_currency)
    converted_amount = amount * exchange_rate
    
    print(f"{amount:.2f} {base_currency} equivale a {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
