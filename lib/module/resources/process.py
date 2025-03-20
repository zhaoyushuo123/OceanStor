from lib.public.common.common_module_base import CommonModuleBase
from lib.public.faults.process.process_fault import CommonProcessFaultHelper
from lib.public.resources.common_process import CommonProcess


class Proces(CommonProcess):
    @property
    def name(self):
        return self.name
    @property
    def description(self):
        return self.description
    def inject_fault(self):
        self.fault_helper.inject_fault()

    @property
    def fault_helper(self):
        cls = PacificProcessFaultHelper()
        return cls

class PacificProcessFaultHelper(CommonProcessFaultHelper):
    pass