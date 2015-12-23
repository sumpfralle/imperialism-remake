#!/usr/bin/python3
# Imperialism remake
# Copyright (C) 2015 Spitaels <spitaelsantoine@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from unit.LandUnitType import LandUnitType
from nation.nation import Nation


class LandUnit:
    """Class LandUnit
    """
    # Attributes:
    unitStrength = [0, 100]  # (int)
    experienceLevel = [1, 5]  # (int)
    graphicCharge = None  # (QPixmap)
    graphicShoot = None  # (QPixmap)
    graphicStand = None  # (QPixmap)

    # Operations
    def increase_experience_level(self):
        """function increase_experience_level

        returns boolean
        """
        raise NotImplementedError()
        return None

    def draw(self, defending, scene, size):
        """function draw

        defending: boolean
        scene: QGraphicsScene
        size: QSize

        returns
        """
        raise NotImplementedError()
        return None
