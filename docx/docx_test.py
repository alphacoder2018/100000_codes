from docx import Document
from docx.shared import  Pt
from docx.oxml.ns import  qn
from docx.shared import Inches
#如果程序文件名字是 docx.py，程序又 from docx import Document 的话，就会出现ImportError: cannot import name 'Document'错误。
#创建对象
document = Document()




#加入不同等级的标题
document.add_heading('面向API编程：使用python编辑word文档',0)
document.add_heading(u'二级标题 人生苦短，我用python.',1)
document.add_heading(u'二级标题 这个系列主要学习记录使用python实现办公自动化。',2)

#添加文本
paragraph = document.add_paragraph(u'添加了文本 那么就从最常见的办公三件套 -----word开始。')
#设置字号
run = paragraph.add_run(u'设置字号')
run.font.size=Pt(36)

#设置字体
run = paragraph.add_run('Set Font,')
run.font.name='Consolas'

#设置中文字体
run = paragraph.add_run(u'设置中文字体，')
run.font.name=u'宋体'
r = run._element
r.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

#设置斜体
run = paragraph.add_run(u'斜体、')
run.italic = True

#设置粗体
run = paragraph.add_run(u'粗体').bold = True

#增加引用
document.add_paragraph('Intense quote', style='Intense Quote')

#增加有序列表
document.add_paragraph(
    u'有序列表元素1',style='List Number'
)
document.add_paragraph(
    u'有序列别元素2',style='List Number'
)

#增加无序列表
document.add_paragraph(
    u'无序列表元素1',style='List Bullet'
)
document.add_paragraph(
    u'无序列表元素2',style='List Bullet'
)

#增加图片（此处使用相对位置）
document.add_picture('docx.jpg',width=Inches(3.25))

#增加表格
table = document.add_table(rows=3,cols=3)
for i in range(0,3):
  hdr_cells=table.rows[i].cells
  for j in range(0,3):
    hdr_cells[j].text="第%s列第%d行"%(j+1,i+1)

#增加分页
document.add_page_break()

#保存文件
document.save('test.docx')

