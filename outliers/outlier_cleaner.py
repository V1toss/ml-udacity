#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    for pred, a, net_w in zip(predictions, ages, net_worths):
        cleaned_data.append((a, net_w, pred - net_w))

    cleaned_data.sort(key=lambda i: i[2])

    return cleaned_data[:81]

