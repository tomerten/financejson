import click
import json
from .validate import validate_file
from .tree import Tree
from .convert import convert_file


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


@main.command()
@click.argument('file', type=click.Path(exists=True))
@click.argument('input_format')
@click.argument('output_format')
def convert(**kwargs):
    convert_file(kwargs['file'], kwargs['input_format'], kwargs['output_format'])
