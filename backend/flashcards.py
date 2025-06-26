from together_llm import generate_answer
import re

def generate_flashcards(text_chunk: str) -> list[dict]:

    prompt = f"""Generate 3 flashcards from the following content.

Format each flashcard as:
Q: <question>
A: <answer>

Text:
{text_chunk}
"""

    raw_output = generate_answer(prompt)
    return parse_flashcards(raw_output)


def parse_flashcards(raw_text: str) -> list[dict]:
    """
    Parses the LLM output into structured flashcard list.
    """

    # Split by Q: ... A: ...
    qa_pairs = re.findall(r"Q:\s*(.*?)\s*A:\s*(.*?)(?=\nQ:|\Z)", raw_text, re.DOTALL)

    flashcards = []
    for q, a in qa_pairs:
        flashcards.append({
            "question": q.strip(),
            "answer": a.strip()
        })

    return flashcards