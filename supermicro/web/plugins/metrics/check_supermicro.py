#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

metric_info["memory_eccerrorcount"] = {
  "title" : _("Failure ECC error count"),
  "color": "23/a",
  "unit"  : "count",
}

metric_info["memory_ueccerrorcount"] = {
  "title" : _("Uncorrectable ECC error count"),
  "color": "13/a",
  "unit"  : "count",
}

graph_info.append({
  "title" : _("Memory error count"),
  "metrics" : [
    ( "memory_ueccerrorcount", "line" ),
    ( "memory_eccerrorcount", "line" ),
  ]
})

check_metrics["check_mk-supermicro.mem"] = {
  "eccerrorcount": { "name": "memory_eccerrorcount", "auto_graph" : False },
  "ueccerrorcount" : { "name": "memory_ueccerrorcount", "auto_graph" : False },
}
