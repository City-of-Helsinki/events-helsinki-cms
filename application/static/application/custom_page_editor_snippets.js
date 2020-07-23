$(documentReady);

function documentReady() {
  scrollToValidationError();
  addLinksForCuratedEvents();
}

function scrollToValidationError() {
  secondErrorMessage = $(".error").get(1);

  if (secondErrorMessage) {
    secondErrorMessage.scrollIntoView({ behavior: "smooth" });
  }
}

function addLinksForCuratedEvents() {
  eventLinks = $("input[placeholder*='Event link']");

  for (eventLink of eventLinks) {
    eventPageLink = `<a href='${eventLink.value}'>Link to event page</a>`;
    $(eventPageLink).insertAfter(eventLink);
  }
}
