{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
from pprint import pprint
from jnpr.healthbot.swagger.models.hb_graphs_query import HbGraphsQuery
from jnpr.healthbot.swagger.models.hb_graphs import HbGraphs
from jnpr.healthbot import PINClient

ip = 'ip'
gui_username = 'admin'
gui_password = 'pwd'


with PINClient(ip, gui_username, gui_password, port=8080) as pin:
    # Adding a new canvas
    # group_name, device_name, measurement_name, field_name are compulsory fields here
    query1 = HbGraphsQuery(group_name='dg-junos', device_name="d2", measurement_name="system.commit/commit-history",
                           transformation=None, field_name="l1-threshold", field_aggregation="mean",
                           where=[{'key': "comment", "operator": '=', "value": "new"}],
                           group_by_interval="1s", group_by_fill="fill(null)", group_by_tag_key=[])
    # Multiple queries can be present for a graph
    # graph_name, graph_type, time_range are compulsory here
    graph1 = HbGraphs(graph_name="graph1", graph_description=None, graph_type="Heatmap",
                      time_range='3h', query=[query1], y_label=None, y_max=None,
                      y_min=None, unit_type=None, decimals=None)
    # Multiple graphs can be present for a canvas
    # Adding a new canvas with a single graph
    pin.charts.add_canvas(canvas_name="mycanvas", graphs=[graph1])
    pin.commit()

    # Updating an existing canvas
    # Edit an existing graph
    query1 = HbGraphsQuery(group_name='dg-junos', device_name="d2", measurement_name="system.commit/commit-history",
                           transformation=None, field_name="l1-threshold", field_aggregation="mean",
                           where=[{'key': "comment", "operator": '!=', "value": "new"}],
                           group_by_interval="1s", group_by_fill="fill(null)", group_by_tag_key=[])
    graph1 = HbGraphs(graph_name="graph1", graph_description=None, graph_type="Time Series",
                      time_range='3h', query=[query1])
    pin.charts.update_canvas(canvas_name="mycanvas", graphs=[graph1])
    pin.commit()

    # Add a new graph
    graph2 = HbGraphs(graph_name="graph2", graph_description=None, graph_type="Time Series",
                      time_range='3h')
    pin.charts.update_canvas(canvas_name="mycanvas", graphs=[graph1, graph2])
    pin.commit()

    # Delete a graph from a canvas
    pin.charts.update_canvas(canvas_name="mycanvas", graphs=[graph2])
    pin.commit()

    # Getting canvas details
    pprint(pin.charts.get_canvas("mycanvas"))

    # Deleting an canvas
    pin.charts.delete_canvas(canvas_name="mycanvas")
    pin.commit()

