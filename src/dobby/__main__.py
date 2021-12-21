import subprocess

import click


def clean():
    """Delete all gen/build files

    - public/
    - static/data
    """
    pass


def tailwind():
    """Launch watcher process"""
    from pathlib import Path
    path = str(Path(__file__).parent.parent.parent.resolve())

    print(path)

    cmd = ['tailwindcss',
           '--input', './src/tailwind.css',
           '--output', './static/css/tailwind.css',
           '--watch'
          ]

    subprocess.run(cmd, cwd=path, shell=True)


def zola():
    """Serve zola process"""
    cmd = ['zola', 'serve', '--open']

    subprocess.run(cmd)


def all():
    """Perfrom all actions"""
    clean()
    tailwind()
    zola()


@click.command()
@click.argument('cmds', nargs=-1)
def pmake(cmds):
    if not cmds:
        cmds = ("all",)

    for cmd in cmds:
        func = globals().get(cmd)

        if func is not None and callable(func):
            print(f"Running {cmd}")
            func()
