import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def game():
    answers = [
        "Sigue por este camino y lograrás todo.",
        "Vaya... ¡Qué mala suerte!",
        "Yo digo que sí.",
        "Tengo mis dudas...",
        "La verdad, no lo sé.",
        "Supondremos que sí.",
        "Naaaaaa...",
        "Creo que no.",
        "Supongamos que sí.",
    ]
    return random.choice(answers)

def currency():
    results = [
        "¡Y es cara!",
        "¡Y es escudo!",
    ]
    return random.choice(results)

def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "CRUZ"
