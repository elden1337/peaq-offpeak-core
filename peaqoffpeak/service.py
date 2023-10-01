from datetime import datetime, timedelta
import svk_repository as repo
from models.consumptionprofile_model import ConsumptionProfileModel
from models.networkarea_model import NetWorkAreaModel

from dataclasses import dataclass, field

@dataclass
class UpdateConsumptionProfileRq:        
    networkareaid:str = field(default=None)
    startdate:datetime = field(default=datetime.now() - timedelta(days=7))
    enddate:datetime = field(default=datetime.now())
    biddingarea:int = field(default=0)
    interval:int = field(default=0)
    
    def __post_init__(self):
        assert self.interval in [0,1]
        self.startdate = self.startdate.replace(hour=0, minute=0, second=0, microsecond=0)
        self.enddate = self.enddate.replace(hour=0, minute=0, second=0, microsecond=0)


async def get_network_areas() -> list[NetWorkAreaModel]:
    dto = await repo.get_network_areas()
    ret = []
    for d in dto:
        inst = NetWorkAreaModel.from_dto(d)
        ret.append(inst)
    return ret

async def get_consumption_profile(request: UpdateConsumptionProfileRq) -> list[ConsumptionProfileModel]:    
    _enddate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    dto = await repo.get_consumption_profile(
        interval=request.interval, 
        startdate=request.startdate, 
        enddate=request.enddate, 
        biddingarea=request.biddingarea, 
        networkareaid=request.networkareaid)    
    ret = []    
    for d in dto:
        inst = ConsumptionProfileModel.from_dto(d)
        if inst.Period.date() < _enddate.date():
            ret.append(inst)
    return ret


import asyncio

if __name__ == "__main__":
    # ret = asyncio.run(get_network_areas())
    # for r in ret:
    #     print(r)

    request = UpdateConsumptionProfileRq()
    #print(request)
    ret = asyncio.run(get_consumption_profile(request))
    for r in ret:
        print(r)