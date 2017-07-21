/**
 * Created by Cichar on 2017/7/18.
 */

var host = $(location).attr('host'),
        protocol = $(location).attr('protocol') === 'http:' ? 'ws://' : 'wss://',
        ws = new WebSocket(protocol + host  + "/update-monitor");
    ws.onmessage = function (event) {
        var update = $.parseJSON(event.data);
        workers_update(update.workers);
        chart_update(update.active, update.queues);
    };

/*
    EChart Initial
 */
var QueueData = {};
var QueueLegend = [];
var LegendSelected = {};
var QueueDate = [];
var QueueScaleNum = 360;
var QueueChart = echarts.init(document.getElementById('queue-status-chart'));

for (var i = 0; i < QueueScaleNum; i++) {
    QueueDate.push('')
}

var QueueChartOption = {
    title: {
        text: 'Queue Info And Active Task',
        x: 'center'
    },
    tooltip: {
        trigger: 'axis'
    },
    xAxis: {
        type: 'category',
        data: QueueDate,
        splitLine: {
            show: false
        },
        axisLabel: {
            interval: QueueScaleNum/6
        },
        boundaryGap: false
    },
    yAxis: [
        {
            type: 'value',
            boundaryGap: [0, '20%'],
            splitLine: {
                show: false
            }
        },
        {
            type: 'value',
            boundaryGap: [0, '20%'],
            splitLine: {
                show: false
            }
        }
    ],
    series: []
};
QueueChart.setOption(QueueChartOption);

function chart_update(active, queues) {
    var now = new Date();
    QueueDate.shift();
    QueueDate.push([now.getHours(), now.getMinutes(), now.getSeconds()].join(':'));

    function queue_data(){
        var _length = queues.length;

        if ($.isEmptyObject(QueueLegend)) {
            for (var i = 0; i < _length; i++) {
                QueueLegend.push(queues[i].name);
            }
            QueueLegend.push('Active')
        }

        // If QueueData is empty, then create queues dict to store queue's data
        if ($.isEmptyObject(QueueData)) {
            for (var i = 0; i < QueueLegend.length; i++){
                QueueData[QueueLegend[i]] = {data: []};
                for (var n = 0; n < QueueScaleNum; n++) {
                    QueueData[QueueLegend[i]].data.push(null)
                }
            }
        }

        // Update queue's info
        for (var i = 0; i < _length; i++){
            QueueData[queues[i].name].data.shift();
            QueueData[queues[i].name].data.push(queues[i].messages);

            // Legend Selected Depend On The Data Is Or Not Zero
            LegendSelected[queues[i].name] = queues[i].messages;
        }
        QueueData['Active'].data.shift();
        QueueData['Active'].data.push(active);

        var series = [];
        for(var i = 0; i < _length; i++){
            var item = {
                name: queues[i].name,
                type: 'bar',
                data: QueueData[queues[i].name].data
            };
            series.push(item);
        }
        series.push({
            name: 'Active',
            type: 'line',
            yAxisIndex: 1,
            smooth: true,
            lineStyle: {
                normal: {
                    width: 1
                }
            },
            smoothMonotone: 'x',
            showSymbol: false,
            hoverAnimation: false,
            data: QueueData['Active'].data
        });
        return series;
    }

    QueueChart.setOption({
        legend: {
            top: 30,
            formatter: function (name) {
                return echarts.format.truncateText(name, 40, '14px Microsoft Yahei', '…');
            },
            tooltip: {
                show: true
            },
            selected: LegendSelected,
            data: QueueLegend
        },
        xAxis: {
            data: QueueDate
        },
        series: queue_data()
    });
}

/*
    Worker Table
 */
var workers_table = $("#workers-table").DataTable({
    'select': true,
    "paginate": false,
    "ordering": false,
    "order": [],
    "language": {
        // "url": "static/dataTables/datatables_chinese.json"
    },
    "createdRow": function ( row, data, index ) {
            $('td', row).css({'word-wrap':'break-word','word-break':'break-all', 'vertical-align':"middle"});
    },
    "columnDefs": [{
            targets: [ 0, 1, 2, 3, 4, 5, 6],
            className: 'c-table-td'
        },
        {
            targets: 0,
            data: 'name'
        }, {
            targets: 1,
            data: 'status',
            render: function (data, type, full, meta) {
                if (data === 'ONLINE') {
                    return '<span class="">ONLINE</span>';
                } else {
                    return '<span class="">OFFLINE</span>';
                }
            }
        }, {
            targets: 2,
            data: 'active'
        } ,{
            targets: 3,
            data: 'retried'
        } , {
            targets: 4,
            data: 'failed'
        }
        , {
            targets: 5,
            data: 'succeeded'
        }
        , {
            targets: 6,
            data: 'processed'
        }
        ]
});

function workers_update(update) {

    $.each(update, function (name, info) {
        try {
            var row = workers_table.row('#' + name );
            if (row) {
                row.data(info);
            } else {
                workers_table.row.add(info);
            }
        }catch (err){
        }
    });
    workers_table.draw();
}
