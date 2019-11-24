import click
import json
from .validate import validate_file
from .tree import Tree


@click.group()
@click.version_option()
def main():
    pass


@main.command()
@click.argument('file', type=click.Path(exists=True))
def validate(**kwargs):
    validate_file(kwargs['file'])


@main.command()
@click.argument('file', type=click.Path(exists=True))
def treejson(**kwargs):
    with open(kwargs['file']) as finance_file:
        data = json.load(finance_file)
    tree = Tree()
    tree.walk(data)
    print(tree.outstr)
