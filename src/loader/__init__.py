from src.loader.circulacao_viaria import main as loader_circulacao_viaria
from src.loader.estacionamento_rotativo import main as loader_estacionamento_rotativo
from src.loader.estacionamento_rotativo_idoso import main as loader_estacionamento_rotativo_idoso
from src.loader.estacionamento_rotativo_motofrete import main as loader_estacionamento_rotativo_motofrete
from src.loader.logradouros_acidentes_transito_vitima import main as loader_logradouros_acidentes_transito_vitima
from src.loader.ocorrencias_acidentes_transito_vitima import main as loader_ocorrencias_acidentes_transito_vitima
from src.loader.pessoas_acidentes_transito_vitima import main as loader_pessoas_acidentes_transito_vitima
from src.loader.posto_venda_rotativo import main as loader_posto_venda_rotativo
from src.loader.redutor_velocidade import main as loader_redutor_velocidade
from src.loader.sinalizacao_semaforica import main as loader_sinalizacao_semaforica
from src.loader.veiculos_acidentes_transito_vitima import main as loader_veiculos_acidentes_transito_vitima


def main():
    loader_circulacao_viaria()
    loader_estacionamento_rotativo()
    loader_estacionamento_rotativo_idoso()
    loader_estacionamento_rotativo_motofrete()
    loader_logradouros_acidentes_transito_vitima()
    loader_ocorrencias_acidentes_transito_vitima()
    loader_pessoas_acidentes_transito_vitima()
    loader_posto_venda_rotativo()
    loader_redutor_velocidade()
    loader_sinalizacao_semaforica()
    loader_veiculos_acidentes_transito_vitima()


if __name__ == '__main__':
    main()
