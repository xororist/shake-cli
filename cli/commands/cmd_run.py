import click


@click.group()
def cli():
    pass


@cli.command()
def run():
    click.echo("Run command...")
