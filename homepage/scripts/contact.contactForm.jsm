$(function() {
$('#contact_form').ajaxForm(function(data){
    $('.contact_form').html(data);
    notify();
}); // ajaxform
});
function notify() {

    var errors = ${ errors }

    if (!errors){
        $.growl.success({ title: "Thank You!", message: "Your Email Has Been Sent", size:"large", duration:8000 });
    }
    else {

        %for v in form_errors:
            $.growl.error({ title: "Oops!", message: "${v}" });
        %endfor
    }

}
