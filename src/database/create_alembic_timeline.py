import glob
import os

import pandas as pd

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


def create_alembic_timeline(verbose=True):
    list_files = []
    for file in glob.glob(ROOT_PATH + '/alembic/versions/*.py'):
        if '__init__.py' not in file:
            with open(file) as f:
                for line in f.readlines():
                    if line.startswith('revision:'):
                        revision = line.split('=')[1].replace('\n', '')
                    if line.startswith('down_revision:'):
                        down_revision = line.split('=')[1].replace('\n', '')
                        if down_revision == ' None':
                            down_revision = None

                    if 'def upgrade() -> None:' in line:
                        list_files.append(
                            {
                                'file': file,
                                'revision': revision,
                                'down_revision': down_revision,
                            },
                        )

                        revision, down_revision = None, None
                        continue

    df = pd.DataFrame(list_files)
    df['file'] = df['file'].apply(lambda x: os.path.basename(x))
    df = df[['file', 'revision', 'down_revision']]
    first_version = df.loc[df['down_revision'].isnull()]['revision'].values[0]
    df.loc[df['revision'] == first_version, 'order'] = 1
    find_revision(first_version, df, c=2)
    df.sort_values('order', ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    if verbose:
        print(df)
    return df


def find_revision(revision, df, c=0):
    if not df.loc[df['down_revision'] == revision].empty:
        df.loc[df['down_revision'] == revision, 'order'] = c
        new_revision = df.loc[df['down_revision'] == revision]['revision'].values[0]
        find_revision(new_revision, df, c + 1)


if __name__ == '__main__':
    create_alembic_timeline()
