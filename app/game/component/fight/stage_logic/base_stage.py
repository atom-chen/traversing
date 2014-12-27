#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BaseStageLogic(object):
    """docstring for BaseStage 基类"""
    def __init__(self, player, stage_id):
        super(BaseStageLogic, self).__init__()
        self._stage_id = stage_id
        self._player = player

    @property
    def stage_id(self):
        return self._stage_id


    def check(self):
        return {'result': True}