"""
Rule-based feedback engine — без обращения к внешним LLM API.
"""

CATEGORY_TIPS = {
    "verb_tense": (
        "Tense mistakes usually come from mixing up when an action happens. "
        "Tip: ask yourself — is this a completed action, an ongoing one, or "
        "something that started in the past and continues now?"
    ),
    "articles": (
        "Articles (a/an/the) depend on whether something is specific or general. "
        "Tip: use 'a/an' for something new or one of many, 'the' for something "
        "specific or already known."
    ),
    "prepositions": (
        "Prepositions often don't translate literally between languages. "
        "Tip: learn prepositions together with the word they follow, as a fixed "
        "phrase, rather than translating word by word."
    ),
    "subject_verb": (
        "The verb must agree with the subject in number. "
        "Tip: find the real subject first, then check if it's singular or plural."
    ),
    "word_order": (
        "English has a fairly strict word order (usually Subject-Verb-Object). "
        "Tip: build the sentence core first, then add details like time and place."
    ),
    "vocabulary": (
        "This is about choosing the word that best fits the meaning or context. "
        "Tip: learn new words inside example sentences, not as isolated translations."
    ),
    "other": (
        "Tip: review this rule with a fresh example sentence of your own."
    ),
}


def build_feedback(wrong_answers: list[dict]) -> list[dict]:
    feedback = []
    for item in wrong_answers:
        category_tip = CATEGORY_TIPS.get(item["category"], CATEGORY_TIPS["other"])
        feedback.append({
            "question": item["question"],
            "chosen": item["chosen"],
            "correct": item["correct"],
            "specific_explanation": item.get("chosen_explanation") or "",
            "general_tip": category_tip,
        })
    return feedback