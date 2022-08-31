let $ = require("jquery");
const axios = require("axios");

$(async function () {
  loadBucketsEndpoints();
});

async function loadBucketsEndpoints() {
  let response = await axios.get("http://127.0.0.1:5000/api/scans");
  const allScans = response.data["results"];

  $.each(allScans, (index, row) => {
    if (!row?.buckets) return;

    for (let bucket of row.buckets) {
      let rowContent = `<tr>
            <td><a href=https://${bucket.bucket}> ${bucket.bucket}</a></td>
            <td>${bucket.platform}</td>;
            <td>${bucket.service}</td>;
        </tr>`;
      $("#bucket-scan-results").append(rowContent);
    }
  });
}
