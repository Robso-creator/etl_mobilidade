import os

import alembic.config

from src.database.create_alembic_timeline import create_alembic_timeline


def test_forces_one_more_migration_to_find_missing_one():
    create_revision_cmd = f"revision --autogenerate -m 'testing'"

    cwd = os.getcwd()
    alembic.config.main(argv=f"--raiseerr -c {cwd}/alembic.ini {create_revision_cmd}".split(" "))

    path_alembic = os.path.join(cwd, 'src', 'database', 'alembic', 'versions')
    list_path_abs_versions = [os.path.join(path_alembic, _alembic_version) for _alembic_version in
                              os.listdir(path_alembic)]
    # get rid of __pycache__
    list_path_abs_versions = [_full_path_alembic_version for _full_path_alembic_version in list_path_abs_versions if
                              _full_path_alembic_version.endswith('.py')]
    df_migrations = create_alembic_timeline(verbose=False)
    last_number_revision = df_migrations['order'].max()
    last_revision_file = df_migrations.query("order==@last_number_revision")['file'].values[0]
    path_abs_last_revision_file = ''
    for _file_abs in list_path_abs_versions:
        if last_revision_file in _file_abs:
            path_abs_last_revision_file = _file_abs

    with open(path_abs_last_revision_file, 'r') as f:
        len_new_revision = len(f.readlines())

    try:
        assert len_new_revision == 30, "Missing migration!!"
    finally:
        # delete files
        print('deleting file -->', path_abs_last_revision_file)
        os.remove(path_abs_last_revision_file)
