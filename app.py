#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Application"""

import os
from tkinter import Tk

import lib.global_variable as gv
from components import app_view

gv.init_global_variable()
gv.set_variable("APP_BUNDLE_ID", "org.crogram.blockchain-node")
gv.set_variable("APP_NAME", "区块链客户端GUI")
gv.set_variable("APP_PATH", os.path.dirname(__file__))  # 当前目录
gv.set_variable("APP_VERSION", "0.1.1")


class App(Tk):
    """Application Class"""

    def __init__(self):

        Tk.__init__(self)

        app_view.client(self)

        self.mainloop()


if __name__ == "__main__":
    App()
