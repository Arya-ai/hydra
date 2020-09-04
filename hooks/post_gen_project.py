import subprocess

def init_git():
    subprocess.call(['git', 'init'], stdout=subprocess.DEVNULL)


def add_all():
    subprocess.call(['git', 'add', '*'], stdout=subprocess.DEVNULL)


def commit():
    subprocess.call(['git', 'commit', '-m', 'Initial Commit'], stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    init_git()
    add_all()
    commit()
