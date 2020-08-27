$(documentReady);

function documentReady() {
  removeFocalPointInImageEditorInterface();
}

function removeFocalPointInImageEditorInterface() {
  $(".focal-point-chooser")
    .next()
    .find(".col8.divider-after")
    .remove();
}
