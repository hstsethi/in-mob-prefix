from train_save import train_save_model
def train_save_all():
    "Function to train and save all models"

    train_save_model("9xxx-gbc.bin", "../data/9xxx-in-mob-prefix.csv")
    train_save_model("8xxx-gbc.bin", "../data/8xxx-in-mob-prefix.csv")
    train_save_model("7xxx-gbc.bin", "../data/7xxx-in-mob-prefix.csv")
    train_save_model("6xxx-gbc.bin", "../data/6xxx-in-mob-prefix.csv")

if __name__ == "__main__":
    train_save_all()

