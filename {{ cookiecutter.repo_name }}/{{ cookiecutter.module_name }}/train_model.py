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
def train_model(config: DictConfig):
    """Function to train the model"""

    print(f"Train modeling using {config.data.processed}")
    print(f"Model used: {config.model.name}")
    print(f"Save the output to {config.data.final}")


@app.command()
def run():
    train_model()

if __name__ == "__main__":
    app()