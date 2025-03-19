from lib.public.common.common_module_base import CommonProductBase


class MedModuleBase(CommonProductBase):
    @property
    def cluster(self):
        return 'med_cluster'

    @property
    def region_id(self):
        return 0
