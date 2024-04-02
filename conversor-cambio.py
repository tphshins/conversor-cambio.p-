import requests

def get_exchange_rate(base_currency, target_currency):
    try:
        api_key = 'YOUR_API_KEY'  # Substitua 'YOUR_API_KEY' pela sua chave da ExchangeRate-API
        url = f'https://v6.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}&apiKey={api_key}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'error' in data:
            raise ValueError(data['error'])
        return data['rates'][target_currency]
    except requests.RequestException as e:
        print(f"Erro ao obter taxa de câmbio: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Erro ao processar resposta da API: {e}")
        return None

def convert_currency(amount, exchange_rate):
    try:
        if exchange_rate is None or exchange_rate <= 0:
            raise ValueError("Taxa de câmbio inválida")
        
        if amount <= 0:
            raise ValueError("Valor inválido para conversão")
        
        converted_amount = amount * exchange_rate
        return converted_amount
    except ValueError as e:
        print(f"Erro ao converter valor: {e}")
        return None

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
        if converted_amount is not None:
            print(f"{amount:.2f} {base_currency} equivale a {converted_amount:.2f} {target_currency}")
    else:
        print("Não foi possível obter a taxa de câmbio.")

if __name__ == "__main__":
    main()
