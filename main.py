from lib.module.common.feature_base import PacificFeatureModuleBase
from mass_storages.public_reliability.reliability_base import ReliabilityBase


def main():
    print("its first main")

if __name__ == "__main__":
    main()
    pacific_feature_obj = PacificFeatureModuleBase()
    print(pacific_feature_obj.cluster)

    case = ReliabilityBase()
    case.pretest()
    case.produce()
    case.posttest()