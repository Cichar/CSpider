# -*- utf-8 -*-

__Author__ = 'Cichar'
__Email__ = '363655056@qq.com'
__CreateDate__ = '2017/7/29'
__Version__ = '0.1'


class BaseChart(object):
    """ This Base Charts Class For Automatic Render EChart Lib. """

    RENDER_HTML = """
                     <div id="{render_id}" style="width:{width};height:{height};"></div> 
                     <script type="text/javascript"> 
                        var {name} = echarts.init(document.getElementById('{render_id}'));
                        var option = {option}; 
                        {name}.setOption(option); 
                     </script>
                  """

    FUNCTIONS = ['_add_tooltip', '_add_x_axis', '_add_y_axis', '_add_series']

    def __init__(self, title, subtitle=None, toolbox=False, name='myChart',
                 width='100%', height='400px', render_id=None):
        if not name or not isinstance(name, str):
            raise ValueError('name is required and must be string type.')
        if not render_id or not isinstance(render_id, str):
            raise ValueError('render_id is required and must be string type.')
        if not width or not isinstance(width, str):
            raise ValueError('width is required and must be string type, such as "100%" or "400px"')
        if not height or not isinstance(height, str):
            raise ValueError('height is required and must be string type, such as "20%" or "400px"')
        self._name = name
        self._width = width
        self._height = height
        self._render_id = render_id

        self._option = {}
        self._add_title(title, subtitle)
        if toolbox:
            self._add_toolbox()
        for func in self.FUNCTIONS:
            getattr(self, func)()

    def _add_title(self, title, subtitle):
        """ Add The Title And Subtitle For The Cecharts """

        self._option['title'] = {"text": title}
        if subtitle:
            self._option['title'].update({"subtext": subtitle})

    def update_title(self, **kwargs):
        """ Update The Title Configuration """

        self._option['title'].update(kwargs)

    def _add_toolbox(self):
        """ Add The Toolbox For The Cecharts """

        self._option['toolbox'] = {"left": "right",
                                   "feature": {
                                                "saveAsImage": {}
                                              }
                                   }

    def update_toolbox(self, **kwargs):
        """ Update The Toolbox Configuration """

        self._option['toolbox'].update(kwargs)

    def _add_tooltip(self):
        """ Add The Tooltip For The Cecharts """

        self._option['tooltip'] = {'trigger': 'axis'}

    def update_tooltip(self):
        # """ Update The Tooltip Configuration """
        pass

    def _add_legend(self):
        """ Add The Legend For The Cecharts """

        self._option['legend'] = {'data': []}

    def _update_legend(self, data):
        """ Update The Legend Configuration """

        if not self._option.get('legend', None):
            self._add_legend()
        if not isinstance(data, list):
            raise TypeError('data must be list type, get {0} type'.format(type(data).__name__))
        self._option['legend']['data'].extend(data)

    def _add_x_axis(self):
        """ Initial The xAxis Configuration """

        self._option['xAxis'] = []

    def update_x_axis(self, data, _type='category'):
        self._option['xAxis'].append({
            'type': _type,
            'data': data
        })

    def _add_y_axis(self):
        """ Initial The yAxis Configuration """

        self._option['yAxis'] = []

    def update_y_axis(self, _type='value'):
        self._option['yAxis'].append({
            'type': _type
        })

    def _add_series(self):
        """ Initial The Series Configuration """

        self._option['series'] = []

    def update_series(self, datas, legend=True):
        raise NotImplementedError()

    def render(self):
        """ Render Cecharts """

        if not self._option.get('yAxis'):
            self.update_y_axis()
        return self.RENDER_HTML.format(render_id=self._render_id, width=self._width,
                                       height=self._height, name=self._name, option=self._option)

    def __str__(self):
        return '%s' % self._option


if __name__ == '__main__':
    a = BaseChart('Test', render_id='test', toolbox=True)
    a.update_title(top='center')
    print(a)
