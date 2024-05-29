$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      type: 'POST',
      datatype: 'json',
      data: { lang: $('INPUT#language_code').val() },
      success: function (response) {
        $('DIV#hello').html(response.hello);
      }
    });
  });
});
