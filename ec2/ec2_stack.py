from aws_cdk.aws_s3_assets import Asset
import os.path
dirname = os.path.dirname(__file__)

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    core
)


class Ec2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "VPC",
        nat_gateways=0,
        subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
            )

        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforSSM"))

        instance = ec2.Instance(self, "Instance",
        instance_type=ec2.InstanceType("t3.nano"),
        machine_image=amzn_linux,
        vpc = vpc,
        role = role
        )

        asset = Asset(self, "Asset", path=os.path.join(dirname, "configure.sh"))
        local_path = instance.user_data.add_s3_download_command(
            bucket=asset.bucket,
            bucket_key=asset.s3_object_key
        )
        instance.user_data.add_execute_file_command(
            file_path=local_path,
            arguments="--verbose -y"
        )
        asset.grant_read(instance.role)
