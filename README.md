## Usage

1. Make new directories, run `sh mkdir.sh`

2. Put [original data](https://pan.baidu.com/s/1vRBgHBudaplr4RNyVieaJw) in *data/original/images*, and then copy the file to *data/original/labels*. PWD: **2ba5**

3. Seperate your original images and labels to *train/train_labels*, *val/val_labels* and *test* directories.

4. Deploy the environment.

   ```shell
   pip3 install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
   ```

5. Data preprocess, run `python3 data_preprocess.py`.

6. Training the data, run `python3 train.py`.

7. Testing the result, run `python3 test.py`.

8. Visualize the result, run `python3 label_visualization.py`.