# -*- utf-8 -*-

from Htmlrender.decorator import check_args

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/29'
__Version__ = '0.1'


class Table(object):
    """ Automatic Render Table """

    TABLE_HEAD = '<th class="c-table-td">{0}</th>'
    TABLE_ROW_TD = '<td class="c-table-td">{0}</td>'

    RENDER_HTML = """
                    <div class="{_class}" style="margin-bottom: {margin_bottom};">
                        <div class='c-table-title' style="font-size: {title_size}; 
                                                          font-weight: {title_weight}">{title}</div>
                        <table class="c-table text-center dataTable no-footer">
                            <thead>
                                <tr role="row">
                                    {head}
                                </tr>
                            </thead>
                            <tbody>
                                {body}
                            </tbody>
                        </table>
                    </div>
                  """

    FUNCTIONS = ['_add_head', '_add_body']

    @check_args
    def __init__(self, title: str='', head: list=None, body: list=None, _class: str='col-md-12',
                 margin_bottom: str='50px', title_size: str='', title_weight: int=600):
        self.title = title
        self.head = head
        self.body = body
        self._class = _class
        self.margin_bottom = margin_bottom
        self.title_size = title_size
        self.title_weight = title_weight

        for func in self.FUNCTIONS:
            getattr(self, func)()

    def _add_head(self):
        head = ''
        for v in self.head:
            head += self.TABLE_HEAD.format(v)
        self.head = head

    def _add_body(self):
        body = ''
        for _list in self.body:
            row = '<tr>'
            for v in _list:
                row += self.TABLE_ROW_TD.format(v)
            row += '</tr>'
            body += row
        self.body = body

    def render(self):
        return self.RENDER_HTML.format(title=self.title, head=self.head, body=self.body,
                                       _class=self._class, margin_bottom=self.margin_bottom,
                                       title_size=self.title_size, title_weight=self.title_weight)
