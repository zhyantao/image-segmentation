## Usage

1. Put [original data](https://pan.baidu.com/s/1vRBgHBudaplr4RNyVieaJw) in *data/original/images*, and then copy the file to *data/original/labels*. PWD: **2ba5**

2. Seperate your original images and labels to *train/train_labels*, *val/val_labels* and *test* directories.

3. Deploy the environment

   ```shell
   pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
   ```

4. Data preprocess, run ` ./data_preprocess.py`

5. Training the data, run `./train.py`

6. Testing the result, run `./test.py`

7. Visualize the result, run `./label_visualization.py`