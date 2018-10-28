"""
Dockerfile parser and generator.

This module contains the parsing logic for Dockerfile files commands.
"""
from dataclasses import dataclass, field


@dataclass
class From:
    """
    Dataclass for the FROM command in Dockerfile.

    :param base_image: the image to base the Docker image on
    :param tag: the tag of the base image
    :param digest: the digest of the base image
    :param stage: the stage for a multi-stage build
    """

    base_image: str
    tag: str = field(default="")
    digest: str = field(default="")
    stage: str = field(default="")

    def __post_init__(self):
        """Check that only one of tag or digest is set."""
        if self.tag != "" and self.digest != "":
            print("Only one of tag or digest can be used.")
            raise RuntimeError("Only one of tag or digest can be used")

    def __str__(self):
        """Format the command."""
        return f"FROM {self.base_image}{f':{self.tag}' if self.tag != '' else ''}{f'@{self.digest}' if self.digest != '' else ''}{f' AS {self.stage}' if self.stage != '' else ''}"
