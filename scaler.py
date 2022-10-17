from typing import Sequence
import pandas as pd
import pickle

scaler = pickle.load(open('scaler.pkl', 'rb'))


def runScaler(texture_mean, area_mean, concavity_mean, area_se, concavity_se, fractal_dimension_se, smoothness_worst, concavity_worst, symmetry_worst, fractal_dimension_worst):
    d = {'texture_mean': [texture_mean], 'area_mean': [area_mean], 'concavity_mean': [concavity_mean], 'area_se': [area_se], 'concavity_se': [concavity_se], 'fractal_dimension_se': [
        fractal_dimension_se], 'smoothness_worst': [smoothness_worst], 'concavity_worst': [concavity_worst], 'symmetry_worst': [symmetry_worst], 'fractal_dimension_worst': [fractal_dimension_worst]}
    df = pd.DataFrame(data=d)
    return scaler.transform(df)
