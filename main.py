import numpy as np
import pandas as pd
from options import get_options
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from joblib import dump, load
from tqdm import tqdm

def read_csv_pgbar(csv_path, index_col=None, chunksize=1024, read_first=None, usecols=None):
    rows = sum(1 for _ in open(csv_path, 'r')) - 1
    chunk_list = []
    with tqdm(total=rows, desc=f'Reading {csv_path}') as pbar:
        i = 0
        for chunk in pd.read_csv(csv_path, index_col=index_col, chunksize=chunksize, sep='\t', usecols=usecols):
            chunk_list.append(chunk)
            pbar.update(len(chunk))
            i += 1
            if i+1 == read_first:
                break
    df = pd.concat((f for f in chunk_list), axis=0)
    return df

def train(opts):
    if opts.model == 'baseline':
        feat_traintest = read_csv_pgbar(opts.path_to_dataset + 'FINAL_FEATURES_TRAINTEST.tsv', index_col=0)
        targets_traintest = read_csv_pgbar(opts.path_to_dataset + 'FINAL_TARGETS_DATES_TRAINTEST.tsv', index_col=0)
        _public_idx = targets_traintest[targets_traintest['TARGET'] != 'test'].index.values
        public_idx = _public_idx[(_public_idx != 86181) & (_public_idx != 84024)] # drop extra users
        public_targets = targets_traintest.loc[public_idx]
        public_targets.TARGET = public_targets.TARGET.astype('int')
        np.random.seed(1)
        mask = np.random.choice(['train', 'test'], size=len(public_idx), p=[0.8, 0.2])
        train_idx = public_idx[mask == 'train']
        test_idx = public_idx[mask == 'test']
        train_baseline(feat_traintest.loc[train_idx], public_targets.loc[train_idx], opts.path_to_model)

def train_baseline(feat_traintest, public_targets, path_to_model):
    clf = make_pipeline(
        PCA(n_components=128),
        GradientBoostingClassifier(n_estimators=64, max_depth=4, verbose=1)
    )
    clf.fit(
        feat_traintest, 
        public_targets.loc[:, 'TARGET'],
    )
    dump(clf, path_to_model)

def evaluate(opts):
    if opts.model == 'baseline':
        feat_traintest = read_csv_pgbar(opts.path_to_dataset + 'FINAL_FEATURES_TRAINTEST.tsv', index_col=0)
        targets_traintest = read_csv_pgbar(opts.path_to_dataset + 'FINAL_TARGETS_DATES_TRAINTEST.tsv', index_col=0)
        _public_idx = targets_traintest[targets_traintest['TARGET'] != 'test'].index.values
        public_idx = _public_idx[(_public_idx != 86181) & (_public_idx != 84024)] # drop extra users
        public_targets = targets_traintest.loc[public_idx]
        public_targets.TARGET = public_targets.TARGET.astype('int')
        np.random.seed(1)
        mask = np.random.choice(['train', 'test'], size=len(public_idx), p=[0.8, 0.2])
        train_idx = public_idx[mask == 'train']
        test_idx = public_idx[mask == 'test']
        evaluate_baseline(feat_traintest.loc[test_idx], public_targets.loc[test_idx], opts.path_to_model)

def evaluate_baseline(feat_traintest, public_targets, path_to_model):
    clf = load(path_to_model)
    pred = clf.predict_proba(feat_traintest)
    print(roc_auc_score(public_targets['TARGET'], pred[:, 1]))

def predict(opts):
    if opts.model == 'baseline':
        feat_traintest = read_csv_pgbar(opts.path_to_dataset + 'FINAL_FEATURES_TRAINTEST.tsv', index_col=0)
        idx = opts.idx
        predict_baseline(feat_traintest.loc[idx], opts.path_to_model)

def predict_baseline(feat_traintest, path_to_model):
    clf = load(path_to_model)
    pred = clf.predict_proba(feat_traintest)
    print(pred[:, 1])

if __name__ == "__main__":
    opts = get_options()
    if opts.action == 'train':
        train(opts)
    if opts.action == 'evaluate':
        evaluate(opts)
    if opts.action == 'predict':
        predict(opts)