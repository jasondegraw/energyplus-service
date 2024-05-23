# SPDX-FileCopyrightText: 2024-present Jason W. DeGraw <jason.degraw@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
import pytest
import tempfile
import json
import os
from energyplus_service import create_app

@pytest.fixture
def app():

    temporary_dir = tempfile.TemporaryDirectory()

    # This is not great, need a mechanism that works better
    conf = {}
    if os.path.exists('tests\config.json'):
        with open('tests\config.json') as fp:
            conf = json.load(fp)
    
    conf['TESTING'] = True
    conf['RUN_DIRECTORY'] = temporary_dir.name

    app = create_app(conf)

    yield app

    temporary_dir.cleanup()

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()