from _typeshed import Incomplete
from s3transfer.tasks import CompleteMultipartUploadTask as CompleteMultipartUploadTask, CreateMultipartUploadTask as CreateMultipartUploadTask, SubmissionTask as SubmissionTask, Task as Task
from s3transfer.utils import ChunksizeAdjuster as ChunksizeAdjuster, calculate_range_parameter as calculate_range_parameter, get_callbacks as get_callbacks, get_filtered_dict as get_filtered_dict

class CopySubmissionTask(SubmissionTask):
    EXTRA_ARGS_TO_HEAD_ARGS_MAPPING: Incomplete
    UPLOAD_PART_COPY_ARGS: Incomplete
    CREATE_MULTIPART_ARGS_BLACKLIST: Incomplete
    COMPLETE_MULTIPART_ARGS: Incomplete

class CopyObjectTask(Task): ...
class CopyPartTask(Task): ...
