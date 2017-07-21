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
var WorkerData = [];
var WorkerDate = [];
var WorkerScaleNum = 120;
var WorkerChart = echarts.init(document.getElementById('worker-status-chart'));

for (var i = 0; i < WorkerScaleNum; i++) {
    WorkerData.push(null);
    WorkerDate.push('')
}

var WorkerChartOption = {
    title: {
        text: 'Running Task'
    },
    tooltip: {
        trigger: 'axis',
        formatter: function (data) {
            data = data[0];
            return data.value[0] + ' / ' + data.value[1];
        },
        axisPointer: {
            animation: false
        }
    },
    xAxis: {
        type: 'category',
        data: WorkerDate,
        splitLine: {
            show: false
        },
        axisLabel: {
            interval: WorkerScaleNum/6
        }
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '50%'],
        splitLine: {
            show: false
        }
    },
    series: [{
        name: 'Running',
        type: 'line',
        showSymbol: false,
        hoverAnimation: false,
        data: WorkerData
    }]
};


var QueueData = {};
var QueueDate = [];
var QueueScaleNum = 1000;
var QueueChart = echarts.init(document.getElementById('queue-status-chart'));

for (var i = 0; i < QueueScaleNum; i++) {
    QueueDate.push('')
}

var QueueChartOption = {
    title: {
        text: 'Queue Info'
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
        }
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '20%'],
        splitLine: {
            show: false
        }
    },
    series: []
};

WorkerChart.setOption(WorkerChartOption);
QueueChart.setOption(QueueChartOption);

function chart_update(active, queues) {
    var now = new Date();
    var data = {
        value: [
            [now.getHours(), now.getMinutes(), now.getSeconds()].join(':'),
            active
        ]
    };
    WorkerData.shift();
    WorkerDate.shift();
    WorkerData.push(data);
    WorkerDate.push(data.value[0]);
    QueueDate.push(data.value[0]);

    WorkerChart.setOption({
        xAxis: {
            data: WorkerDate
        },
        series: [{
            data: WorkerData
        }]
    });

    function queue_data(){
        var _length = queues.length;
        // If QueueData is empty, then create queues dict to store queue's data
        if ($.isEmptyObject(QueueData)) {
            for (var i = 0; i < _length; i++) {
                QueueData[queues[i].name] = {data: []};
                for (var n = 0; n < QueueScaleNum; n++) {
                    QueueData[queues[i].name].data.push(null)
                }
            }
        }

        // Update queue's info
        for (var i = 0; i < _length; i++){
            QueueData[queues[i].name].data.shift();
            QueueData[queues[i].name].data.push(queues[i].messages);
        }

        var series = [];
        for(var i = 0; i < _length; i++){
            var item = {
                name: queues[i].name,
                type: 'line',
                data: QueueData[queues[i].name].data
            };
            series.push(item);
        }
        return series;
    }

    QueueChart.setOption({
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
