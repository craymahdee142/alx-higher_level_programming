$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (enter) {
      if (enter.keydown === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $.get(apiUrl + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
