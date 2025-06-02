# H Company cookbook

The H Company cookbook provides code examples and guides to help developers using tools developed by [**H Company**](https://www.hcompany.ai/).

## Holo-1

Holo-1 is an Action Vision-Language Model (VLM) developed by [**H Company**](https://www.hcompany.ai/) for use in the Surfer-H web agent system. It is designed to interact with web interfaces like a human user.

As part of a broader agentic architecture, Holo-1 acts as a policy, localizer, or validator, helping the agent understand and act in digital environments.

Trained on a mix of open-access, synthetic, and self-generated data, Holo-1 enables state-of-the-art (SOTA) performance on the WebVoyager benchmark, offering the best accuracy/cost tradeoff among current models. It also excels in UI localization tasks such as Screenspot, Screenspot-V2, Screenspot-Pro, GroundUI-Web, and our own newly introduced benchmark WebClick.

Holo-1 is optimized for both accuracy and cost-efficiency, making it a strong open-source alternative to existing VLMs.

- [Holo-1 3B](https://huggingface.co/Hcompany/Holo1-3B) - [Qwen RESEARCH LICENSE](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/blob/main/LICENSE)
- [Holo-1 7B](https://huggingface.co/Hcompany/Holo1-7B) - Apache 2.0

### Examples:

- [How to deploy Holo-1 (3B or 7B) on Amazon Sagemaker](https://github.com/hcompai/hai-cookbook/blob/main/holo1/sagemaker/deploy.ipynb)
- [Using AWS SageMaker to Invoke Holo-1 for a localisation task](https://github.com/hcompai/hai-cookbook/blob/main/holo1/sagemaker/invoke_localisation.ipynb)


## License

This library is licensed under the Apache 2.0 License. For more details, please take a look at the LICENSE file.

