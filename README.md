# H.AI cookbook

The H.AI cookbook provides code examples and guides to help developers use models developed by [**H Company**](https://www.hcompany.ai/).

## Holo1

Holo1 is an Action Vision-Language Model (VLM) developed by [**H Company**](https://www.hcompany.ai/) for use in the Surfer-H web agent system. It is designed to interact with web interfaces like a human user.

As part of a broader agentic architecture, Holo1 acts as a policy, localizer, or validator, helping the agent understand and act in digital environments.

Trained on a mix of open-access, synthetic, and self-generated data, Holo1 enables state-of-the-art (SOTA) performance on the WebVoyager benchmark, offering the best accuracy/cost tradeoff among current models. It also excels in UI localization tasks such as Screenspot, Screenspot-V2, Screenspot-Pro, GroundUI-Web, and our own newly introduced benchmark, WebClick.

Holo1 is optimized for both accuracy and cost-efficiency, making it a strong open-source alternative to existing VLMs.

- [Holo1 3B](https://huggingface.co/Hcompany/Holo1-3B) - [Qwen RESEARCH LICENSE](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/blob/main/LICENSE)
- [Holo1 7B](https://huggingface.co/Hcompany/Holo1-7B) - Apache 2.0

### vLLM guides:

- [How to deploy Holo1 (3B or 7B) locally with vLLM on Nvidia](https://github.com/hcompai/hai-cookbook/blob/main/holo1/vllm/README.md)
- [Using OpenAI Client to invoke Holo1 for a navigation task](https://github.com/hcompai/hai-cookbook/blob/main/holo1/vllm/invoke_navigation.ipynb)
- [Using OpenAI Client to invoke Holo1 for a localization task](https://github.com/hcompai/hai-cookbook/blob/main/holo1/vllm/invoke_localization.ipynb)

### AWS SageMaker guides:

- [How to deploy Holo1 (3B or 7B) on Amazon SageMaker](https://github.com/hcompai/hai-cookbook/blob/main/holo1/sagemaker/deploy.ipynb)
- [Using AWS SageMaker to Invoke Holo1 for a navigation task](https://github.com/hcompai/hai-cookbook/blob/main/holo1/sagemaker/invoke_navigation.ipynb)
- [Using AWS SageMaker to Invoke Holo1 for a localization task](https://github.com/hcompai/hai-cookbook/blob/main/holo1/sagemaker/invoke_localization.ipynb)


## Citation

**BibTeX:**

```
@misc{andreux2025surferhmeetsholo1costefficient,
      title={Surfer-H Meets Holo1: Cost-Efficient Web Agent Powered by Open Weights}, 
      author={Mathieu Andreux and Breno Baldas Skuk and Hamza Benchekroun and Emilien Biré and Antoine Bonnet and Riaz Bordie and Matthias Brunel and Pierre-Louis Cedoz and Antoine Chassang and Mickaël Chen and Alexandra D. Constantinou and Antoine d'Andigné and Hubert de La Jonquière and Aurélien Delfosse and Ludovic Denoyer and Alexis Deprez and Augustin Derupti and Michael Eickenberg and Mathïs Federico and Charles Kantor and Xavier Koegler and Yann Labbé and Matthew C. H. Lee and Erwan Le Jumeau de Kergaradec and Amir Mahla and Avshalom Manevich and Adrien Maret and Charles Masson and Rafaël Maurin and Arturo Mena and Philippe Modard and Axel Moyal and Axel Nguyen Kerbel and Julien Revelle and Mats L. Richter and María Santos and Laurent Sifre and Maxime Theillard and Marc Thibault and Louis Thiry and Léo Tronchon and Nicolas Usunier and Tony Wu},
      year={2025},
      eprint={2506.02865},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2506.02865}, 
}
```


## License

This library is licensed under the Apache 2.0 License. For more details, please take a look at the LICENSE file.
