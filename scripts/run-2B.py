# SPDX-FileCopyrightText: 2024-present Jason W. DeGraw <jason.degraw@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
import requests
import os

idf_file = 'C:\\EnergyPlusV22-2-0\\ExampleFiles\\5ZoneCoolBeam.idf'
epw_file = 'USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw'
run_base_dir = 'C:\\Users\\jason\\eps-run' # this one exists
run_dir = os.path.join(run_base_dir, '2B')
os.mkdir(run_dir)

inputs = {'idf': idf_file, 'epw': epw_file, 'run_dir': run_dir}

r = requests.post('http://127.0.0.1:5000/run', data=inputs)

print('Done!')