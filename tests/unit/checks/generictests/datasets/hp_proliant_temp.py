#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# type: ignore
checkname = 'hp_proliant_temp'

info = [
    ['1', '11', '27', '45', '2'], ['2', '6', '40', '70', '2'],
    ['3', '6', '40', '70', '2'], ['4', '7', '33', '87', '2'],
    ['5', '7', '34', '87', '2'], ['6', '7', '36', '80', '2'],
    ['7', '7', '36', '80', '2'], ['8', '7', '36', '80', '2'],
    ['9', '7', '36', '80', '2'], ['10', '7', '36', '80', '2'],
    ['11', '7', '36', '80', '2'], ['12', '3', '35', '60', '2'],
    ['13', '3', '50', '105', '2'], ['14', '3', '41', '95', '2'],
    ['15', '10', '35', '0', '2'], ['16', '10', '34', '0', '2'],
    ['17', '10', '36', '80', '2'], ['18', '10', '36', '80', '2'],
    ['19', '3', '35', '115', '2'], ['20', '3', '35', '115', '2'],
    ['21', '3', '35', '115', '2'], ['22', '3', '35', '115', '2'],
    ['23', '3', '30', '65', '2'], ['26', '3', '42', '100', '2'],
    ['27', '3', '40', '100', '2'], ['28', '3', '37', '90', '2'],
    ['31', '5', '85', '100', '2'], ['35', '5', '35', '67', '2'],
    ['36', '5', '37', '67', '2'], ['37', '5', '37', '67', '2'],
    ['38', '5', '36', '67', '2'], ['41', '3', '39', '90', '2'],
    ['42', '3', '38', '90', '2'], ['43', '3', '40', '90', '2'],
    ['46', '8', '36', '65', '2'], ['47', '8', '36', '65', '2'],
    ['48', '12', '40', '90', '2'], ['49', '12', '38', '90', '2'],
    ['50', '3', '32', '60', '2'],
    ['51', '3', '0', '60', '1'],
]

discovery = {
    '': [
        ('1 (ambient)', {}), ('10 (memory)', {}), ('11 (memory)', {}),
        ('12 (system)', {}), ('13 (system)', {}), ('14 (system)', {}),
        ('15 (powerSupply)', {}), ('16 (powerSupply)', {}),
        ('17 (powerSupply)', {}), ('18 (powerSupply)', {}),
        ('19 (system)', {}), ('2 (cpu)', {}), ('20 (system)', {}),
        ('21 (system)', {}), ('22 (system)', {}), ('23 (system)', {}),
        ('26 (system)', {}), ('27 (system)', {}), ('28 (system)', {}),
        ('3 (cpu)', {}), ('31 (ioBoard)', {}), ('35 (ioBoard)', {}),
        ('36 (ioBoard)', {}), ('37 (ioBoard)', {}), ('38 (ioBoard)', {}),
        ('4 (memory)', {}), ('41 (system)', {}), ('42 (system)', {}),
        ('43 (system)', {}), ('46 (storage)', {}), ('47 (storage)', {}),
        ('48 (chassis)', {}), ('49 (chassis)', {}), ('5 (memory)', {}),
        ('50 (system)', {}), ('6 (memory)', {}), ('7 (memory)', {}),
        ('8 (memory)', {}), ('9 (memory)', {})
    ]
}

