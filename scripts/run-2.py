# SPDX-FileCopyrightText: 2024-present Jason W. DeGraw <jason.degraw@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause
import os
import asyncio
import httpx
import time

idf_files = ['C:\\EnergyPlusV22-2-0\\ExampleFiles\\5ZoneAirCooled.idf',
             'C:\\EnergyPlusV22-2-0\\ExampleFiles\\5ZoneCoolBeam.idf',
             'C:\\EnergyPlusV22-2-0\\ExampleFiles\\AirflowNetwork_MultiZone_SmallOffice.idf',
             'C:\\EnergyPlusV22-2-0\\ExampleFiles\\CoolingTower.idf',
             'C:\\EnergyPlusV22-2-0\\ExampleFiles\\1ZoneUncontrolled.idf',
             'C:\\EnergyPlusV22-2-0\\ExampleFiles\\AirCooledElectricChiller.idf']
epw_file = 'C:\\EnergyPlusV22-2-0\\WeatherData\\USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw'
run_base_dir = 'C:\\Users\\jason\\eps-run' # this one exists
run_dirs = [os.path.join(run_base_dir, '3%s'%el) for el in ['A', 'B', 'C', 'D', 'E', 'F']]
for el in run_dirs:
    os.mkdir(el)

data = [{'idf': idf, 'epw': epw_file, 'run_dir': dir} for idf,dir in zip(idf_files, run_dirs)]

async def run():
    async with httpx.AsyncClient() as client:
        tasks = [client.post('http://127.0.0.1:5000/run', data=inputs, timeout=None) for inputs in data]
        result = await asyncio.gather(*tasks)
        return result

start = time.time()
result = asyncio.run(run())
delta = time.time() - start

print('Done! (%s seconds)' % delta)
for el in result:
    print(el.status_code, el.text)