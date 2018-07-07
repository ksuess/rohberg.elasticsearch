# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rohberg.elasticsearch


class RohbergElasticsearchLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=rohberg.elasticsearch)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rohberg.elasticsearch:default')


ROHBERG_ELASTICSEARCH_FIXTURE = RohbergElasticsearchLayer()


ROHBERG_ELASTICSEARCH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ROHBERG_ELASTICSEARCH_FIXTURE,),
    name='RohbergElasticsearchLayer:IntegrationTesting',
)


ROHBERG_ELASTICSEARCH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ROHBERG_ELASTICSEARCH_FIXTURE,),
    name='RohbergElasticsearchLayer:FunctionalTesting',
)


ROHBERG_ELASTICSEARCH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ROHBERG_ELASTICSEARCH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RohbergElasticsearchLayer:AcceptanceTesting',
)
