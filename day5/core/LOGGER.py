#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX


def userlog(user,msg):
    import logging
    log_dir = '../log/' + user + '.log'
    logger = logging.getLogger('../log/test1.log')
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler('../log/' + user + '.log')
    fh.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s -  %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.warning(msg)
