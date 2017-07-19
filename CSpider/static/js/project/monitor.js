/**
 * Created by Cichar on 2017/7/18.
 */

var host = $(location).attr('host'),
        protocol = $(location).attr('protocol') === 'http:' ? 'ws://' : 'wss://',
        ws = new WebSocket(protocol + host  + "/update-monitor");
    ws.onmessage = function (event) {
        var update = $.parseJSON(event.data);
        workers_update(update);
        status_data_update(update);
    };

/*
    EChart Initial
 */
var statusChart = echarts.init(document.getElementById('worker-status-chart'));

var statusData = [];
var statusDate = [];

for (var i = 0; i < 120; i++) {
    statusData.push(null);
    statusDate.push('')
}

var option = {
    title: {
        text: 'Workers Status'
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
        data: statusDate,
        splitLine: {
            show: false
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
        data: statusData
    }]
};

statusChart.setOption(option);

function status_data_update(update) {
    var now = new Date();
    var data = {
        value: [
            [now.getHours(), now.getMinutes(), now.getSeconds()].join(':'),
            update.active
        ]
    };
    statusData.shift();
    statusDate.shift();
    statusData.push(data);
    statusDate.push(data.value[0]);

    statusChart.setOption({
        xAxis: {
            data: statusDate
        },
        series: [{
            data: statusData
        }]
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
