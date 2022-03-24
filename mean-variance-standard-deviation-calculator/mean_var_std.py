import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list).reshape(3, 3)
    calculations = dict()
    calculations["mean"] = calculateMean(arr)
    calculations["variance"] = calculateVariance(arr)
    calculations["standard deviation"] = calculateStandardDeviation(arr)
    calculations["max"] = calculateMax(arr)
    calculations["min"] = calculateMin(arr)
    calculations["sum"] = calculateSum(arr)
    return calculations


def calculateMean(arr):
    returned = []
    returned.append(np.mean(arr, axis=0).tolist())
    returned.append(np.mean(arr, axis=1).tolist())
    returned.append(np.mean(arr).tolist())
    return returned


def calculateVariance(arr):
    returned = []
    returned.append(np.var(arr, axis=0).tolist())
    returned.append(np.var(arr, axis=1).tolist())
    returned.append(np.var(arr).tolist())
    return returned


def calculateStandardDeviation(arr):
    returned = []
    returned.append(np.std(arr, axis=0).tolist())
    returned.append(np.std(arr, axis=1).tolist())
    returned.append(np.std(arr).tolist())
    return returned


def calculateMax(arr):
    returned = []
    returned.append(np.max(arr, axis=0).tolist())
    returned.append(np.max(arr, axis=1).tolist())
    returned.append(np.max(arr).tolist())
    return returned


def calculateMin(arr):
    returned = []
    returned.append(np.min(arr, axis=0).tolist())
    returned.append(np.min(arr, axis=1).tolist())
    returned.append(np.min(arr).tolist())
    return returned


def calculateSum(arr):
    returned = []
    returned.append(np.sum(arr, axis=0).tolist())
    returned.append(np.sum(arr, axis=1).tolist())
    returned.append(np.sum(arr).tolist())
    return returned
