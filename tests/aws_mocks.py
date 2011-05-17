# -*- coding: utf-8 -*-
class MockBatch(object):

    def __init__(self, paths):
        self.paths = paths

    def to_xml(self):
        return '<dumb><xml>Hi!</xml></dumb>'

class MockDistributionSummary(object):

    def __init__(self, id, cname):
        self.id = id
        self.cnames = (cname,)

class MockCloudFrontConnection(object):

    def create_invalidation_request(self, distribution_id, paths):
        return MockBatch(paths=paths)

    def get_all_distributions(self):
        return [
            MockDistributionSummary(id='XUUS9933', cname='static.domain.com'),
            MockDistributionSummary(id='XUUS9934', cname='cdn.domain.uk'),
        ]
