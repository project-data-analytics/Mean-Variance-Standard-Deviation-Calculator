import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    schema = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [np.mean(schema, axis=0).tolist(), np.mean(schema, axis=1).tolist(), np.mean(schema).item()],
        'variance': [np.var(schema, axis=0).tolist(), np.var(schema, axis=1).tolist(), np.var(schema).item()],
        'standard deviation': [np.std(schema, axis=0).tolist(), np.std(schema, axis=1).tolist(), np.std(schema).item()],
        'max': [np.max(schema, axis=0).tolist(), np.max(schema, axis=1).tolist(), np.max(schema).item()],
        'min': [np.min(schema, axis=0).tolist(), np.min(schema, axis=1).tolist(), np.min(schema).item()],
        'sum': [np.sum(schema, axis=0).tolist(), np.sum(schema, axis=1).tolist(), np.sum(schema).item()]
        }

    return calculations
