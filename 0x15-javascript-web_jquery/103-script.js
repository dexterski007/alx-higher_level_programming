$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  });

  $('INPUT#language_code').on('keypress', function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });

  const translate = function () {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      type: 'POST',
      datatype: 'json',
      data: { lang: $('INPUT#language_code').val() },
      success: function (response) {
        $('DIV#hello').html(response.hello);
      }
    });
  };
});
