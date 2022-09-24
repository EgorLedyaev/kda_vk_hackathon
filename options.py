import argparse
def get_options(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model', default='baseline', help="The type of model")
    parser.add_argument(
        '--path_to_model', default='', help='Path to model weights')
    parser.add_argument(
        '--path_to_dataset', default='', help='Path to the dataset')
    parser.add_argument(
        '--path_to_pred', default='', help='Path to the predictions')
    parser.add_argument(
        '--action', default='', help='What to do: train, evaluate, predict')
    parser.add_argument(
        '--idx', default='', help='Indices to predict')
    opts = parser.parse_args(args)
    if len(opts.idx):
        opts.idx = [int(item) for item in opts.idx.split(',')]
    return opts
