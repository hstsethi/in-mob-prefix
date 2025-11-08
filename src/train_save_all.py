from train_save import train_save_model


def train_save_all():
    "Function to train and save all models"

    train_save_model("../models/9xxx-gbc.bin", "../data/9xxx-in-mob-prefix.csv")
    train_save_model("../models/8xxx-gbc.bin", "../data/8xxx-in-mob-prefix.csv")
    train_save_model("../models/7xxx-gbc.bin", "../data/7xxx-in-mob-prefix.csv")
    train_save_model("../models/6xxx-gbc.bin", "../data/6xxx-in-mob-prefix.csv")


if __name__ == "__main__":
    train_save_all()
