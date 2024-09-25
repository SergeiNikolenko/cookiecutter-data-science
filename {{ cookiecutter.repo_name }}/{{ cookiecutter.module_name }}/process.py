import hydra
from omegaconf import DictConfig
import typer
from loguru import logger

try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass


app = typer.Typer()

@hydra.main(config_path="../config", config_name="main", version_base="1.2")
def process_data(config: DictConfig):
    """Function to process the data"""
    
    logger.info("Starting data processing...")
    logger.info(f"Process data using {config.data.raw}")
    logger.info(f"Columns used: {config.process.use_columns}")

    # Ваш код обработки данных здесь


@app.command()
def run():
    process_data()

if __name__ == "__main__":
    app()