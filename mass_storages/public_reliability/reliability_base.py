from lib.module.faults.process.process_fault import ProcessFault


class ReliabilityBase(object):
    """
    可靠性公共基类
    """
    def pretest(self):
        pass

    def produce(self):
        self.process_fault = ProcessFault()
        self.process_fault.inject()

    def posttest(self):
        pass