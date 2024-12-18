from src.transformer.gold.circulacao_viaria_no_do_trecho import main as gold_circulacao_viaria_no_do_trecho_main
from src.transformer.gold.estacionamento_idoso import main as gold_estacionamento_idoso_main
from src.transformer.gold.estacionamento_rotativo_para_motofrete import main as gold_estacionamento_rotativo_para_motofrete_main
from src.transformer.gold.faces_de_quadras_regulamentadas_com_estacionamento_rotativo import main as gold_faces_de_quadras_regulamentadas_com_estacionamento_rotativo_main
from src.transformer.gold.localizacao_das_sinalizacoes_semaforicas import main as gold_localizacao_das_sinalizacoes_semaforicas_main
from src.transformer.gold.posto_de_venda_rotativo import main as gold_posto_de_venda_rotativo_main
from src.transformer.gold.redutor_de_velocidade import main as gold_redutor_de_velocidade_main
from src.transformer.gold.relacao_das_pessoas_envolvidas_nos_acidentes_de_transito_com_vitima import main as gold_relacao_das_pessoas_envolvidas_nos_acidentes_de_transito_com_vitima_main
from src.transformer.gold.relacao_de_ocorrencias_de_acidentes_de_transito_com_vitima import main as gold_relacao_de_ocorrencias_de_acidentes_de_transito_com_vitima_main
from src.transformer.gold.relacao_dos_logradouros_dos_locais_de_acidentes_de_transito_com_vitima import main as gold_relacao_dos_logradouros_dos_locais_de_acidentes_de_transito_com_vitima_main
from src.transformer.gold.relacao_dos_veiculos_envolvidos_nos_acidentes_de_transito_com_vitima import main as gold_relacao_dos_veiculos_envolvidos_nos_acidentes_de_transito_com_vitima_main


def main():
    gold_circulacao_viaria_no_do_trecho_main()
    gold_estacionamento_idoso_main()
    gold_estacionamento_rotativo_para_motofrete_main()
    gold_faces_de_quadras_regulamentadas_com_estacionamento_rotativo_main()
    gold_localizacao_das_sinalizacoes_semaforicas_main()
    gold_posto_de_venda_rotativo_main()
    gold_redutor_de_velocidade_main()
    gold_relacao_das_pessoas_envolvidas_nos_acidentes_de_transito_com_vitima_main()
    gold_relacao_de_ocorrencias_de_acidentes_de_transito_com_vitima_main()
    gold_relacao_dos_logradouros_dos_locais_de_acidentes_de_transito_com_vitima_main()
    gold_relacao_dos_veiculos_envolvidos_nos_acidentes_de_transito_com_vitima_main()


if __name__ == '__main__':
    main()
