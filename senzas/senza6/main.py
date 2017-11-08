def kensci_senza(shouldFail):
    if shouldFail:
        raise ValueError("Expected failure.")
    else:
        return "Did not fail"
