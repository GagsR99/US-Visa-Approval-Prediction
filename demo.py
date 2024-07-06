# # from us_visa.logger import logging
# # from us_visa.exception import USvisaException
# # import sys
# #
# # try:
# #     a = 1 / "10"
# # except Exception as e:
# #     logging.info(e)
# #     raise USvisaException(e, sys) from e
# #
# # # logging.info("Welcome to our custom log")

# from us_visa.constants import *

# print(COLLECTION_NAME)

from us_visa.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()