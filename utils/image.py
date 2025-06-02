"""Image utilities."""

import base64
import math
from io import BytesIO
from mimetypes import types_map

from PIL import Image, ImageDraw


def smart_resize(
    height: int,
    width: int,
    factor: int = 28,
    min_pixels: int = 56 * 56,
    max_pixels: int = 14 * 14 * 4 * 1280,
) -> tuple[int, int]:
    """Copied from https://github.com/huggingface/transformers/blob/v4.52.4/src/transformers/models/qwen2_vl/image_processing_qwen2_vl.py#L55.

    Rescales the image so that the following conditions are met:
      - Both dimensions (height and width) are divisible by 'factor'.
      - The total number of pixels is within the range ['min_pixels', 'max_pixels'].
      - The aspect ratio of the image is maintained as closely as possible.
    """
    if height < factor or width < factor:
        raise ValueError(
            f"height:{height} or width:{width} must be larger than factor:{factor}"
        )
    elif max(height, width) / min(height, width) > 200:
        raise ValueError(
            f"absolute aspect ratio must be smaller than 200, got {max(height, width) / min(height, width)}"
        )
    h_bar = round(height / factor) * factor
    w_bar = round(width / factor) * factor
    if h_bar * w_bar > max_pixels:
        beta = math.sqrt((height * width) / max_pixels)
        h_bar = math.floor(height / beta / factor) * factor
        w_bar = math.floor(width / beta / factor) * factor
    elif h_bar * w_bar < min_pixels:
        beta = math.sqrt(min_pixels / (height * width))
        h_bar = math.ceil(height * beta / factor) * factor
        w_bar = math.ceil(width * beta / factor) * factor
    return h_bar, w_bar


def draw_image_with_click(image: Image.Image, x: int, y: int):
    """Draw a click on an image with absolute coordinates.

    Args:
        image: PIL image.
        x: X absolute coordinate of the click.
        y: Y absolute coordinate of the click.

    Returns:
        PIL image with the click drawn on it.
    """
    draw = ImageDraw.Draw(image)
    draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill="red", outline="red")
    return image


def convert_image_to_base64_url(image: Image.Image, format: str = "JPEG") -> str:
    """Convert an image to a base64 URL.

    Args:
        image: PIL image.
        format: PIL image format (see https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

    Returns:
        Base64 URL.
    """
    mime_type = _get_mime_type_from_format(format=format)
    data = _encode_image_to_base64_string(image=image, format=format)
    return f"data:{mime_type};base64,{data}"


def _get_mime_type_from_format(format: str) -> str:
    """Get the MIME type associated to the PIL image format.

    Args:
        format: PIL image format (see https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).

    Returns:
        MIME type associated to the PIL image format.
    """
    for extension, mime_type in types_map.items():
        pil_format = Image.registered_extensions().get(extension)
        if format == pil_format:
            return mime_type
    raise ValueError(f"Format {format} not supported")


def _encode_image_to_base64_string(
    image: Image.Image,
    format: str,
    jpeg_quality: int = 90,
) -> str:
    """Encodes an image to a base64 string.

    Args:
        image: PIL image.
        format: PIL image format (see https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).
        jpeg_quality: JPEG compression quality.

    Returns:
        Base64 encoded string.
    """
    buffer = BytesIO()
    if format == "JPEG":
        image.convert("RGB").save(buffer, format=format, quality=jpeg_quality)
    else:
        image.save(buffer, format=format)
    base64_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return base64_str
