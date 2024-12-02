import sys
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.main import get_selected_service_names, main
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.botocore_changelog import BotocoreChangelog


class TestMain:
    def test_get_selected_service_names(self) -> None:
        assert [
            i.name
            for i in get_selected_service_names(
                ["s3", "ec2"],
                [ServiceName("ec2", "EC2"), ServiceName("other", "Other")],
            )
        ] == ["ec2"]
        assert [
            i.name
            for i in get_selected_service_names(
                ["all", "ec2"],
                [ServiceName("ec2", "EC2"), ServiceName("other", "Other")],
            )
        ] == ["ec2", "other"]
        assert get_selected_service_names(["s3", "ec2"], []) == []
        with patch.object(BotocoreChangelog, "fetch_updated") as fetch_updated_mock:
            fetch_updated_mock.return_value = ["ecs"]
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

    @patch("mypy_boto3_builder.main.get_available_service_names")
    @patch("mypy_boto3_builder.main.Boto3Generator")
    @patch.object(sys, "argv", ["-o", "/tmp", "-b", "1.2.3.post4"])  # noqa: S108
    def test_main(
        self,
        Boto3GeneratorMock: MagicMock,
        get_available_service_names_mock: MagicMock,
    ) -> None:
        main()
        Boto3GeneratorMock().generate_product.assert_called()
