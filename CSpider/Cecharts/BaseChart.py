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
        """
        :param title: 
                    Chart's Title.
        :param subtitle: 
                    Charts's subtitle.
        :param toolbox: 
                    Show Or Not Show Chart's Toolbox. Default Is ''False''.
        :param name: 
                    The Name For Render In Web Page. Default Is ''myChart''.
                    User Need To Provide Another Name To Support When The 
                    Web Page Has More Than One Chart.
        :param width: 
                    The Width For Render In Web Page. Default Is ''100%''.
        :param height: 
                    The Height For Render In Web Page. Default Is ''400px''.
        :param render_id: 
                    The Id For JS To Select, Then ECharts Initial The Object.
        """

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
        """ Add The Title And Subtitle For The Chart """

        self._option['title'] = {"text": title}
        if subtitle:
            self._option['title'].update({"subtext": subtitle})

    def update_title(self, show=None, link=None, target=None, text_color=None, text_font_style=None,
                     text_font_weight=None, text_font_family=None, text_font_size=None,text_align=None,
                     text_base_line=None, sub_link=None, sub_target=None, sub_text_style=None,
                     padding=None, item_gap=None, z_level=None, z=None, left=None, top=None, right=None,
                     bottom=None, background_color=None, border_color=None, border_width=None, shadow_blur=None,
                     shadow_color=None, shadow_offset_x=None, shadow_offset_y=None):
        """ Update The Title Configuration """

        title_option = {
            'show': show,
            'link': link,
            'target': target,
            'textStyle': {
                'color': text_color,
                'fontStyle': text_font_style,
                'fontWeight': text_font_weight,
                'fontFamily': text_font_family,
                'fontSize': text_font_size,
            },
            'textAlign': text_align,
            'textBaseline': text_base_line,
            'sublink': sub_link,
            'subtarget': sub_target,
            'subtextStyle': sub_text_style,
            'padding': padding,
            'itemGap': item_gap,
            'zlevel': z_level,
            'z': z,
            'left': left,
            'top': top,
            'right': right,
            'bottom': bottom,
            'backgroundColor': background_color,
            'borderColor': border_color,
            'borderWidth': border_width,
            'shadowBlur': shadow_blur,
            'shadowColor': shadow_color,
            'shadowOffsetX': shadow_offset_x,
            'shadowOffsetY': shadow_offset_y
        }

        self._update_option('title', title_option)

    def _add_legend(self):
        """ Add The Legend For The Chart """

        self._option['legend'] = {'data': []}

    def update_legend(self, show=None, z_level=None, z=None, left=None, top=None, right=None,
                       bottom=None, width=None, height=None, orient=None, align=None, padding=None,
                       item_gap=None, item_width=None, item_height=None, formatter=None, selected_mode=None,
                       inactive_color=None, selected=None, text_color=None, text_font_style=None,
                       text_font_weight=None, text_font_family=None, text_font_size=None, data=None,
                       background_color=None, border_color=None, border_width=None, shadow_blur=None,
                       shadow_color=None, shadow_offset_x=None, shadow_offset_y=None):
        """ Update The Legend Configuration """

        if not self._option.get('legend', None):
            self._add_legend()
        if not isinstance(data, list):
            raise TypeError('data must be list type, get {0} type'.format(type(data).__name__))

        legend_option = {
            'show': show,
            'zlevel': z_level,
            'z': z,
            'left': left,
            'top': top,
            'right': right,
            'bottom': bottom,
            'width': width,
            'height': height,
            'orient': orient,
            'align': align,
            'padding': padding,
            'itemGap': item_gap,
            'itemWidth': item_width,
            'itemHeight': item_height,
            'formatter': formatter,
            'selectedMode': selected_mode,
            'inactiveColor': inactive_color,
            'selected': selected,
            'textStyle': {
                'color': text_color,
                'fontStyle': text_font_style,
                'fontWeight': text_font_weight,
                'fontFamily': text_font_family,
                'fontSize': text_font_size,
            },
            'data': data,
            'backgroundColor': background_color,
            'borderColor': border_color,
            'borderWidth': border_width,
            'shadowBlur': shadow_blur,
            'shadowColor': shadow_color,
            'shadowOffsetX': shadow_offset_x,
            'shadowOffsetY': shadow_offset_y
        }

        self._update_option('legend', legend_option)

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

    def _add_tooltip(self):
        """ Add The Tooltip For The Chart """

        self._option['tooltip'] = {'trigger': 'axis'}

    def update_tooltip(self):
        # """ Update The Tooltip Configuration """
        pass

    def _add_toolbox(self):
        """ Add The Toolbox For The Chart """

        self._option['toolbox'] = {"left": "right",
                                   "feature": {
                                                "saveAsImage": {}
                                              }
                                   }

    def update_toolbox(self, **kwargs):
        """ Update The Toolbox Configuration """

        self._option['toolbox'].update(kwargs)

    def _add_series(self):
        """ Initial The Series Configuration """

        self._option['series'] = []

    def update_series(self, datas, legend=True):
        raise NotImplementedError()

    def _update_option(self, key, option):
        """ Used To Update The Option In ''self._option[key]'' """

        if not isinstance(key, str):
            raise TypeError('key must be string type, get {0} type.'.format(type(key).__name__))
        if not isinstance(option, dict):
            raise TypeError('option must be dict type, get {0} type.'.format(type(option).__name__))

        for k, v in option.items():
            if v:
                if isinstance(v, dict):
                    for _k, _v in v.items():
                        if _v:
                            if not self._option[key].get(k, None):
                                self._option[key].update({k: {}})
                            self._option[key][k].update({_k: _v})
                else:
                    self._option[key].update({k: v})

    def render(self):
        """ Render Chart """

        if not self._option.get('yAxis'):
            self.update_y_axis()
        return self.RENDER_HTML.format(render_id=self._render_id, width=self._width,
                                       height=self._height, name=self._name, option=self._option)

    def __str__(self):
        return '%s' % self._option


if __name__ == '__main__':
    a = BaseChart('Test', render_id='test', toolbox=True)
    a.update_title()
    print(a)
