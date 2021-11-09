import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.cli_parser import Namespace
from mypy_boto3_builder.main import (
    generate_docs,
    generate_stubs,
    get_available_service_names,
    get_selected_service_names,
    main,
)
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.boto3_changelog import Boto3Changelog


class TestMain:
    def test_get_selected_service_names(self) -> None:
        assert [
            i.name
            for i in get_selected_service_names(
                ["s3", "ec2"], [ServiceName("ec2", "EC2"), ServiceName("other", "Other")]
            )
        ] == ["ec2"]
        assert [
            i.name
            for i in get_selected_service_names(
                ["all", "ec2"], [ServiceName("ec2", "EC2"), ServiceName("other", "Other")]
            )
        ] == ["ec2", "other"]
        assert get_selected_service_names(["s3", "ec2"], []) == []
        with patch.object(Boto3Changelog, "get_updated_service_names", lambda x, y: ["ecs"]):
            assert [
                i.name
                for i in get_selected_service_names(
                    ["updated", "ec2"],
                    [
                        ServiceName("ec2", "EC2"),
                        ServiceName("ecs", "ECS"),
                        ServiceName("other", "Other"),
                    ],
                )
            ] == ["ec2", "ecs"]

    def test_get_available_service_names(self) -> None:
        session_mock = MagicMock()
        session_mock.get_available_services.return_value = ["s3", "ec2", "unsupported"]
        session_mock._session.get_service_data.return_value = {
            "metadata": {"serviceAbbreviation": "Amazon S3", "serviceId": "s3"}
        }
        assert len(get_available_service_names(session_mock)) == 3

    @patch("mypy_boto3_builder.main.generate_stubs")
    @patch("mypy_boto3_builder.main.generate_docs")
    @patch.object(sys, "argv", ["-o", "/tmp", "-b", "1.2.3.post4"])
    def test_main(self, generate_docs_mock: MagicMock, generate_stubs_mock: MagicMock) -> None:
        main()
        generate_stubs_mock.assert_called()

    @patch("mypy_boto3_builder.main.process_service_docs")
    @patch("mypy_boto3_builder.main.process_boto3_stubs_docs")
    def test_generate_docs(
        self, process_boto3_stubs_docs_mock: MagicMock, process_service_docs_mock: MagicMock
    ) -> None:
        with tempfile.TemporaryDirectory() as output_dir:
            namespace = Namespace(
                log_level=0,
                output_path=Path(output_dir),
                service_names=["s3"],
                build_version="1.2.3.post4",
                installed=False,
                skip_master=False,
                skip_services=False,
                builder_version="1.2.3",
                generate_docs=False,
                list_services=False,
                partial_overload=False,
                skip_published=False,
            )
            session_mock = MagicMock()
            generate_docs(
                namespace,
                service_names=[ServiceName("s3", "S3")],
                available_service_names=[ServiceName("s3", "S3")],
                session=session_mock,
            )
            process_boto3_stubs_docs_mock.assert_called()
            process_service_docs_mock.assert_called()

    @patch("mypy_boto3_builder.main.PyPIManager")
    @patch("mypy_boto3_builder.main.process_service")
    @patch("mypy_boto3_builder.main.process_master")
    @patch("mypy_boto3_builder.main.process_boto3_stubs")
    @patch("mypy_boto3_builder.main.process_botocore_stubs")
    def test_generate_stubs(
        self,
        process_botocore_stubs_mock: MagicMock,
        process_boto3_stubs_mock: MagicMock,
        process_master_mock: MagicMock,
        process_service_mock: MagicMock,
        PyPIManagerMock: MagicMock,
    ) -> None:
        with tempfile.TemporaryDirectory() as output_dir:
            namespace = Namespace(
                log_level=0,
                output_path=Path(output_dir),
                service_names=["s3"],
                build_version="1.2.3.post4",
                installed=False,
                skip_master=False,
                skip_services=False,
                builder_version="1.2.3",
                generate_docs=False,
                list_services=False,
                partial_overload=False,
                skip_published=False,
            )
            session_mock = MagicMock()
            generate_stubs(
                namespace,
                service_names=[ServiceName("s3", "S3")],
                available_service_names=[ServiceName("s3", "S3")],
                session=session_mock,
            )
            process_botocore_stubs_mock.assert_called()
            process_boto3_stubs_mock.assert_called()
            process_master_mock.assert_called()
            process_service_mock.assert_called()
