import subprocess


def main():
    git_branch = subprocess.run(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
        capture_output=True,
        text=True,
    ).stdout.strip()

    create_revision_cmd = f"alembic revision --autogenerate -m '{git_branch}'"
    return_crc = subprocess.Popen(create_revision_cmd.split())
    return_crc.communicate()


if __name__ == '__main__':
    main()
