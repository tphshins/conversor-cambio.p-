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
    moeda_base = input("Digite a moeda de origem (BRL, USD, EUR, JPY, INR): ").upper()
    moeda_alvo = input("Digite a moeda de destino (BRL, USD, EUR, JPY, INR): ").upper()
    valor_str = input("Digite o valor a ser convertido: ")
    valor_str = valor_str.replace(',', '.')  # Substitui vírgula por ponto
    valor = float(valor_str)

    taxa = obter_taxa_de_cambio(moeda_base, moeda_alvo)
    valor_convertido = converter_moeda(valor, moeda_base, moeda_alvo, taxa)

    print(f"\nTaxa de conversão de {moeda_base} para {moeda_alvo}: {taxa}")
    print(f"Valor convertido de {moeda_base} para {moeda_alvo}: {valor_convertido:.2f}")

if __name__ == "__main__":
    main()
