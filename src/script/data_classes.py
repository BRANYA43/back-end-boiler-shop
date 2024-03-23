from dataclasses import dataclass
from pathlib import Path
from typing import Union, List, Literal

Value = int | float | str
PriceValue = Value
PriceValueList = list[PriceValue]
SortedPriceValues = dict[str, PriceValue]
SpecValue = Value
SpecValueList = list[SpecValue]
SortedSpecValues = dict[str, SpecValue]


@dataclass
class UnpackedSpecificationData:
    name: str
    value: SpecValue


@dataclass
class UnpackedSpecificationsData:
    all: List[UnpackedSpecificationData]
    card: List[str]
    detail: List[str]


@dataclass
class UnpackedImageSetData:
    cover: Path
    extra: List[Path]


@dataclass
class UnpackedProductData:
    name: str
    description: str
    img_set: UnpackedImageSetData
    price: PriceValue
    specs: UnpackedSpecificationsData


@dataclass
class CompactSpecificationData:
    name: str
    value: Union[SpecValue, SortedSpecValues, SortedSpecValues]


@dataclass
class CompactSpecificationsData:
    sorting: List[str]
    all: List[CompactSpecificationData]
    card: List[str]
    detail: List[str]


@dataclass
class CompactPricesData:
    sorting: List[str]
    values: Union[PriceValue, PriceValueList, SortedPriceValues]


class CompactImageSetData:
    cover: Path
    extra: List[Path]


@dataclass
class CompactProductData:
    name: str
    description: Union[str, None]
    pattern_kws: Union[dict, None]
    img_set: CompactImageSetData
    mixin: Literal['fully', 'equally']
    prices: CompactPricesData
    specs: CompactSpecificationsData


@dataclass
class CompactCategoryData:
    name: str
    cover_img: Path


@dataclass
class CompactCatalogData:
    category: CompactCategoryData
    products: List[CompactProductData]


@dataclass
class CompactData:
    catalog: List[CompactCatalogData]
