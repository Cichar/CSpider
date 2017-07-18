/**
 * Created by Cichar on 2017/7/18.
 */

var host = $(location).attr('host'),
        protocol = $(location).attr('protocol') === 'http:' ? 'ws://' : 'wss://',
        ws = new WebSocket(protocol + host  + "/update-monitor");
    ws.onmessage = function (event) {
        var update = $.parseJSON(event.data);
        workers_update(update);
        graph_status_data(update)
    };


/*
    Initial Chart Canvas
*/
var statusData = {
        labels : [],
        datasets: [
            {
                label: "Running",
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(0,192,239,0.4)",
                // line color
                borderColor: "rgba(0,192,239,1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(0,192,239,1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                // point background color
                pointHoverBackgroundColor: "rgba(0,192,239,1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [],
                spanGaps: false
            }
        ]
    };

var statusOptions = {
    scales: {
        yAxes: [{
            ticks: {
            }
        }],
        xAxes: [{
            ticks: {
                  callback: function(value) {
                      return null;
                  }
            }
        }]
    }
};

var statusChartCanvas = $("#cluster_status_Chart").get(0).getContext("2d");

// X Cell
for (var i = 0; i < 120; i++) {
    statusData.labels.push('');
    statusData.datasets[0].data.push(null);
}

var statusChart = new Chart(statusChartCanvas, {
    type: 'line',
    data: statusData,
    options: statusOptions
});

function graph_status_data(data) {

    // 进行中
    statusData.datasets[0].data.shift();
    statusData.labels.shift();

    var label = '';

    // 进行中
    statusData.datasets[0].data.push(data.active);
    statusData.labels.push(label);

    statusChart.update();
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
