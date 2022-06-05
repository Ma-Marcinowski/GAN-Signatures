# GAN-Signatures

### 0. Introduction

* #### 0.1. Objective of the author's repository was to introduce GAN based methods for forgery of static handwritten signatures. The purpose of these methods was to evaluate and develop forensic methods for detection and attribution of deepfake signatures.

* #### 0.2. Keywords:

    * Computational, statistical, probabilistic; 
    * Forensics, criminalistics, analysis, examination;
    * Handwriting, signatures, documents, forgery;
    * Neural, networks, deep, machine, learning, artificial, intelligence, generative, adversarial, GAN, ANN, AI;

* #### 0.3. Data:

    * CEDAR signatures: 24 original and 24 forged signatures by 55 anonymous writers.
    * Dey, Sounak, Anjan Dutta, J. Ignacio Toledo, Suman K. Ghosh, Josep Llados, and Umapada Pal. ‘SigNet: Convolutional Siamese Network for Writer Independent Offline Signature Verification’. ArXiv:1707.02131 [Cs], 30 September 2017. http://arxiv.org/abs/1707.02131.
    * Available at http://www.cedar.buffalo.edu/NIJ/data/signatures.rar

 * #### 0.4. Preprocessing:

    * Images are converted to grayscale, colour inverted, then padded to achieve equal height and width, lastly resized to 512 by 512 px and saved in a png format.

### 1. Model v1.0

* #### 1.1. Architecture:
     
     * Based on: Isola, Phillip, Jun-Yan Zhu, Tinghui Zhou, and Alexei A. Efros. ‘Image-to-Image Translation with Conditional Adversarial Networks’. ArXiv:1611.07004 [Cs], 26 November 2018. http://arxiv.org/abs/1611.07004.

     * Where SPADE was utilized and of Batch Normalization, based on: Park, Taesung, Ming-Yu Liu, Ting-Chun Wang, and Jun-Yan Zhu. ‘Semantic Image Synthesis with Spatially-Adaptive Normalization’. arXiv, 5 November 2019. https://doi.org/10.48550/arXiv.1903.07291.

* #### 1.2. Initial results:
     
     ![example](https://github.com/Ma-Marcinowski/GAN-Signatures/blob/main/Examples/Example.png "Example")
     
