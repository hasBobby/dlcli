from ..cli import *
from ..api import *
import sys
import click
import logging


logger = logging.getLogger(__name__)

from ..api import rules as rules_api

@cli.group('mute')
def mute():
    """mutes rules"""


@click.command(short_help="Mute all rules")
def all():
    for r in rules_api.get_rules(**context.settings):
        rules_api.mute_rule(rule=r['name'], **context.settings)


@click.command(short_help="Backup an Organization")
@click.argument('name')
def rule(name):
    rules_api.mute_rule(rule=name, **context.settings)


mute.add_command(all)
mute.add_command(rule)

