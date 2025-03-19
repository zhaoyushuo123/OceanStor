from lib.public.common.common_module_base import Module


class CommonProductBase(Module):
    def __init__(self, *args, **kwargs):
        pass

    @property
    def cluster(self):
        raise NotImplementedError

    @property
    def region_id(self):
        raise NotImplementedError

    @property
    def product_type(self):
        raise NotImplementedError
