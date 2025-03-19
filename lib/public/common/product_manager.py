class ProductManager:
    def __init__(self):
        self.product_type = 'pacific'
    def get_product_instance(self, *args, **kwargs):
        if 'pacific' in self.product_type:
            from lib.module.common.module_base import PacificModuleBase
            return PacificModuleBase(*args, **kwargs)
        elif 'med' in self.product_type:
            from lib.med.common.module_base import MedModuleBase
            return MedModuleBase(*args, **kwargs)
