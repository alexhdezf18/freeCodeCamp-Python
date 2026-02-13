def verify_card_number(card_number):
    clean_number = card_number.replace(" ", "").replace("-", "")
    digits = [int(d) for d in clean_number]

    digits.reverse()

    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] >= 9:
            digits[i] -= 9
    
    total = sum(digits)

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
