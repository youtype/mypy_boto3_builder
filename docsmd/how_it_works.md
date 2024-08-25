# How it works

Fully automated [mypy-boto3-builder](https://github.com/youtype/mypy_boto3_builder) carefully generates
type annotations for each service, patiently waiting for `boto3` updates. It delivers
drop-in type annotations for you and makes sure that:

- All available `botocore` services are covered.
- Each public class and method of every `botocore` service gets valid type annotations
  extracted from `botocore` schemas.
- Type annotations include up-to-date documentation.
- Link to documentation is provided for every method.
- Code is processed by [ruff](https://docs.astral.sh/ruff/) for readability.
