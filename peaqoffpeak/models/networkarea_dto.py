from dataclasses import dataclass

@dataclass
class NetworkAreaDTO:
    NetworkArea: str
    NetworkAreaId: str
    NetworkAreaTypeName:str
    ConstraintAreaId:int
    ConstraintAreaName:str
    CompanyName:str
    EdielId:str
    IsActive:bool
    ValidFrom:str
    ValidTo:str
    BalanceProviders:str
    FutureBalanceProviders:str

    @classmethod
    def from_dict(cls, data):
        return cls(
            NetworkArea = data.get('NetworkArea'),
            NetworkAreaId = data.get('NetworkAreaId'),
            NetworkAreaTypeName = data.get('NetworkAreaTypeName'),
            ConstraintAreaId = data.get('ConstraintAreaId'),
            ConstraintAreaName = data.get('ConstraintAreaName'),
            CompanyName = data.get('CompanyName'),
            EdielId = data.get('EdielId'),
            IsActive = data.get('IsActive'),
            ValidFrom = data.get('ValidFrom'),
            ValidTo = data.get('ValidTo'),
            BalanceProviders = data.get('BalanceProviders'),
            FutureBalanceProviders = data.get('FutureBalanceProviders')
        )
    

@dataclass
class NetWorkAreaModel:
    displayname:str #show in dropdown
    networkareaid:str #use as networkareaid in call
    biddingarea:int #constraintareaid    
    isvalid: bool #isactive true and validto is null or future

    @classmethod
    def from_dto(cls, dto:NetworkAreaDTO):
        return cls(
            displayname = dto.NetworkArea,
            networkareaid = dto.NetworkAreaId,
            biddingarea = dto.ConstraintAreaId,
            isvalid = dto.IsActive and (dto.ValidTo.lower == "null" or datetime.strptime(dto.ValidTo, "%Y-%m-%dT%H:%M:%S") > datetime.now())
        )
    

"""
"NetworkArea": "Ajaure-Grundfors",
    "NetworkAreaId": "AJG",
    "NetworkAreaTypeName": "Stamnät",
    "ConstraintAreaId": 2,
    "ConstraintAreaName": "Elområde 2",
    "CompanyName": "Svenska kraftnät",
    "EdielId": "10000",
    "IsActive": true,
    "ValidFrom": "1996-01-01T00:00:00",
    "ValidTo": null,
    "BalanceProviders": null,
    "FutureBalanceProviders": null
"""