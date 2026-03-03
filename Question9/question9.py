def is_valid_url(url):
    """Check if the passed parameter is a valid URL"""

    # must be a string
    if type(url) != str:
        return False

    # must start with http:// or https://
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    # URLs cannot contain spaces
    if " " in url:
        return False

    # remove the protocol to get everything after it
    if url.startswith("https://"):
        rest = url[8:]
    else:
        rest = url[7:]

    # must have something after the protocol
    if len(rest) == 0:
        return False

    # get just the domain (everything before the first "/")
    domain = rest.split("/")[0]

    # domain must contain a dot
    if "." not in domain:
        return False

    # nothing can be empty around the dot — "google." or ".com" are not valid
    parts = domain.split(".")
    for part in parts:
        if len(part) == 0:
            return False

    return True


# tests
print(is_valid_url("https://google.com"))        # True
print(is_valid_url("http://ie.edu/masters"))      # True
print(is_valid_url("google.com"))                 # False - no protocol
print(is_valid_url("https://"))                   # False - nothing after protocol
print(is_valid_url("https://google"))             # False - no dot in domain
print(is_valid_url("https://google. com"))        # False - space
print(is_valid_url(1234))                         # False - not a string
