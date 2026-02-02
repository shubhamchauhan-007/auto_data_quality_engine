import logging

logging.basicConfig(
    filename="data/reports/pipeline.log",
    level=logging.INFO,
    format ="%(asctime)s - %(levelname)s -%(message)s"
)

logger = logging.getLogger()