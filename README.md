# OCT Image Segmentation

## Dependencies

- CentOS 7
- Python 3.6.5
- [Python-tkinter](https://centos.pkgs.org/7/centos-sclo-rh-x86_64/rh-python36-python-tkinter-3.6.3-3.el7.x86_64.rpm.html)
- Deploy the environment.
    ```shell
    pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
    ```

## Usage

### Data Preprocess

- Download source codes, run command:

  `git clone https://github.com/toooney/image-segmentation.git`

- Download [original data](https://pan.baidu.com/s/1WRdH2HjVpIi6cjRVHrhO8Q) to `image-segmentation/`. PWD: **msla**

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

## References

1. [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/) 
2. [Deep-Learning Based, Automated Segmentation of Macular Edema in Optical Coherence Tomography](https://www.biorxiv.org/content/biorxiv/early/2017/05/09/135640.full.pdf)
3. [SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation](https://arxiv.org/pdf/1511.00561v2.pdf)
4. [Relationship Between a Systemic Inflammatory Marker, Plaque Inflammation, and Plaque Characteristics Determined by Intravascular Optical Coherence Tomography](https://www.ahajournals.org/doi/pdf/10.1161/ATVBAHA.107.145987)
5. [preddy5/segnet](https://github.com/preddy5/segnet)