$(function() {
$('#contact_form').ajaxForm(function(data){
    $('.contact_form').html(data);
    notify();
}); // ajaxform
});
function notify() {

    var errors = ${ errors }

    if (!errors){
        $.growl.success({ title: "We sent you an email!", message: "Confirm your invite by clicking the confirmation link.  Make sure to check your Spam folder", size:"large", duration:8000 });
    }
    else {

        %for v in form_errors:
            $.growl.error({ title: "Oops!", message: "${v}" });
        %endfor
    }

}
