from lib.public.common.common_feature_base import CommonFeatureModuleBase


class PacificFeatureModuleBase(CommonFeatureModuleBase):

    @property
    def cluster(self):
        return self.product_instance.cluster

    @property
    def region_id(self):
        return self.product_instance.cluster
