from lib.public.common.common_product_base import CommonProductBase


class PacificModuleBase(CommonProductBase):
    @property
    def cluster(self):
        return 'pacific_cluster'

    @property
    def region_id(self):
        return 0


