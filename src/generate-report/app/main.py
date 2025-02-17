from typing import Any

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(service=__name__)

@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: Any, context: LambdaContext) -> None:
    pass
