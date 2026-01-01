def evaluate_f1_components(tp, fp, fn):
    """
    Docstring for evaluate_f1_components
    
    :param tp: Description
    :param fp: Description
    :param fn: Description
    """
    # check typeError using isinstance
    if not isinstance(tp, int): 
        raise TypeError("tp must be int")
    if not isinstance(fp, int):
        raise TypeError("fp must be int")
    if not isinstance(fn, int):
        raise TypeError("fn must be int")
    
    if tp < 0 or fp < 0 or fn < 0:
        raise ValueError("tp and fp and fn must be greater than or equal zero")
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    F1_score = 2 * (precision * recall) / (precision + recall)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-score: {F1_score}")

    return precision, recall, F1_score

evaluate_f1_components(2, 3, 1)