checks = {
    '': [
        (
            '1 (ambient)', {}, [
                (0, '27.0 °C', [('temp', 27.0, 45.0, 45.0, None, None)])
            ]
        ),
        (
            '10 (memory)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 80.0, 80.0, None, None)])
            ]
        ),
        (
            '11 (memory)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 80.0, 80.0, None, None)])
            ]
        ),
        (
            '12 (system)', {}, [
                (0, '35.0 °C', [('temp', 35.0, 60.0, 60.0, None, None)])
            ]
        ),
        (
            '13 (system)', {}, [
                (0, '50.0 °C', [('temp', 50.0, 105.0, 105.0, None, None)])
            ]
        ),
        (
            '14 (system)', {}, [
                (0, '41.0 °C', [('temp', 41.0, 95.0, 95.0, None, None)])
            ]
        ),
        (
            '15 (powerSupply)', {}, [
                (0, '35.0 °C', [('temp', 35.0, None, None, None, None)])
            ]
        ),
        (
            '16 (powerSupply)', {}, [
                (0, '34.0 °C', [('temp', 34.0, None, None, None, None)])
            ]
        ),
        (
            '17 (powerSupply)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 80.0, 80.0, None, None)])
            ]
        ),
        (
            '18 (powerSupply)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 80.0, 80.0, None, None)])
            ]
        ),
        (
            '19 (system)', {}, [
                (0, '35.0 °C', [('temp', 35.0, 115.0, 115.0, None, None)])
            ]
        ),
        (
            '2 (cpu)', {}, [
                (0, '40.0 °C', [('temp', 40.0, 70.0, 70.0, None, None)])
            ]
        ),
        (
            '20 (system)', {}, [
                (0, '35.0 °C', [('temp', 35.0, 115.0, 115.0, None, None)])
            ]
        ),
        (
            '21 (system)', {}, [
                (0, '35.0 °C', [('temp', 35.0, 115.0, 115.0, None, None)])
            ]
        ),
        (
            '22 (system)', {}, [
                (0, '35.0 °C', [('temp', 35.0, 115.0, 115.0, None, None)])
            ]
        ),
        (
            '23 (system)', {}, [
                (0, '30.0 °C', [('temp', 30.0, 65.0, 65.0, None, None)])
            ]
        ),
        (
            '26 (system)', {}, [
                (0, '42.0 °C', [('temp', 42.0, 100.0, 100.0, None, None)])
            ]
        ),
        (
            '27 (system)', {}, [
                (0, '40.0 °C', [('temp', 40.0, 100.0, 100.0, None, None)])
            ]
        ),
        (
            '28 (system)', {}, [
                (0, '37.0 °C', [('temp', 37.0, 90.0, 90.0, None, None)])
            ]
        ),
        (
            '3 (cpu)', {}, [
                (0, '40.0 °C', [('temp', 40.0, 70.0, 70.0, None, None)])
            ]
        ),
        (
            '31 (ioBoard)', {}, [
                (0, '85.0 °C', [('temp', 85.0, 100.0, 100.0, None, None)])
            ]
        ),
        (
            '35 (ioBoard)', {}, [
                (0, '35.0 °C', [('temp', 35.0, 67.0, 67.0, None, None)])
            ]
        ),
        (
            '36 (ioBoard)', {}, [
                (0, '37.0 °C', [('temp', 37.0, 67.0, 67.0, None, None)])
            ]
        ),
        (
            '37 (ioBoard)', {}, [
                (0, '37.0 °C', [('temp', 37.0, 67.0, 67.0, None, None)])
            ]
        ),
        (
            '38 (ioBoard)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 67.0, 67.0, None, None)])
            ]
        ),
        (
            '4 (memory)', {}, [
                (0, '33.0 °C', [('temp', 33.0, 87.0, 87.0, None, None)])
            ]
        ),
        (
            '41 (system)', {}, [
                (0, '39.0 °C', [('temp', 39.0, 90.0, 90.0, None, None)])
            ]
        ),
        (
            '42 (system)', {}, [
                (0, '38.0 °C', [('temp', 38.0, 90.0, 90.0, None, None)])
            ]
        ),
        (
            '43 (system)', {}, [
                (0, '40.0 °C', [('temp', 40.0, 90.0, 90.0, None, None)])
            ]
        ),
        (
            '46 (storage)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 65.0, 65.0, None, None)])
            ]
        ),
        (
            '47 (storage)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 65.0, 65.0, None, None)])
            ]
        ),
        (
            '48 (chassis)', {}, [
                (0, '40.0 °C', [('temp', 40.0, 90.0, 90.0, None, None)])
            ]
        ),
        (
            '49 (chassis)', {}, [
                (0, '38.0 °C', [('temp', 38.0, 90.0, 90.0, None, None)])
            ]
        ),
        (
            '5 (memory)', {}, [
                (0, '34.0 °C', [('temp', 34.0, 87.0, 87.0, None, None)])
            ]
        ),
        (
            '50 (system)', {}, [
                (0, '32.0 °C', [('temp', 32.0, 60.0, 60.0, None, None)])
            ]
        ),
        (
            '6 (memory)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 80.0, 80.0, None, None)])
            ]
        ),
        (
            '7 (memory)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 80.0, 80.0, None, None)])
            ]
        ),
        (
            '8 (memory)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 80.0, 80.0, None, None)])
            ]
        ),
        (
            '9 (memory)', {}, [
                (0, '36.0 °C', [('temp', 36.0, 80.0, 80.0, None, None)])
            ]
        )
    ]
}
