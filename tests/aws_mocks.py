# -*- coding: utf-8 -*-
class MockBatch(object):

    def __init__(self, paths):
        self.paths = paths

    def to_xml(self):
        return '<dumb><xml>Hi!</xml></dumb>'

class MockCloudFrontConnection(object):

    def create_invalidation_request(self, distribution_id, paths):
        return MockBatch(paths)
