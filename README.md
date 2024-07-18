# Neural-Style-Transfer-with-Image-Captioning

##

## Overview

This project integrates two powerful techniques in the field of computer vision and deep learning: Neural Style Transfer and Image Captioning. The goal is to apply artistic styles to images while generating descriptive captions that detail the content of the stylized images.

### Neural Style Transfer
Neural Style Transfer is a technique that manipulates images to adopt the style of a given reference image while maintaining the content of the original image. This project uses a pre-trained model from TensorFlow Hub to achieve this transformation.

### Image Captioning
Image Captioning involves generating textual descriptions for images. This project uses a pre-trained image captioning model from the `transformers` library, which combines a Vision Transformer (ViT) for image feature extraction and a GPT-2 model for sequence generation.

## Features

- Apply artistic styles to images using Neural Style Transfer.
- Generate descriptive captions for stylized images.
- Use pre-trained models for both style transfer and image captioning to streamline the process.
- Easy-to-use interface for applying styles and generating captions.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip

### Required Libraries

Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── README.md
├── requirements.txt
├── NeuralStyleTransfer.ipyb
└── ImageCaptioning.ipyb
```

- `README.md`: This file.
- `requirements.txt`: List of required Python libraries.
- `NeuralStyleTransfer.ipyb`: Script for performing neural style transfer.
- `ImageCaptioning.ipyb`: Script for generating image captions.

## Pre-trained Models

The project uses pre-trained models from TensorFlow Hub and the `transformers` library. No additional model files are needed unless specified.

## Acknowledgments

- [Neural Style Transfer by Leon A. Gatys, Alexander S. Ecker, and Matthias Bethge](https://arxiv.org/abs/1508.06576)
- [Show and Tell: A Neural Image Caption Generator by Oriol Vinyals, Alexander Toshev, Samy Bengio, and Dumitru Erhan](https://arxiv.org/abs/1411.4555)
- [TensorFlow Hub](https://tfhub.dev/)
- [Hugging Face Transformers](https://github.com/huggingface/transformers)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/neural-style-transfer-captioning/issues) if you want to contribute.

---

