from lib.public.common.common_dfx_base import CommonFaultBase
from lib.public.common.common_module_base import CommonModuleBase


class CommonProcessFault(CommonFaultBase):
    def inject(self):
        self.fault_object.inject_fault()

    @property
    def fault_object(self):
        raise NotImplementedError
    @property
    def fault_helper(self):
        raise NotImplementedError

class CommonProcessFaultHelper(CommonModuleBase):
    def inject_fault(self):
        print('inject_fault')