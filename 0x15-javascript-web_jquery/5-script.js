$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    const newListItem = $('<li>').text('Item');
    $('UL.my_list').append(newListItem);
  });
});
