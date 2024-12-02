from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

def train_model(tokenized_data, labels, model_name="bert-base-uncased", output_dir="model_output"):
    """Fine-tune a pretrained model on the dataset."""
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(set(labels)))

    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_data,
        eval_dataset=tokenized_data,
    )

    trainer.train()
    return model
