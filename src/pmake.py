from pathlib import Path
import shutil
import shlex
import asyncio
import pprint

import click


def get_base_path_from_venv() -> Path:
    parts = []
    for part in Path(__file__).parts:
        if part.lower() in ['venv', 'env', '.venv', '.env', 'venv.bak', 'env.bak']:
            break
        parts.append(part)
    else:
        return Path(__file__).parent.parent.resolve()

    if not parts:
        raise ValueError("Could not get the base folder path")

    return Path("\\".join(parts)).resolve()


async def run(cmd: str):
    path = get_base_path_from_venv()

    proc = await asyncio.create_subprocess_shell(cmd, cwd=path)
    _ = await proc.communicate()


def clean(*args, **kwargs) -> None:
    """Delete all gen/build files

    - public/
    - static/data
    """
    pass


def npm_install(*args, **kwargs) -> None:
    """Setup npm modules"""
    cmd = shlex.split('npm install -D tailwindcss@latest postcss@latest autoprefixer@latest @tailwindcss/typography@latest')
    cmd[0] = f'"{shutil.which(cmd[0])}"'
    cmd = ' '.join(cmd)

    return cmd


def tailwind(*args, **kwargs) -> None:
    """Launch watcher process"""
    cmd = shlex.split('npx tailwindcss --input ./src/tailwind.css --output ./static/css/tailwind.css --watch')
    cmd[0] = f'"{shutil.which(cmd[0])}"'
    cmd = ' '.join(cmd)

    return cmd


def zola(drafts: bool=False, *args, **kwargs) -> None:
    """Serve zola process"""
    cmd = shlex.split('zola serve --interface 127.0.0.1 --base-url 127.0.0.1 --open')
    cmd[0] = f'"{shutil.which(cmd[0])}"'

    if drafts:
        cmd.append('--drafts')

    cmd = ' '.join(cmd)

    return cmd


async def main(cmds: list[list[str]]):
    await asyncio.gather(*[run(cmd) for cmd in cmds])


@click.command()
@click.argument('cmd_args', nargs=-1)
def make(cmd_args):
    if not cmd_args:
        print("make [clean] [tailwind] [zola[+drafts]]")

    cmds = []

    for cmd in cmd_args:
        args = []
        kwargs = {}
        if '+' in cmd:
            cmd, *args = cmd.split('+')
            kwargs |= {x: True for x in args}

        func = globals().get(cmd)

        if func is not None and callable(func):
            print(f"Running {cmd} with {kwargs!s}")
            cmd = func(**kwargs)
            if cmd is not None:
                cmds.append(cmd)

    asyncio.run(main(cmds))