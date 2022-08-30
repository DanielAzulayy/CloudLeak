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
      if (!bucket?.files) return;

      for (let endpoint of bucket.files) {
        let rowContent = `<tr>
                <td>${bucket.platform}</td>
                <td>${bucket.service}</td>;
                <td><a href=${endpoint}> ${endpoint}</a></td>
                <td><span class="badge bg-success">Active</span></td>
            </tr>`;
        $("#bucket-endpoints").append(rowContent);
      }
    }
  });
}
