from transformers import pipeline
from typing import TextIO


def summarization(text: TextIO):
    classifier = pipeline("summarization")
    with open(text, "r") as file:
        content: str = file.read()

    txtSummary = classifier(content)
    return str(txtSummary[0]["summary_text"])


def str_summarization(str_text: str):
    classifier = pipeline("summarization")
    txtSummary = classifier(str_text)
    return str(txtSummary[0]["summary_text"])
