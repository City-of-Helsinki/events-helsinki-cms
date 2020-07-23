$(documentReady);

function documentReady() {
  scrollToValidationError();
}

function scrollToValidationError() {
  secondErrorMessage = $(".error").get(1);

  if (secondErrorMessage) {
    secondErrorMessage.scrollIntoView({ behavior: "smooth" });
  }
}
