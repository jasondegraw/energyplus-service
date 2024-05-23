# SPDX-FileCopyrightText: 2024-present Jason W. DeGraw <jason.degraw@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
import tempfile
import os
import shutil

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
idf_file = os.path.join(script_dir, '..', 'resources', '5ZoneAirCooled.idf') 
epw_file = os.path.join(script_dir, '..', 'resources', 'USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw')

def test_local_run(client):
    with tempfile.TemporaryDirectory() as temporary_dir:
        response = client.post('/local/run', json={'idf': idf_file, 'epw': epw_file, 'run_dir': temporary_dir})
        assert response

def test_local_in(client):
    with tempfile.TemporaryDirectory() as temporary_dir:
        shutil.copy(idf_file, os.path.join(temporary_dir, 'in.idf'))
        shutil.copy(epw_file, os.path.join(temporary_dir, 'in.epw'))
        response = client.post('/local/in', json={'run_dir': temporary_dir})
        assert response