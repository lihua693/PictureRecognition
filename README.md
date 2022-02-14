# Get_photo_ret.py

## Usage



```shell
python3 main.py
```

本地服务器路径：127.0.0.1:8888/api/v1/vin-rec

传入图片本地路径，以及available.text中的uid，即可识别图片信息。使用post方法。

available.text文件中的uid需要以空格隔开。

### example

```
key=path value=demo.png
key=key  value=a038a418-1e86-4197-859d-24aed35765d1
```

```
# return value:
"LSVG449J472059134"
```

### 相关依赖

```
# 安装python的Web框架 tornado
pip install tornado
# 安装OCR工具 paddleocr
pip install paddleocr
# 如运行不成功执行
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```

### uuid.text格式

```
以 ”,“ 为分隔符，需要手动设置uuid，未实现post设置方法。
```



