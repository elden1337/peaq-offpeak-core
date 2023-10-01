from multiprocessing import AuthenticationError
from datetime import datetime
import json
import asyncio
import aiohttp
from models.networkarea_dto import NetworkAreaDTO
from models.consumptionprofile_dto import ConsumptionProfileDTO, ConsumptionProfileModel
from const import *
    

async def get_network_areas():
    data = await _call(uri='GetNetworkAreas')
    ret = []
    for d in data:
        inst = NetworkAreaDTO.from_dict(d)
        ret.append(inst)
    return ret

async def get_consumption_profile(interval:int, startdate:datetime, enddate:datetime, biddingarea:int, networkareaid:str):
    params = {"interval":interval, "periodFrom":startdate.strftime("%Y-%m-%d"), "periodTo":enddate.strftime("%Y-%m-%d"), "biddingAreaId":biddingarea, "networkAreaId":networkareaid}
    data = await _call(uri='GetConsumptionProfile', params=params)
    ret = []
    for d in data:
        #print(d)
        inst = ConsumptionProfileDTO.from_dict(d)
        ret.append(inst)
    return ret
    

async def _call(uri, params=None):
    headers = {"Content-Type":"application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{ENDPOINT}{uri}", headers = headers, params=params) as response:
            try:
                ret = await response.json()
                return ret
            except:
                return 'Error!'


###move below to service layer###

async def update_consumption_profile() -> list[ConsumptionProfileModel]:
    _startdate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0, day=1)
    _enddate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    dto = await get_consumption_profile(interval=0, startdate=_startdate, enddate=_enddate, biddingarea=3, networkareaid='GBG')    
    ret = []
    for d in dto:
        inst = ConsumptionProfileModel.from_dto(d)
        if inst.Period.date() < _enddate.date():
            ret.append(inst)
    return ret

# if __name__ == "__main__":
#     ret = asyncio.run(get_network_areas())
#     for r in ret:
#         print(r)

if __name__ == "__main__":
    ret = asyncio.run(update_consumption_profile())
    ttt = {v.Period: v.Value for v in ret}
    print(ttt)
    # for r in ret:
    #     print(r)

