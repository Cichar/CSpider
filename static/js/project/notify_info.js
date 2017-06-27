/**
 * Created by Cichar on 2017/6/27.
 */

/*
    消息通知
 */
function notify_success(message, callback) {

    iziToast.success({
        title: 'OK',
        message: message,
        position: 'bottomRight',
        transitionIn: 'bounceInLeft',
        onClose: function(){
            if(callback===true){
                window.location.reload()
            }
        }
    });
}

function notify_info(message, callback) {
    iziToast.info({
        color: '#ffffff',
        title: 'INFO',
        message: message,
        position: 'bottomRight',
        transitionIn: 'bounceInLeft',
        onClose: function(){
            if(callback===true){
                window.location.reload()
            }
        }
    });
}

function notify_warning(message, callback) {

    iziToast.warning({
        title: 'WARNING',
        message: message,
        position: 'bottomRight',
        transitionIn: 'bounceInLeft',
        onClose: function(){
            if(callback===true){
                window.location.reload()
            }
        }
    });
}

function notify_error(message, callback) {

    iziToast.error({
        title: 'ERROR',
        message: message,
        position: 'bottomRight',
        transitionIn: 'bounceInLeft',
        onClose: function(){
            if(callback===true){
                window.location.reload()
            }
        }
    });
}

