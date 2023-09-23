import qrcode
# 构建二维码
data = 'hello world!'
img = qrcode.make(data)
# 显示图片格式，为qrcode.image.pil.PilImage
print(type(img))
# 保存图片 
img.save("test2.png")
