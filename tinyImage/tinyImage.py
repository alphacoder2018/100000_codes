import tinify
import os
from os import path
import zipfile

tinify.key = 'your key'
root_dir = path.abspath(os.getcwd())
input_dir = root_dir + '\\images'
output_dir = root_dir + '\\tinyimages'
images_list = os.listdir(input_dir)

image_url = 'https://www.sciencemag.org/sites/default/files/styles/article_main_large/public/images/sn-pandasH.jpg'


def local_images():
  for filename in images_list:
    try:
      input_path = str(input_dir+'\\'+filename)
      output_path = str(output_dir+'\\'+filename)
      source = tinify.from_file(input_path)
      source.to_file(output_path)
      print(filename +"转换完成")
    except tinify.Error:
      print(filename +"转换异常")
      pass

def url_image(url):
  output_path = str(output_dir+'\\'+'tiny.png')
  try:
    source = tinify.from_url(url)
    source.to_file(output_path)
    print(url +"转换完成")
  except tinify.Error:
    print(url +"转换异常")
    pass

def deleteImage(dir):
  file_list = os.listdir(input_dir)
  for filename in file_list:
    try:
      my_file = str(input_dir+'\\'+filename)
      os.remove(my_file)
      print(filename +"删除完成")
    except:
      print(filename +"删除失败")
      pass

def tinyImages(url):
  print('开始转换')
  if url:
    url_image(url)
  else:
    local_images()
  print('转换结束')


# 压缩文件夹
def make_zip(source_dir, output_filename):
  zipf = zipfile.ZipFile(output_filename, 'w')
  pre_len = len(os.path.dirname(source_dir))
  for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
      pathfile = os.path.join(parent, filename)
      arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
      zipf.write(pathfile, arcname)
  zipf.close()

#make_zip(output_dir,'test.zip')

tinyImages(image_url)