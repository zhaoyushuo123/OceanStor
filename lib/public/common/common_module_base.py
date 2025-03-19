from lib.public.common.product_manager import ProductManager


class Module(object):
    pass


class CommonModuleBase(Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = []
        self.args = args
        self.kwargs = {}
        self.kwargs = kwargs
        self.product_manager = ProductManager()

    @property
    def product_instance(self):
        if not hasattr(self, '_product_instance'):
            self._product_instance = self.product_manager.get_product_instance(*self.args, **self.kwargs)
        return self._product_instance

    @property
    def product_type(self):
        raise NotImplementedError

    @property
    def cluster(self):
        return self.product_instance.cluster

    @property
    def region_id(self):
        return self.product_instance.cluster
