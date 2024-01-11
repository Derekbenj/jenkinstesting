import data_processing
import models

def main():
    """Main entry point of the program."""

    # Load and process data
    data = data_processing.load_and_preprocess_data()

    # Train a model
    model = models.train_model(data)

    # Use the model (e.g., for predictions)
    # new_data = 5
    # predictions = model.predict(new_data)

    # print(predictions)
    print("We did it!")
    print("does it rebuild on push?")
    print("will it build again?")

if __name__ == "__main__":
    main()