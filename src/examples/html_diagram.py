import json
import math

from org.eclipse.swt import SWT
from org.eclipse.swt.browser import Browser
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.widgets import Display, Shell


def get_flow(name):  # type: (str) -> Flow
    """
    Get the flow `Emission to air / unspecified / Chromium ...` from the
    database.
    """
    flows = FlowDao(db).getForName(name)
    for flow in flows:
        c = flow.category
        if c is None or c.name != "unspecified":
            continue
        c = c.category
        if c is None or c.name != "Emission to air":
            continue
        return flow


def get_results():  # type: () -> List[List[float or str]]
    """
    Get the values for the flow from the process inputs and outputs and
    transform them: f(x) = log10(x * 1e15).
    """
    results = []

    chrom3 = get_flow("Chromium III")
    results.append(collect_amounts(chrom3))

    chrom6 = get_flow("Chromium VI")
    results.append(collect_amounts(chrom6))

    return [list(row) for row in zip(*results)]


def collect_amounts(flow):  # type: (Flow) -> List[float or str]
    results = [flow.name]

    def collect_results(record):
        results.append(math.log10(record.getDouble(1) * 1e15))
        return True

    print("Collecting results for {name}".format(**{"name": flow.name}))
    query = (
        "SELECT resulting_amount_value FROM tbl_exchanges WHERE f_flow = %i AND is_input = 0"
        % flow.id
    )
    NativeSql.on(db).query(query, collect_results)

    print("{size} results collected".format(**{"size": len(results) - 1}))

    return results


def make_html(results):  # type: (List[List[float or str]]) -> str
    """Generate the HTML page for the data."""

    html = """<html>
    <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
        google.charts.load("current", {packages:["corechart"]});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {
            var data = google.visualization.arrayToDataTable(%s);

            var options = {
                title: 'Chromium Emission Levels',
                legend: { position: 'bottom' },
                hAxis: {
                    title: 'log(amount × 1e15)',
                    ticks: [%s]
                },
                vAxis: {
                    title: 'Number of exchanges'
                }
            };

            var chart = new google.visualization.Histogram(
                document.getElementById('chart_div')
            );
            chart.draw(data, options);
        }
        </script>
    </head>
    <body>
        <div id="chart_div" style="width: 900px; height: 500px;"></div>
    </body>
    </html>
    """ % (
        json.dumps(results),
        ", ".join(str(x) for x in range(-3, 16)),
    )
    return html


def main():
    """
    Create the results, HTML, and window with the Browser and set the HTML
    content of the Browser.
    """
    results = get_results()
    html = make_html(results)

    shell = Shell(Display.getDefault())
    shell.setText("Chromium VI")
    shell.setLayout(FillLayout())
    browser = Browser(shell, SWT.NONE)
    browser.setText(html)

    shell.open()


App.runInUI("Visualizing Chromium Emission Levels", main)
