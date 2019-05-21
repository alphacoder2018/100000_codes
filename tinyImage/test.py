import tinify
tinify.key = "你的KEY" 

image_path = '本地文件路径'
output_path = '压缩后的图片路径'
image_url = '在线图片链接'

source = tinify.from_file(image_path)
source.to_file(output_path)
print("转换完成")


source = tinify.from_url(image_url)
source.to_file(output_path)
print(image_url +"转换完成")