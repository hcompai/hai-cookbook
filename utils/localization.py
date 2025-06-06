import json
from typing import Any, Literal

from PIL import Image
from pydantic import BaseModel

from utils.image import convert_image_to_base64_url


LOCALIZATION_TASK_PROMPT = """\
Localize an element on the GUI image according to my instructions 
and output a click position as Click(x, y) with x num pixels from 
the left edge and y num pixels from the top edge.
"""


def build_localization_task_messages(
    task: str, image: Image.Image, image_format: str
) -> list[dict[str, Any]]:
    """Build the messages for the localization task.

    Args:
        image: Image providing context for the localization task.
        instruction: User instruction for the localization task.
        format: PIL image format (see https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

    Returns:
        List of messages for the localization task.
    """
    image_url = convert_image_to_base64_url(image=image, format=image_format)
    return [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url", 
                    "image_url": {
                        "url": image_url,
                    },
                },
                {"type": "text", "text": f"{LOCALIZATION_TASK_PROMPT}\n{task}"},
            ],
        }
    ]


class ClickAction(BaseModel):
    """Click at specific coordinates on the screen."""

    action: Literal["click"] = "click"
    x: int
    """The x coordinate, number of pixels from the left edge."""
    y: int
    """The y coordinate, number of pixels from the top edge."""


def build_localization_task_messages_structured_output(
    task: str, image: Image.Image, image_format: str
) -> list[dict[str, Any]]:
    return [
        {
            "role": "system",
            "content": json.dumps([ClickAction.model_json_schema()]),
        },
        *build_localization_task_messages(
            task=task, image=image, image_format=image_format
        ),
    ]
