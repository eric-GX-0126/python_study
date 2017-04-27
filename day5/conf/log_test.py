#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

import logging
import logging.config

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('eric')

logger.debug('haha')

