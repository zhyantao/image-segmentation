## Usage

1. Download [original data](https://pan.baidu.com/s/1vRBgHBudaplr4RNyVieaJw) to this directory. PWD: **2ba5**

2. Make original dataset, run `sh make_dataset.sh`

3. Deploy the environment.

   ```shell
   pip3 install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
   ```

4. Data preprocess, run `python3 data_preprocess.py`.

5. DIY your dataset, run `sh DIY_dataset.sh`

6. Training the data, run `python3 train.py`.

7. Testing the result, run `python3 test.py`.

8. Visualize the result, run `python3 label_visualization.py`.