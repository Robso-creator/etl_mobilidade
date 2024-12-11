import pandas as pd
import requests

def main():
    urls = [
        "https://ckan.pbh.gov.br/dataset/posto-de-venda-rotativo",
        "https://ckan.pbh.gov.br/dataset/redutor-de-velocidade",
        "https://ckan.pbh.gov.br/dataset/relacao-dos-veiculos-envolvidos-nos-acidentes-de-transito-com-vitima"
    ]

    def download_csv(url):
        response = requests.get(url)
        with open("dataset.csv", "wb") as file:
            file.write(response.content)
        return pd.read_csv("dataset.csv")

    dataframes = [download_csv(url) for url in urls]

    for df in dataframes:
        df.dropna(inplace=True)

    final_df = pd.concat(dataframes)
    final_df.to_csv("final_dataset.csv", index=False)

    breakpoint()

if __name__ == '__main__':
    print('aqui foi amigão')