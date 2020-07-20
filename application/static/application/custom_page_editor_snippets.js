$(document).ready(function() {
  second_error_message = $(".error").get(1);

  if (second_error_message) {
    second_error_message.scrollIntoView({ behavior: "smooth" });
  }
});
