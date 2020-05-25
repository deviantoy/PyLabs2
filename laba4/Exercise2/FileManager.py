import xml.etree.ElementTree as ET
import wx
import json


class FileManager(object):
    @staticmethod
    def save_author_info_XML(author_info):
        ID, name, country, years = author_info
        born_year, death_year = years.split('-')
        xml = '''
        <?xml version="1.0"?>
        <author>
            <name>''' + name + '''</name>
            <country>''' + country + '''</country>
            <years born="''' + born_year + '''" died="''' + death_year + '''"/>
        </author>
        '''
        with open(str(name)+'.xml', 'w') as f:
            f.write(xml)

    @staticmethod
    def save_book_info_xml(book):
        authors_id, title, sheets, publisher, year = book
        xml = '''
        <?xml verison="1.0"?>
        <book>
            <author_id>''' + str(authors_id) + '''</author_id>
            <title>''' + title + '''</title>
            <sheets>''' + str(sheets) + '''</sheets>
            <publisher>''' + publisher + '''</publisher>
            <year>''' + str(year) + '''</year>
        </book>'''
        with open(str(title)+'.xml', 'w') as f:
            f.write(xml)

    @staticmethod
    def save_author_info_json(author_info):
        ID, name, country, years = author_info
        with open(str(name)+'.json', 'w') as f:
            f.write(json.dumps(author_info))

    @staticmethod
    def save_book_info_json(book):
        authors_id, title, sheets, publisher, year = book
        with open(str(title)+'.json', 'w') as f:
            f.write(json.dumps(book))

    @staticmethod
    def load_author_info():
        name, country, years = None, None, None

        dlg = wx.FileDialog(None, message='Выберите файл',
                            defaultDir='', defaultFile='',
                            wildcard='*.*', style=wx.FLP_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            tree = ET.parse(dlg.GetPath())
            root = tree.getroot()
            for child in root:
                if child.tag == 'name':
                    name = child.text
                if child.tag == 'country':
                    country = child.text
                if child.tag == 'years':
                    years = child.attrib['born'] + '-' + child.attrib['died']
            return name, country, years
        return None

