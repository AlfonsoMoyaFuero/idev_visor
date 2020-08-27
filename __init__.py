# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Idev
                                 A QGIS plugin
 Infraestructura Valenciana de Dades Espacials
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-08-13
        copyright            : (C) 2020 by Alfonso Moya Fuero
        email                : moya_alf@gva.es
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Idev class from file Idev.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .idev_visor import Idev
    return Idev(iface)
