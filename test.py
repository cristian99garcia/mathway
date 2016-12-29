#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016, Cristian García <cristian99garcia@gmail.com>
#
# This library is free software you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from mathway import FirstDegreeEquation


def equation_degree1():
    formula = "3x - 1"
    eq = FirstDegreeEquation.new_from_string(formula)
    steps = eq.solve_step_by_step()
    print "Solve: " + eq.get_expression()
    print "Solutions set: {", str(eq.solve()[0]), "}"
    for step in steps:
        print step


tests = {
    equation_degree1: True
}


for test in tests.keys():
    if tests[test]:
        test()
