from typing import Dict, List

from s3transfer.tasks import CompleteMultipartUploadTask as CompleteMultipartUploadTask
from s3transfer.tasks import CreateMultipartUploadTask as CreateMultipartUploadTask
from s3transfer.tasks import SubmissionTask as SubmissionTask
from s3transfer.tasks import Task as Task
from s3transfer.utils import ChunksizeAdjuster as ChunksizeAdjuster
from s3transfer.utils import calculate_range_parameter as calculate_range_parameter
from s3transfer.utils import get_callbacks as get_callbacks
from s3transfer.utils import get_filtered_dict as get_filtered_dict

class CopySubmissionTask(SubmissionTask):
    EXTRA_ARGS_TO_HEAD_ARGS_MAPPING: Dict[str, str]
    UPLOAD_PART_COPY_ARGS: List[str]
    CREATE_MULTIPART_ARGS_BLACKLIST: List[str]
    COMPLETE_MULTIPART_ARGS: List[str]

class CopyObjectTask(Task): ...
class CopyPartTask(Task): ...
