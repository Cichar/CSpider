/**
 * Created by Cichar on 2017/7/26.
 */

var host = $(location).attr('host'),
        protocol = $(location).attr('protocol') === 'http:' ? 'ws://' : 'wss://',
        ws = new WebSocket(protocol + host  + "/update-tasks");
    ws.onmessage = function (event) {
        var update = $.parseJSON(event.data);
        tasks_update(update);
    };

/*
    Worker Table
 */
var tasks_table = $("#tasks-table").DataTable({
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
            targets: [ 0, 1, 2, 3, 4],
            className: 'c-table-td'
        },
        {
            targets: 0,
            data: 'name'
        }, {
            targets: 1,
            data: 'success'
        }, {
            targets: 2,
            data: 'failed'
        } ,{
            targets: 3,
            data: 'remain'
        } , {
            targets: 4,
            data: 'status',
            render: function (data, type, full, meta) {
                if (data === 'running') {
                    return '<span class="">Running</span>';
                }
                else if (data === 'success'){
                    return '<span class="">Success</span>';
                } else {
                    return '<span class="">Stop</span>';
                }
            }
        }
    ]
});

function tasks_update(update) {

    $.each(update, function (id, info) {
        try {
            var row = tasks_table.row('#' + id );
            if (row) {
                row.data(info);
            } else {
                tasks_table.row.add(info);
            }
        }catch (err){
        }
    });
    tasks_table.draw();
}
