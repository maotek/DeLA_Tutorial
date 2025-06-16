import numpy as np
import pandas as pd
from pathlib import Path
import torch


TRAIN_PATH = Path("archive/train.csv")
TEST_PATH = Path("archive/test.csv")


def read_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def preprocess_data(df: pd.DataFrame) -> tuple[torch.Tensor, torch.Tensor]:
    X = df[df.columns[1:]].to_numpy() # Data points
    y = df[df.columns[0]].to_numpy() # Label

    X = X.reshape((X.shape[0], 351, 3))
    X = X[:, :, :-1] # Drop the Value column (not needed)
    y = y.reshape(y.shape[0], 1)

    # X: 60000, 351, 3
    # y: 60000, 1
    return torch.tensor(X), torch.tensor(y)

print(preprocess_data(read_data(TRAIN_PATH)))