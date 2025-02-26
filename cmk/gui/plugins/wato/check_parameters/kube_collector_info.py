#!/usr/bin/env python3
# Copyright (C) 2022 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _
from cmk.gui.plugins.wato.utils import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)
from cmk.gui.valuespec import Dictionary, MonitoringState


def _parameter_valuespec():
    return Dictionary(
        elements=[
            (
                "machine_metrics",
                MonitoringState(
                    title=_(
                        ("Monitoring state if the Cluster Collector reports no Machine Metrics")
                    ),
                    default_value=2,
                ),
            ),
        ],
        required_keys=["machine_metrics"],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name="kube_collector_info",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec,
        title=lambda: _("Kubernetes Collector Info"),
    )
)
