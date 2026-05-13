from transformers import pipeline

# Use text-generation instead
generator = pipeline(
    "text-generation",
    model="gpt2"
)


def generate_summary(text):

    text = text[:1000]

    prompt = f"Summarize the following text:\n\n{text}\n\nSummary:"

    result = generator(
        prompt,
        max_length=200,
        num_return_sequences=1
    )

    return result[0]["generated_text"]

    