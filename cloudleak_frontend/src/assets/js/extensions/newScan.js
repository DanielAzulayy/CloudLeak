let $ = require("jquery");

$("#startScan").on("submit", function () {
  const target = $("#target").val();
  const platform = $("#platform-select").val();

  $.ajax({
    url: "http://127.0.0.1:5000/api/scans",
    type: "POST",
    data: JSON.stringify({ target, platform }),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    error: function () {
      // TODO: add alert with sweet alert
      alert("Failed to start scan. Check logs as well.");
    },
    success: function () {
      return;
    },
  });
});
