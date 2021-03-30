"""A sample CLI."""

import click
import log

from meddra_toolkit.clilib.printers import *
from meddra_toolkit.meddra import MeddraData, VERSION_24_0_FR


@click.command()
@click.argument('term')
@click.option(
    '--regex',
    '-r',
    is_flag=True,
    help="consider the search term as a regular expression",
)
@click.option(
    '--hierarchy', '-h', is_flag=True, help="print term hierarchy (not in CSV format)"
)
@click.option(
    '--printer',
    '-p',
    type=click.Choice(['formatted', 'csv', 'json', 'pretty_json']),
    default="formatted",
    help="output format",
)
def main(term, regex=False, hierarchy=False, printer="formatted"):
    """Search TERM in Meddra terminology."""
    log.init()

    med = MeddraData(VERSION_24_0_FR)
    med.load()

    results = med.find(term, regex=regex)

    printer_impl = FormattedPrinter(hierarchy)
    if printer == "csv":
        printer_impl = CSVPrinter()
    if printer == "json":
        printer_impl = JSONPrinter()
    if printer == "pretty_json":
        printer_impl = JSONPrinter(pretty=True)

    for f in results:
        printer_impl.onResult(f)

    final_output = printer_impl.output()
    if final_output:
        print(final_output)


if __name__ == '__main__':  # pragma: no cover
    main()
