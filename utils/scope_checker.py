ALLOWED_DOMAINS = {"google.com","example.com"}

def is_within_scope(target):
    return target in ALLOWED_DOMAINS
