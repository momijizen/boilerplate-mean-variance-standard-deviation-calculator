import numpy as np

def calculate(list):

    if len(list) != 9 :
      raise ValueError("List must contain nine numbers.")

    list_np = np.array(list).reshape((3,3))

    calculations = {
      'mean': mean(list_np), 
      'variance': variance(list_np), 
      'standard deviation': std(list_np),
      'max': max(list_np),
      'min': min(list_np),
      'sum': sum(list_np)
    }
    
    return calculations


def mean(list_np):
    axis1 = list_np.mean(axis=0)
    axis2 = list_np.mean(axis=1)
    flattened = list_np.mean()
    result = [axis1.tolist(), axis2.tolist(), flattened.tolist()]
    return result


def variance(list_np):
    axis1 = list_np.var(axis=0)
    axis2 = list_np.var(axis=1)
    flattened = list_np.var()
    result = [axis1.tolist(), axis2.tolist(), flattened.tolist()]
    return result


def std(list_np):
    axis1 = list_np.std(axis=0)
    axis2 = list_np.std(axis=1)
    flattened = list_np.std()
    result = [axis1.tolist(), axis2.tolist(), flattened.tolist()]
    return result


def max(list_np):
    axis1 = list_np.max(axis=0)
    axis2 = list_np.max(axis=1)
    flattened = list_np.max()
    result = [axis1.tolist(), axis2.tolist(), flattened.tolist()]
    return result


def min(list_np):
    axis1 = list_np.min(axis=0)
    axis2 = list_np.min(axis=1)
    flattened = list_np.min()
    result = [axis1.tolist(), axis2.tolist(), flattened.tolist()]
    return result


def sum(list_np):
    axis1 = list_np.sum(axis=0)
    axis2 = list_np.sum(axis=1)
    flattened = list_np.sum()
    result = [axis1.tolist(), axis2.tolist(), flattened.tolist()]
    return result