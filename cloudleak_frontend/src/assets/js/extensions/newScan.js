let $ = require("jquery");

$("#startScan").on("submit", function (e) {
  const target = $("#target").val();
  const platform = $("#basicSelect").val();

  $.ajax({
    type: "POST",
    url: "http://localhost:8000/api/startScan",
    data: { target_scan: target, platform_scan: platform },
    dataType: "json",
    success(response) {
      alert("succuess", response);
    },
    error(response) {
      alert("Error", response);
    },
  });
});
