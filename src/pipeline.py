from src.extractor.main import main as extractor_main
from src.loader import main as loader_main
from src.transformer.bronze import main as bronze_main
from src.transformer.gold import main as gold_main

if __name__ == '__main__':
    extractor_main()

    bronze_main()

    gold_main()

    loader_main()
