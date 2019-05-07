# OCT Image Segmentation

## Dependencies

- CentOS 7

- Python 3.6.5

- Deploy the environment.

```shell
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

## Usage

### Data Preprocess

- Download [original data](https://pan.baidu.com/s/1vRBgHBudaplr4RNyVieaJw) to `seg-retinal/`. PWD: **2ba5**

- Make original dataset, run command:

  `sh make_dataset.sh`
  
- Data preprocess, run command:

  `python data_preprocess.py`
  
- DIY your dataset, open `DIY_dataset.sh` and modify the number of images you wanna to train and valid, then run command:

  `sh DIY_dataset.sh`

### Training model

```shell
python train.py
```

### Test model

```shell
python test.py
```

### Visualize the result

```shell
python label_visualization.py
```

## References:

1. [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/) 
#. [Deep-Learning Based, Automated Segmentation of Macular Edema in Optical Coherence Tomography](https://www.biorxiv.org/content/biorxiv/early/2017/05/09/135640.full.pdf)
#. [SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation](https://arxiv.org/pdf/1511.00561v2.pdf)
#. [Relationship Between a Systemic Inflammatory Marker, Plaque Inflammation, and Plaque Characteristics Determined by Intravascular Optical Coherence Tomography](https://www.ahajournals.org/doi/pdf/10.1161/ATVBAHA.107.145987)
#. [preddy5/segnet](https://github.com/preddy5/segnet)