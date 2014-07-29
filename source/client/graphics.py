# Imperialism remake
# Copyright (C) 2014 Trilarion
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

from PySide import QtGui, QtCore

import tools as t
import lib.graphics as g


class GameDialog(QtGui.QWidget):
    def __init__(self, parent, content, title=None, modal=False, delete_on_close=False, help_callback=None,
                 close_callback=None):
        super().__init__(parent, f=QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)

        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setObjectName('gamedialog')

        # should be deleted on close
        if delete_on_close:
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # default state is Qt.NonModal
        if modal:
            self.setWindowModality(QtCore.Qt.WindowModal)

        # title bar
        title_bar = g.DraggableToolBar()
        title_bar.setIconSize(QtCore.QSize(20, 20))
        title_bar.setObjectName('titlebar')
        title_bar.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        title_bar.dragged.connect(lambda delta: self.move(self.pos() + delta))

        # title in titlebar and close icon
        title = QtGui.QLabel(title)
        title.setObjectName('gamedialog-title')
        title_bar.addWidget(title)

        spacer = QtGui.QWidget()
        spacer.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        title_bar.addWidget(spacer)

        if help_callback:
            help_action = QtGui.QAction(t.load_ui_icon('icon.help.png'), 'Help', title_bar)
            help_action.triggered.connect(help_callback)
            title_bar.addAction(help_action)

        self.close_callback = close_callback

        close_action = QtGui.QAction(t.load_ui_icon('icon.close.png'), 'Close', title_bar)
        close_action.triggered.connect(self.close)
        title_bar.addAction(close_action)

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setContentsMargins(2, 2, 2, 2)
        self.layout.addWidget(title_bar)
        self.layout.addWidget(content)

    def closeEvent(self, event):
        """
            To prevent Alt+F4 or other automatic closes.
        :param event:
        :return:
        """
        if self.close_callback and not self.close_callback(self):
            event.ignore()