$(document).ready(function() {

  $("#account-select").change(function() {
    $("#show-address").show('slide');
    window.scrollTo(0,document.body.scrollHeight);
  });

  $("#show-address").click(function(){
    $("#address-history").show('slide');
    window.scrollTo(0,document.body.scrollHeight);
  });

  $("#yes").click(function(){
    $("#current-address").show('slide');
    $("#non-uk").hide();
    window.scrollTo(0,document.body.scrollHeight);
  });

  $("#no").click(function(){
    $("#non-uk").show('slide');
    $("#current-address").hide();
    window.scrollTo(0,document.body.scrollHeight);
  });

  $("#yes-prev").click(function(){
    $("#previous-address").show('slide');
    $("#get-consent").show('slide');
    window.scrollTo(0,document.body.scrollHeight);
  });

   $("#no-prev").click(function(){
    $("#get-consent").show('slide');
    $("#previous-address").hide();
    window.scrollTo(0,document.body.scrollHeight);
  });

  $("#get-consent").click(function(){
    $("#your-consent").show('slide');
    window.scrollTo(0,document.body.scrollHeight);
  });

  $("#credit-click").click(function() {
    $("#info-request").show('slide');
    window.scrollTo(0,document.body.scrollHeight);
  });

  $("#info-click").click(function() {
    $("#submit-app").show('slide');
    window.scrollTo(0,document.body.scrollHeight);
  });

  $('#app-form').on('submit', function(){
    var arr = $(this).serializeArray();
    console.log(arr);
    return false;
});
});