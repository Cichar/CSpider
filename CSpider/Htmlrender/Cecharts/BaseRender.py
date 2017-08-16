# -*- utf-8 -*-

RENDER_TO_WEB = """
                 <div id="{render_id}" style="width:{width};height:{height};"></div> 
                 <script type="text/javascript"> 
                    var {name} = echarts.init(document.getElementById('{render_id}'));
                    var option = {option}; 
                    {name}.setOption(option); 
                 </script>
              """
