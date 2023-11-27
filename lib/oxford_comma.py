def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        # Join all items with commas, except the last one which gets "and" before it
        return f"{', '.join(items[:-1])}, and {items[-1]}"
