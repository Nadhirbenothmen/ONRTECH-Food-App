# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from src.utils.appium_utils import setup_logging
sys.path.append('src')
from typing import Final
from src.utils.my_utils import DriverConfig
import logging
webdriverInstance: Final[str] = DriverConfig.getDriver(DriverConfig.DriverType.CHROME)
URL_BASE_CARREFOUR: Final[str] = "https://www.compraonline.alcampo.es/"
path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'logs'))
filename = os.path.basename(sys.argv[0]).replace(".py", "")
setup_logging(path=path, filename=filename, force_override_existing_setup=True)
logging.info("initiating logging info...")
logging.critical("initiating logging critical...")
logging.fatal("initiating logging fatal...")
logging.error("initiating logging error...")
