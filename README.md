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
  `python data_preprocess.py`.
  
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


> References:  
>  
> 1. [Deep-Learning Based, Automated Segmentation of Macular Edema in Optical Coherence Tomography](https://www.biorxiv.org/content/biorxiv/early/2017/05/09/135640.full.pdf)  
> 2. [uw-biomedical-ml/irf-segmenter](https://github.com/uw-biomedical-ml/irf-segmenter)  
> 3. [wuyang0329/unet](https://github.com/wuyang0329/unet)