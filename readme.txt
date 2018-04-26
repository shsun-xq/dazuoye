这是一个具有比赛性质的课程大作业

1、cutPic.py 这个脚本是用来把图切小的，自己修改成员变量aimSize

2、toMask.py 该脚本可以读取用第一个脚本转化后的.tif文件，然后形成numpy
但这里有个特别的注意事项，就是numpy里头的图片是HxWxC(长x宽x通道)的，而torch里头的tensor却是CxHxW的，这样对应不上。所以得在写data_loader时，把用toTensor整成tensor后的值，进行一个维度的转化 output = output.transpose((2, 0, 1))，这样就好

3、dataset.py 一个简陋的dataLoader
