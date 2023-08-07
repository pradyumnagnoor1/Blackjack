def cardAscii(rank, suit):
    card_ascii = f"""
        ┌─────────┐
        │ {rank:<2}      │
        │         │
        │    {suit}    │
        │         │
        │      {rank:>2} │
        └─────────┘
    """

    return card_ascii
