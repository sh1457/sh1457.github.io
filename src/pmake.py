from pathlib import Path
import subprocess

import click


def get_base_path_from_venv() -> Path:
    parts = []
    for part in Path(__file__).parts:
        if part.lower() in ['venv', 'env', '.venv', '.env', 'venv.bak', 'env.bak']:
            break
        parts.append(part)

    if not parts:
        raise ValueError("Could not get the base folder path")

    return Path("\\".join(parts)).resolve()


def clean(path: Path, *args, **kwargs) -> None:
    """Delete all gen/build files

    - public/
    - static/data
    """
    pass


def npm_install(path: Path, *args, **kwargs) -> None:
    cmd = ['npm', 'install', '-D',
           'tailwindcss@latest',
           'postcss@latest',
           'autoprefixer@latest',
           '@tailwindcss/typography@latest']

    subprocess.run(cmd, cwd=path, shell=True)


def tailwind(path: Path, *args, **kwargs) -> None:
    """Launch watcher process"""

    cmd = ['npx', 'tailwindcss',
           '--input', './src/tailwind.css',
           '--output', './static/css/tailwind.css',
           '--watch']

    subprocess.run(cmd, cwd=path, shell=True)


def zola(path: Path, drafts: bool = False, *args, **kwargs) -> None:
    """Serve zola process"""
    cmd = ['zola', 'serve',
           '--interface', '127.0.0.1',
           '--base-url', '127.0.0.1',
           '--open']

    if drafts:
        cmd.append('--drafts')

    subprocess.run(cmd, cwd=path, shell=True)


@click.command()
@click.argument('cmd_args', nargs=-1)
def make(cmd_args):
    path = get_base_path_from_venv()

    if not cmd_args:
        print("make [tailwind|zola[+drafts]|clean]")

    for cmd in cmd_args:
        args = []
        kwargs = {"path": path}
        if '+' in cmd:
            cmd, *args = cmd.split('+')
            kwargs |= {x: True for x in args}

        func = globals().get(cmd)

        if func is not None and callable(func):
            print(f"Running {cmd} with {kwargs!s}")
            func(**kwargs)
