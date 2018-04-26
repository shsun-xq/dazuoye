这是一个具有比赛性质的课程大作业


数据含有5张6000x6000的RGB图像以及相应的label，未划分训练集、测试集，自行划分
数据下载地址：https://pan.baidu.com/s/1HV56CET2V5e8J7BMrA7YYA 密码：9ap5


以下是针对使用pytorch的一个数据处理的参考：
1、cutPic.py 这个脚本是用来把图切小的，自己修改成员变量aimSize就行。
2、toMask.py 该脚本是用来把上面切好的labels转成numpy，这样后续处理上会方便些。
3、dataset.py 通过以上两步就到了inputs（Image）和target（numpy），接下来得把数据写成一个类然后封装成一个对象，使用getItem时成对的返回一个input和一个target，具体可查文档，此脚本是一个比较简陋的样例。

以上步骤是为了在训练时成对得到一个输入图片以及一个可以直接用于2D交叉熵loss函数的矩阵（WxH，每个像素对应类别），需要注意的是（1）input和target得成对匹配;（2）返回值得是两个tensor对象，可用torchvision中的ToTensor，或就像2中，转numpy时直接用.npy生成tensor也行。

