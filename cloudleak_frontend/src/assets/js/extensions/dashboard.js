let $ = require("jquery");
const axios = require("axios");

$(async function () {
    loadScans();

});

async function loadScans () {
    let response = await axios.get("http://127.0.0.1:5000/api/scans");
    const allScans = response.data['results'];

    $.each(allScans, (index, row) => {
        const rowContent = `<tr>
                <td>${index+=1}</td>
                <td>${row.target}</td>
                <td>${row.status}</td>
                <td>${(row.platform).toUpperCase()}</td>
                <td>${row.added_ts}</td>
                <td></td>
                <td>abort/kill</td>
            </tr>`;
        $("#scans").append(rowContent);
  });
}
