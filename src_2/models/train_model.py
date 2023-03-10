import logging
import os
from pathlib import Path

import hydra
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F
from dotenv import find_dotenv, load_dotenv
from hydra.utils import get_original_cwd

import wandb
from src_2.models.model import GCN


@hydra.main(
    version_base=None, config_path="../config", config_name="default_config.yaml"
)
def main(cfg):
    wandb.init(project="MLOps", entity="team-27")
    print(f"Current working directory : {os.getcwd()}")
    print(f"Orig working directory    : {get_original_cwd()}")
    logger = logging.getLogger(__name__)
    logger.info("training model")

    hparams = cfg.experiment
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    torch.manual_seed(hparams["seed"])

    dataset = torch.load(f"{get_original_cwd()}/{hparams['input_filepath']}")
    data = dataset[0].to(device)
    model = GCN(dataset.num_node_features, dataset.num_classes).to(device)
    optimizer = torch.optim.Adam(
        model.parameters(), lr=hparams["lr"], weight_decay=hparams["weight_decay"]
    )

    train_loss = []
    model.train()
    for epoch in range(hparams["epochs"]):
        optimizer.zero_grad()
        out = model(data)
        loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
        loss.backward()
        optimizer.step()
        loss = loss.item()
        train_loss.append(loss)
        if epoch % hparams["log_interval"] == 0:
            logger.info(f"Training loss: {loss}")
            wandb.log({"loss": loss})

    torch.save(model.state_dict(), f"{os.getcwd()}/trained_model.pt")

    plt.plot(range(1, hparams["epochs"] + 1), train_loss)
    plt.xlabel("Training step")
    plt.ylabel("Training loss")
    plt.savefig(f"{os.getcwd()}/training.png")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
