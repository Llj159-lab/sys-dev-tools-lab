def normalize_name(name):
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be blank")
    if any(character.isdigit() for character in cleaned):
        raise ValueError("name must not contain digits")
    return " ".join(cleaned.split())
