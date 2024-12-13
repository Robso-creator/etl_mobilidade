import os

import alembic.config

from src.database.create_alembic_timeline import create_alembic_timeline
from src.database.create_revisions import main as create_revisions

cwd = os.getcwd()


def alembic_cmd(cmd):
    alembic.config.main(argv=f'--raiseerr -c {cwd}/alembic.ini {cmd}'.split(' '))


def downgrade_n_revision(n=1):
    alembic_cmd(cmd=f'downgrade -{n}')


def upgrade_head():
    alembic_cmd(cmd='upgrade head')


def exclude_last_revision():
    path_alembic = os.path.join(cwd, 'src', 'database', 'alembic', 'versions')
    list_path_abs_versions = [os.path.join(path_alembic, _alembic_version) for _alembic_version in os.listdir(path_alembic)]
    # get rid of __pycache__
    list_path_abs_versions = [_full_path_alembic_version for _full_path_alembic_version in list_path_abs_versions if _full_path_alembic_version.endswith('.py')]
    df_migrations = create_alembic_timeline(verbose=False)
    last_number_revision = df_migrations['order'].max()
    last_revision_file = df_migrations.loc[df_migrations['order'] == last_number_revision]['file'].values[0]

    last_abs_revision_path = [_file for _file in list_path_abs_versions if _file.endswith(last_revision_file)][0]

    print(f'{last_revision_file=}... deleting')
    os.remove(last_abs_revision_path)
    print(f'{last_revision_file=}... deleted')


def redo_last_upgrade():
    print('downgrading last revision')
    downgrade_n_revision(1)
    print('last revision downgraded')

    exclude_last_revision()

    print('creating revision again...')
    create_revisions()
    print('revision created...')

    print('upgrading head')
    upgrade_head()
    print('head upgraded')


if __name__ == '__main__':
    redo_last_upgrade()
