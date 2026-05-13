def answer_question(context, question):
    
    # Split into sentences
    sentences = context.split(".")

    # Remove common useless words
    stop_words = [
        "what", "is", "the", "a", "an",
        "of", "from", "when", "where",
        "how", "why", "are", "to"
    ]

    # Extract important keywords
    keywords = [
        word.lower()
        for word in question.split()
        if word.lower() not in stop_words
    ]

    best_sentence = ""

    # Search relevant sentence
    for sentence in sentences:

        sentence_lower = sentence.lower()

        score = 0

        for keyword in keywords:

            if keyword in sentence_lower:
                score += 1

        if score > 0:
            best_sentence = sentence.strip()
            break

    if best_sentence == "":
        return "Answer not found in document."

    return best_sentence