from lib.module.resources.process import Proces
from lib.public.faults.process.process_fault import CommonProcessFault


class ProcessFault(CommonProcessFault):
    def inject(self):
        super(ProcessFault, self).inject()

    @property
    def fault_object(self):
        return Proces()