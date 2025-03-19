from lib.module.common.feature_base import PacificFeatureModuleBase


def main():
    print("its first main")

if __name__ == "__main__":
    main()
    pacific_feature_obj = PacificFeatureModuleBase()
    print(pacific_feature_obj.cluster)