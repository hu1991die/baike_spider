#coding=utf-8
# Created by feizi at 2016/2/23

#html页面输出器
class HtmlOutputer(object):
    #在构造函数定义一个数据列表
    def __init__(self):
        self.datas = []

    #收集页面数据信息
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    #用于将收集到的数据信息显示到一个html页面中
    def output_html(self):
        #定义一个open输出对象，使用写模式
        fout = open('output.html', 'w')

        fout.write("<!DOCTYPE html>")
        fout.write("""<html lang="en">""")
        fout.write("""<head><meta charset="UTF-8"><title>python爬虫百度百科页面</title></head>""")
        fout.write("""<html lang="en">""")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<th>url链接</th>")
        fout.write("<th>标题</th>")
        fout.write("<th>内容</th>")
        fout.write("</tr>")

        # python 默认的编码格式为ascii，这里需要进行转码
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()