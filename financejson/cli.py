import click
from .validate import validate_file


@click.group()
@click.version_option()
def main():
    pass


@main.command()
@click.argument('file', type=click.Path(exists=True))
def validate(**kwargs):
    validate_file(kwargs['file'])
