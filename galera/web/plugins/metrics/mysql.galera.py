#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

unit_info["galera_cluster_size"] = {
    "title"  : "",
    "description" : _("Floating point number"),
    "symbol" : "",
    "render" : lambda v: render_scientific(v, 0),
}

metric_info["galera_cluster_size"] = {
  "title" : _("Number of nodes in Cluster"),
  "color" : "#80ff40",
  "unit"  : "galera_cluster_size",
}

check_metrics["check_mk-mysql.galera_cluster_size"] = {
  "galera_cluster_size": { "name": "galera_cluster_size" },
}
