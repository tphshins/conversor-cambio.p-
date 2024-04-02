import requests

def obter_taxa_de_cambio(moeda_base, moeda_alvo):
    url = f'https://api.exchangerate-api.com/v4/latest/{moeda_base}'
    resposta = requests.get(url)
    dados = resposta.json()
    taxa = dados['rates'][moeda_alvo]
    return taxa

def converter_moeda(valor, moeda_base, moeda_alvo, taxa_conversao):
    valor_convertido = valor * taxa_conversao
    return valor_convertido

def main():
    print("Selecione a moeda de origem:")
    print("1. Real (BRL)")
    print("2. Dólar (USD)")
    print("3. Euro (EUR)")
    print("4. Iene (JPY)")
    print("5. Rúpias Indianas (INR)")

    opcao_origem = int(input("Digite o número correspondente à moeda de origem: "))
    opcoes = {
        1: 'BRL',
        2: 'USD',
        3: 'EUR',
        4: 'JPY',
        5: 'INR'
    }
    moeda_base = opcoes[opcao_origem]

    print("\nSelecione a moeda de destino:")
    print("1. Real (BRL)")
    print("2. Dólar (USD)")
    print("3. Euro (EUR)")
    print("4. Iene (JPY)")
    print("5. Rúpias Indianas (INR)")

    opcao_destino = int(input("Digite o número correspondente à moeda de destino: "))
    moeda_alvo = opcoes[opcao_destino]

    valor_str = input("Digite o valor a ser convertido: ")
    valor_str = valor_str.replace(',', '.')  # Substitui vírgula por ponto
    valor = float(valor_str)

    taxa = obter_taxa_de_cambio(moeda_base, moeda_alvo)
    valor_convertido = converter_moeda(valor, moeda_base, moeda_alvo, taxa)

    print(f"\nTaxa de conversão de {moeda_base} para {moeda_alvo}: {taxa}")
    print(f"Valor convertido de {moeda_base} para {moeda_alvo}: {valor_convertido:.2f}")

if __name__ == "__main__":
    main()
