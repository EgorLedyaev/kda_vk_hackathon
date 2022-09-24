""" Request Model """

from masoniteorm.models import Model


class Request(Model):
    """Request Model"""
    
    __table__ = "requests"
    __fillable__ = ['id', 'predit', 'input_json', 'output_json']
    pass
