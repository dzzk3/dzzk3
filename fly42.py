#from MyQR import myqr  # 注意区分大小写
#myqr.run(words='Do not go gentle into that good night!')  # 生成二维码

#from MyQR import myqr
#myqr.run(
    #words='https://u.wechat.com/MJ2iAjftPR4PIveiL9vEueA', # 包含信息
    #picture='wolf.jpg',   # 背景图片
    #colorized=True,   # 是否有颜色，如果为False则为黑白
    #save_name='code2.png' # 输出文件名
#)

from MyQR import myqr
myqr.run(
    words='https://u.wechat.com/MJ2iAjftPR4PIveiL9vEueA', # 包含信息
    picture='hourse.gif',   # 背景图片
    colorized=True,   # 是否有颜色，如果为False则为黑白
    save_name='horse.gif' # 输出文件名
)