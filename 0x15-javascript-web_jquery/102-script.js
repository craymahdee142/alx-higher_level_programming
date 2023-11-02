$(document).ready(function () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $('INPUT#btn_translate').click(function () {
    $.get(apiUrl + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
